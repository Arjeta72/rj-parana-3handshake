from model import Employee, Task, Department
import psycopg2

class EmployeeManagerController:

    def add_employee(self, department, employee_data):
        #step1 get the list of the employee from the  departament 
        employees = department.employee_list
        #create new employye object with the provided data
        new_employee = Employee(employee_data[0], employee_data[1], employee_data[2], employee_data[3], [])
        employees.append(new_employee)
        department.employees = employees 

    def deleted_employee(self, department, employee_data):
        #retrive the employee list from the departament
        employee_list = department.employee_list

        for employee in employee_list:
            if employee.name == employee_data[0]:
                employee_list.remove(employee)

    def update_employee(self, old_employee_data, new_employee_data, departament):
        employee_list = departament.employee_list

        for employee in employee_list:
            if employee.name ==old_employee_data[0]:
                #Update the employee's data
                employee.name = new_employee_data[0]
                employee.address = new_employee_data[1]
                employee.email = new_employee_data[2]
                employee.phone_nr = new_employee_data[3]

                break

class EmployeeDatabaseManager:
    def __init__(self, dbname, use, password, host, port):
        self.conn = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        #Create departments table if it dosen't exist
        create_department_table_query= "CREATE TABLE IF NOT EXISTS departments ( id SERIAL PRIMARY KEY, name VARCHAR(20))"
        self.cursor.execute(create_department_table_query)
        self.conn.commit()

        create_employee_table_query = "CREATE TABLE IF NOT EXISTS employees ( id SERIAL PRIMARY KEY, name VARCHAR(20), address VARCHAR(30), email VARCHAR(30), phone VARCHAR, dep_fk INT REFERENCES departments(id))"
        self.cursor.execute(create_employee_table_query)
        self.conn.commit()

        create_tasks_table_query = "CREATE TABLE IF NOT EXISTS tasks ( id SERIAL PRIMARY KEY, name VARCHAR(50), dscription VARCHAR(50), priority VARCHAR(30), emp_fk INT REFERENCES employees(id))"
        self.cursor.execute(create_tasks_table_query)
        self.conn.commit()

    def create_department(self, department_name):
        sql = f"SELECT id FROM departments WERE name = '{department_name}'"
        self.cursor.execute(sql)
        dep_result = self.cursor.fetchone()

        if dep_result:
            print("Department already exists")
        else:
            query = f"INSERT INTO departments (name) VALUES ('{department_name}')"
            self.cursor.execute(query)
            self.conn.commit()
            print("Department created successfully")

    def create_departments(self):
        self.create_department("Sales")
        self.create_department("Marketing")
        self.create_department("Development")

    def get_department_list(self):
        self.create_table()
        self.create_departments()
        sql = "SELECT * FROM departments"
        self.cursor.execute()
        depatments_names = self.cursor.fetchall()
        department_list = []
        for row in depatments_names:
            employee_list = self.get_data_from_table(row[1])
            department_list.append(Department(row[1], employee_list))
            return department_list
        
# CREATE---- INSERT
# READ ------SELECT
# UPDATE ---- UPDATE
# DELETE ---- DELETE
        
                
    def insert_data_for_employee(self, department, data):
        sql = f"SELECT id FROM departments WHERE name = '{department.name}'"
        self.cursor.execute(sql)
        dep_result = self.cursor.fetchone()
        if dep_result:
            dep_id = dep_result[0]
            query = f"INSERT INTO public.employees (name, address, email, phone, dep_fk) VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{dep_id}')"
            self.cursor.execute(query)
            self.conn.commit()
        else:
            print("Department not found")

    def delete_data_for_employee(self, condition):
        # Delete data from the employees table based on condition
        query = f"DELETE FROM employees WHERE name = '{condition[0]}'"
        self.cursor.execute(query)
        self.conn.commit()

    def update_data_for_employee(self, department, condition, data):
        sql = f"SELECT id FROM departments WHERE name = '{department.name}'"
        self.cursor.execute(sql)
        dep_result = self.cursor.fetchone()
        if dep_result:
            dep_id = dep_result[0]
            query = f"UPDATE public.employees SET name = '{data[0]}', address = '{data[1]}', email = '{data[2]}', phone = '{data[3]}', dep_fk = '{dep_id}' WHERE name = '{condition[0]}'"
            self.cursor.execute(query)
            self.conn.commit()
        else:
            print("Department not found")

    def insert_data_for_table(self, department):
        sql = f"SELECT id FROM departments WHERE name = '{department}'"
        self.cursor.execute(sql)
        dep_result = self.cursor.fetchone()
        dep_id = dep_result[0]
        sql = f"SELECT * FROM employees WHERE dep_fk = '{dep_id}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        employee_list = []
        for row in data:
            employee_list.append(Employee(row[1], row[2], row[3], row[4], []))
        self.conn.commit()
        return employee_list


class TaskManagerController:
    def add_employee(self, employee, task_data):
        task = employee.task_list
        new_task = Task(task_data[0], task_data[1], task_data[2], task_data[3], [])
        task.append(new_task)
        employee.task = task 

    def deleted_employee(self, employee, task_name):
            task_list = employee.task_list

            for task in task_list:
                if task.name == task_name[0]:
                    task_list.remove(task)
                    employee.task_list = task_list
                    break
'{data[0]}'
    def update_task(self, old_task_name, new_task_data, employee):
        task_list = employee.task_list

        for task in task_list:
            if task.name == old_task_name:
                task.name = new_task_data[0]
                task.description = new_task_data[1]
                task.priority = new_task_data[2]     