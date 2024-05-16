from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from dataprovider import DataProvider  
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from model import Employee, Task
from admin_controllers import EmployeeManagerController, EmployeeDatabaseManager
from kivy.uix.popup import Popup
from kivy.core.window import Window
from enums import Priority

class EmployeeManagerContentPanel:
    selected_row = -1
    
    employee_manager_controller = EmployeeManagerController()
    employee_database_manager = EmployeeDatabaseManager("intershippython", "123", "localhost", 5432)
    department_list = employee_database_manager.get_department_list()

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_employee_management_panel())
        split_layout_panel.add_widget(self._create_employee_input_data_panel())
        return split_layout_panel
    
    def _create_employee_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=4, spacing=10)
        input_data_component_panel.size_hint_y = None
        input_data_component_panel.height = Window.height * 0.3
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = Window.width *0.7
        
        # Employee name formatting
        self.name_input = MDTextField(
            multiline=True, 
            font_size='18sp', 
            hint_text='Name',
            )
        input_data_component_panel.add_widget(self.name_input)
        # Employee address formatting
        self.address_input = MDTextField(
            multiline=False, 
            font_size='18sp',
              hint_text='Address',
              )
        input_data_component_panel.add_widget(self.address_input)
        # Employee email formatting
        self.email_input = MDTextField(
            multiline=False, 
            font_size='18sp', 
            hint_text='Email',
            )
        input_data_component_panel.add_widget(self.email_input)
        # Employee phone nr formatting
        self.phone_nr_input = MDTextField(
            multiline=False, 
            font_size='18sp', 
            hint_text='Phone Number',
            )
        input_data_component_panel.add_widget(self.phone_nr_input)

        input_data_component_panel.add_widget(self._create_buttons_component_panel())
        return input_data_component_panel

    def _create_employee_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=20)
        content_panel.add_widget(self._create_restaurant_selector())
        content_panel.size_hint_x = None
        content_panel.size_hint_y = None
        content_panel.width = Window.width * 0.7
        content_panel.height= Window.height * 0.7
        content_panel.add_widget(self._create_table_panel())
        return content_panel

    def _create_buttons_component_panel(self):
        button_component_panel = GridLayout(cols=3, padding=0, spacing=30)

        add_button = Button(
            text='Add', 
            size_hint=(None,None),
            size=(100,40), 
            background_color=(0,1,1,1),
            )
        update_button = Button(
            text='Update', 
            size_hint=(None,None),
            size=(100,40), 
            background_color=(0,1,1,1),
            )
        delete_button = Button(
            text='Delete', 
            size_hint=(None,None),
            size=(100,40), 
            background_color=(0,1,1,1),
            )
        add_button.bind(on_pres= self._add_employee)
        delete_button.bind(on_pres= self._delete_employee)
        update_button.bind(on_pres= self._update_employee)
        button_component_panel.add_widget(add_button)
        button_component_panel.add_widget(update_button)
        button_component_panel.add_widget(delete_button)

        return button_component_panel
    
    def _create_table_panel(self):
        table_panel = GridLayout(cols=1, spacing=0)
        self.employee_table = self.create_table()
        #Adds the employee table to the table panel
        self.employee_table.bind(on_check_pres=self._checked)
        self.employee_table.bind(on_row_press=self._on_row_press)
        table_panel.add_widget(self.employee_table)
        return table_panel
    
    def _create_restaurant_selector(self):
        button = Button(
            text='Select a department',
            size_hint=(1, 0.15),
            background_color=(0,1,1,1),
            ) 
        button.bind(on_release=self._show_menu)
        return button
    
    def create_table(self):
        table_row_data = []
        self.department = self.department_list[0]
        employees = self.department.employee_list

        for employee in employees:
            table_row_data.append(
                (employee.name, employee.address, employee.email, employee.phone_nr)
                )

        self.employee_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color_header="7393B3",
            background_color_cesll="#F0FFFF",
            background_color_selected_cell="#ADD8E6",
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", 40),
                ("Address", 40),
                ("Email", 55),
                ("Phone Number", 40),  
            ],
            row_data=table_row_data
        )
        return self.employee_table
    
    def show_menu(self, button):
        menu_items = []
        department_list = self.department_list

        for department in department_list:
            menu_items.append(
                {
                    "viewclass": "OneLineListItem", 
                    "text": department.name,
                    "on_release":lambda d=department: self._update_data_table(d),
                }
            )

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def _checked(self, instance_table, current_row):
        selected_employee = Employee(current_row[0], current_row[1], current_row[2], current_row[3], [])
        
        #assing the emploee data to the input fields
        self.name_input.text = str(selected_employee.name)
        self.address_input.text = str(selected_employee.address)
        self.email_input.text = str(selected_employee.email)
        self.phone_nr_input.text = str(selected_employee.phone_nr)

    def _update_data_table(self, departament):
        self.department = departament

        #get employ data for the selected departament
        table_row_data = []
        employees = departament.employee_list
        for employee in employees:
            table_row_data.append(
                employee.name, employee.address, employee.email, employee.phone_nr
            )
            # update th employee table with data
            self.employee_table.row_data = table_row_data
    
    def _add_employee(self, instanc):
        # get employee data from input fieldes
        name = self.name_input.text
        address = self.address_input.text
        email = self.email_input.text
        phone_nr = self.phone_nr_input.text

        employee_data = []
        employee_data.append(name)
        employee_data.append(address)
        employee_data.append(email)
        employee_data.append(phone_nr)

        if self._is_data_valid(employee_data):
            self.employee_manager_controller.add_employee(
                self.department, employee_data
            )

            self.employee_table.row_data.append([name, address, email, phone_nr])

            self._clear_input_text_fields()

        else:
            popup = Popup(
                title="Invalid data",
                content=Label(text="Provide manatory dta to add a new Employee"),
                size_hint= (None, None),
                size= (400,200),
            )

            popup.open()

    def _on_row_press(self, instance, row):
        #set the row index to delete when a row is pressed
        self.selected_row= int(row.index / len(instance.column_data))

    def _update_employee(self, instance):
        if self.selected_row != -1:
            #Get the updated employee data from the input fieldes
            name = self.name_input.text
            address = self.address_input.text
            email = self.email_input.text
            phone_nr = self.phone_nr_input.text

            employee_data = []
            employee_data.append(name)
            employee_data.append(address)
            employee_data.append(email)
            employee_data.append(phone_nr)

            if self._is_data_valid(employee_data):
                employee_to_remove = self.employee_table.row_data[self.selected_row]

                del self.employee_table.row_data[self.selected_row]
                self.employee_manager_controller.deleted_employee(
                    self.department,employee_to_remove
                )

                self.employee_manager_controller.add_employee(
                    self.department, employee_data
                )

                self.employee_table.row_data.append([name, address, email, phone_nr])
                self._clear_input_text_fields()

            else:
                popup = Popup(
                    title="Invalid data",
                    content=Label(text="Provide manatory dta to add a new Employee"),
                    size_hint= (None, None),
                    size= (400,200),
                )

                popup.open()

        else:
            popup = Popup(
                title="Invalid data",
                content=Label(text="Select any row to update"),
                size_hint= (None, None),
                size= (400,200),
            )

            popup.open()

    def _delete_employee(self, instance):
        if self.selected_row != -1:
            employee_to_remove = self.employee_table.row_data[self.selected_row]

            del self.employee_table.row_data[self.selected_row]
            self.employee_manager_controller.deleted_employee(
                self.department, employee_to_remove
            )

            self._clear_input_text_fields()

        else:
            popup = Popup(
                title="Invalid data",
                content=Label(text="Select any row to delete"),
                size_hint= (None, None),
                size= (400,200),
            )

            popup.open()
    
    def _clear_input_text_fields(self):
        #Clear the input fields by setting their text to emty strings
        self.name_input.text = ""
        self.address_input.text = ""
        self.email_input.text = ""
        self.phone_nr_input.text = ""
        self.selected_row = -1

    def _is_data_valid(self, employee_data):
        #Check if employee data is valid (all fieldes are filled)
        return (
            employee_data[0] != ""
            and employee_data[1] != ""
            and employee_data[2] != ""
            and employee_data[3] != ""
        )


