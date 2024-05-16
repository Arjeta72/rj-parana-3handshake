from dataprovider import DataProvider

class DepartmentEmployeeManagmentApp:
    def start(self):

        self.department_list = []
        self.data_provider = DataProvider()
        self.department_list = self.data_provider.department_list

        #Loop through each departmen
        for department in self.department_list:
            print("-------------------------------------------")
            print("List of employees in the " + department.name +"department")
            print("=================================-----------")

            #Loop through each employee in departmen
            for employee in department.employee_list:
                print(employee.name + "," + employee.address + "," + employee.email + "," + employee.phone_nr)
                print("---------------------------------------")

                for task in employee.task_list:
                    print(task.name + "," + task. description + "," + task.priority.value)
                    print("--------------------------------------")

#create on instance of the application and start it
employee_managment_app = DepartmentEmployeeManagmentApp()
employee_managment_app.start()






        