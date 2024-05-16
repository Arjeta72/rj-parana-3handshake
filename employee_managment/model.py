
class User:
    def __init__(self, username, password, user_role):
        self._username = username
        self._password = password
        self._user_role = user_role

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def user_role(self):
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        self._user_role = user_role



class Department:
    def __init__(self, name, employee_list):
        self.__name = name
        self.__employee_list = employee_list 

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def employee_list(self):
        return self.__employee_list
    
    @employee_list.setter
    def employee_list(self, employee_list):
        self.__employee_list = employee_list

class Employee:
    def __init__(self, name, address, email, phone_nr, task_list):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone_nr = phone_nr
        self.__task_list = task_list

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone_nr(self):
        return self.__phone_nr
    
    @phone_nr.setter
    def phone_nr(self, phone_nr):
        self.__phone_nr = phone_nr

    @property
    def task_list(self):
        return self.__task_list
    
    @task_list.setter
    def task_list(self, task_list):
        self.__task_list = task_list

class Task:
    def __init__(self, name, description, priority):
        self.__name = name
        self.__description = description
        self.__priority = priority

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, priorty):
        self.__priority = priorty