from admin_controllers import TaskManagerController

class TaskManagerContentPanel():
    def __init__(self):
        self.task_manager_controller = TaskManagerController()
        self.departament_list = DataProvider().department_list
        self.department = self.departament_list[0]
        self.employee = self.department.employee_list[0]
        self.departament_selector = None
        self.employee_selector = None
        self.selected_row = -1


    def create_content_panel(self):
       split_layout_panel = GridLayout(cols=2)
       split_layout_panel.add_widget(self._create_employee_input_data_panel())
       split_layout_panel.add_widget(self._create_management_panel())
       return split_layout_panel 

    
    def _create_employee_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1,padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400
         
        #Employee Name
        self.name_input = MDTextField(multiline=True, font_size='18sp', hint_text='Name')
        input_data_component_panel.add_widget(self.name_input)
        
        #Task description
        self.description_input = MDTextField(multiline=False, font_size='18sp', hint_text='description')
        input_data_component_panel.add_widget(self.description_input)
        input_data_component_panel.add_widget(self.create_priority_input_data_panel())
        input_data_component_panel.add_widget(self._create_buttons_component_panel())

        return input_data_component_panel
    
    def create_priority_input_data_panel(self):
        self.priority_input_panel = GridLayout(cols=2, spacing=20)
        self.priority_input_panel.size_hint = (None, None)
        #assuming there are three priority levels : low,medium high

        priority_options = ["Low", "Medium", "High"]
        for priority in priority_options:
            checkbox = CheckBox(group='priority', active=False, color=(0, 0, 0, 1))
            checkbox_label = Label(text=priority, color=(0, 0, 0, 1))
            self.priority_input_panel.add_widget(checkbox)
            self.priority_input_panel.add_widget(checkbox_label)
        return self.priority_input_panel
    
    def _get_selected_priority(self):
        for index, child in enumerate(self.priority_input_panel.children):
            if isinstance(child,CheckBox)and child.active:
                label_index = index -1
                if label_index < len(self.priority_input_panel.children):
                    label = self.priority_input_panel.children[label_index]
                    priority_text = label.text.lower()
                    return Priority[priority_text.upper()]
        return None       
    
    def _create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self._create_department_selector())
        content_panel.add_widget(self._create_empoyee_selector())
        content_panel.add_widget(self.create_table(self.departament_list[0].employee_list[0]))

        return content_panel
    
    def _create_buttons_component_panel(self):
        button_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(text='Add', size_hint=(None, None), size=(100, 40), background_color=(0,1,1,1))
        add_button.bind(on_release=self._add_task)
        
        update_button = Button(text='Update', size_hint=(None, None), size=(100, 40), background_color=(0,1,1,1))
        update_button.bind(on_release=self._update_task)
        
        delete_button = Button(text='Delete', size_hint=(None, None), size=(100, 40), background_color=(0,1,1,1))
        delete_button.bind(on_release=self._delete_task)

        button_component_panel.add_widget(add_button)
        button_component_panel.add_widget(update_button)
        button_component_panel.add_widget(delete_button)
        return button_component_panel
    
    def _create_department_selector(self):
        button = Button(text='Select a department', size_hint=(1, 0.1), background_color=(0,1,1,1))
        button.bind(on_relase = self.show_department_list)
        return button
    
    def show_department_list(self, button):
        menu_items = []
        department_list = self.departament_list
        #create menu items for each department in the departement list
        for department in department_list:
            menu_items.append({"viewclass": "OneLineListItem", "text": department.name,
                               "on_relase": lambda department=department: self.update_employee_list(department)})

            self.dropdown = MDDropdownMenu(
                caller = button,
                items= menu_items,
                width_mult=5,
                max_height=dp(150),
            )
            self.dropdown.open()

    def _create_empoyee_selector(self):
        button = Button(text='Select an employee', size_hint=(1, 0.1), background_color=(0,1,1,1))
        button.bind(on_release=self.show_employee_list)
        return button
    
    def show_employee_list(self, button):
        menu_items =[]
        department_list = self .departament_list
        employee_list = department_list[0].employee_list

        for employee in employee_list:
            menu_items.append({"viewclass": "OneLineListItem", "text": employee.name,
                               "on_relase": lambda e=employee: self._update_data_table(e)})
            
        self.dropdown = MDDropdownMenu(
            caller = button,
            items= menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def create_table(self, employee):
        table_row_data = []
        task_list = employee.task_list

        for task in task_list:
            table_row_data.append((task.name, task.description, task.priority.value))

        self.task_table = MDDataTable(
            pos_hint={'centre_x': 0.5, 'centre_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num = 10,
            column_data=[
                ("Name", dp(40)),
                ("Description", dp(50)),
                ("Priority", dp(40))

            ],
            row_data=table_row_data
        )
        self.task_table.bind(on_check_press = self._checked)
        self.task_table. bind(on_row_press = self._on_row_press)
        return self.task_table
    

    def _checked(self, instance_table, current_row):
        self.selected_task =Task(
            current_row[0], current_row[1], Priority[current_row[2]]
        )

        self.name_input.text = str(self.selected_task.name)
        self.description_input.text = str(self.selected_task.description)
        if self.selected_task.priority == Priority.HIGH:
            print("High")
            self.priority_input_panel.children[5].active = True
        elif self.selected_task.priority == Priority.MIDIUM:
            print("Medium")
            self.priority_input_panel.children[3].active = True
        elif self.selected_task.priority == Priority.LOW:
            self.priority_input_panel.children[1].active = True

    def _on_row_press(self, instance, row):
        self.selected_row = int(row.index / len(instance.column_data))

    def _clear_input_text_fields(self):
        self.name_input.text = ""
        self.description_input.text = ""
        self.selected_row = -1

    def _is_data_valid(self, task_data):
        return(
            task_data[0] != ""
            and task_data[1] != ""
            and task_data[2] != ""
        )
    
    def _add_task(self, instance):
        name = self.name_input.text
        description = self.description_input.text
        priority = self._get_selected_priority()

        task_data = [name, description, priority]

        if self._is_data_valid(task_data):
            self.task_manager_controller.add_task(self.employee, task_data)

            self.task_table.row_data.append([name, description, priority.name])

            self._clear_input_text_fields()

        else:
            self._show_error_popup("Invalid data", "Provide mandatory data to add a new Task")

    def _update_task(self, instance):
        if self.selected_row != -1:
            name = self.name_input.text
            description = self.description_input.text
            priority = self._get_selected_priority()

            task_data = [name, description, priority]

            if self._is_data_valid(task_data):
                task_to_remuve = self.task_table.row_data[self.selected_row]

                del self.task_table.row_data[self.selected_row]
                self.task_manager_controller.update_task(task_to_remuve[0], task_data, self.employee)

                self.task_table.row_data.append([name, description, priority.name])

                self._clear_input_text_fields()
            else:
                self._show_error_popup("Invalid data", "Provide mandatory data to update the Task")
        else:
            self._show_error_popup("Invalid data", "Salect any row to update")

    def _delete_task(self, instance):
        if self.selected_row != -1:
            task_to_remove = self.task_table.row_data[self.selected_row]

            del self.task_table.row_data[self.selected_row]
            self.task_manager_controller.delete_task(self.employee, task_to_remove[0])

            self._clear_input_text_fields()
        else:
            self._show_error_popup("Invalid data", "Select any row to delete")


    def _show_error_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(None, None),
            size=(400,200)
        )
        popup.open()

    
    def update_employee_list(self, department):
        self.department = department
        menu_items = []
        employees = department.employee_list
        for employee in employees:
            menu_items.append({"viewclass": "OneLineItem", "text":employee.name,
                               "on_release": lambda e=employee: self.update_task_table(e)})
           
                

        self.show_employee_list(None)
        self.employee_selector.items = menu_items
        self.employee_selector.dissmiss()
        self._update_data_table(employee[0])

    def _update_data_table(self, employee):
        self.employee = employee
        table_row_data = []
        tasks = employee.task_list
        for task in tasks:
            table_row_data.append(
                (task.name, task.description, task.priority.valu)
            )

        self.task_table.row_data = table_row_data
                                
                                


        

    



        

 
