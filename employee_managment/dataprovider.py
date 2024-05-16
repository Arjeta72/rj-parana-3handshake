
from model import Department, Employee, Task, User
from enums import Priority, UserRole

class UserDataProvider:
    def __init__(self) -> None:
        self.__user_list = []
        self._create_user_list()

    def _create_user_list(self):
        user1 = User("1","1", UserRole.ADMIN)
        user2 = User("2","2", UserRole.EMPLOYEE)
        user3 = User("3","3",UserRole.INTERN)
        user4 = User("4","4",UserRole.EMPLOYEE)
        self.__user_list.append(user1)
        self.__user_list.append(user2)
        self.__user_list.append(user3)
        self.__user_list.append(user4)

    @property
    def user_list(self):
        return self.__user_list
                  
                            
class DataProvider:
    def __init__(self):
        self.__departments = []
        self._create_department_list()

    def _create_department_list(self):
        department1_employee_list = self._create_department1_employees()
        department1 = Department("Sales", department1_employee_list)

        department2_employee_list = self._create_department2_employees()
        department2 = Department("Management", department2_employee_list)

        department3_employee_list = self._create_department3_employees()
        department3 = Department("Development", department3_employee_list)

        self.__departments.append(department1)
        self.__departments.append(department2)
        self.__departments.append(department3)

    def _create_department1_employees(self):
        employee_list = []
        employee_list.append(Employee("Dep1 Empl1","Doro Street 1","dep1.empl1@example.com","+383111111",self.tasks_for_employee1()))
        employee_list.append(Employee("Dep1 Empl2","Doro Street 2","dep1.empl2@example.com","+383222222",self.tasks_for_employee2()))
        employee_list.append(Employee("Dep1 Empl3","Doro Street 3","dep1.empl3@example.com","+383333333",self.tasks_for_employee3()))

        return employee_list
    
    def _create_department2_employees(self):
        employee_list = []
        employee1 = Employee("Dep2 Empl1","Lorem Street 9","dep2.empl1@example.com","+383454545",self.tasks_for_employee1())
        employee2 = Employee("Dep2 Empl2","Lorem Street 8","dep2.empl2@example.com","+383444444",self.tasks_for_employee2())
        employee3 = Employee("Dep2 Empl3","Lorem Street 7","dep2.empl3@example.com","+383555555",self.tasks_for_employee3())
        employee4 = Employee("Dep2 Empl4","Lorem Street 6","dep2.empl3@example.com","+383333333",self.tasks_for_employee1())
        
        employee_list = [employee1, employee2, employee3, employee4]
        return employee_list
 
    def _create_department3_employees(self):
        employee_list = []
        employee1 = Employee("Dep3 Empl1","Ipsun Street 1","dep3.empl1@example.com","+383767676",self.tasks_for_employee1())
        employee2 = Employee("Dep3 Empl2","Ipsun Street 2","dep3.empl2@example.com","+383565656",self.tasks_for_employee2())
        employee3 = Employee("Dep3 Empl3","Ipsun Street 3","dep3.empl3@example.com","+383434343",self.tasks_for_employee3())
        employee4 = Employee("Dep3 Empl4","Ipsun Street 4","dep3.empl3@example.com","+383777777",self.tasks_for_employee3())
        
        employee_list = [employee1, employee2, employee3, employee4]
        return employee_list


    def tasks_for_employee1(self):
        tasks = [
            Task("Task1", "description1", Priority.LOW),
            Task("Task2", "description2", Priority.MEDIUM),
            Task("Task3", "description3", Priority.HIGH),
            Task("Task4", "description4", Priority.LOW)
        ]
        return tasks

    def tasks_for_employee2(self):
        tasks = [
            Task("Task5", "description5", Priority.LOW),
            Task("Task6", "description6", Priority.HIGH),
            Task("Task7", "description7", Priority.HIGH),
            Task("Task8", "description8", Priority.MEDIUM)
        ]
        return tasks

    def tasks_for_employee3(self):
        tasks = [
            Task("Task1", "description1", Priority.LOW),
            Task("Task2", "description2", Priority.HIGH),
            Task("Task3", "description3", Priority.HIGH),
            Task("Task4", "description4", Priority.MEDIUM)
        ]
        return tasks

    @property
    def department_list(self):
        return self.__departments
