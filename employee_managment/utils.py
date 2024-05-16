from enums import UserRole, UserFeatures
from admin_view import EmployeeManagerContentPanel, TaskManagerContentPanel

class AuthorizationService:

    def get_user_feature_by_user_role(self, user_role):
        if user_role == UserRole.ADMIN:
            return [UserFeatures.EMPLOYEES, UserFeatures.DEPARTMENTS, UserFeatures.TASK, UserFeatures.PAYROLLS, UserFeatures.ACCOUNTS, UserFeatures.HOLIDAYS,UserFeatures.SIGN_OUT]
        elif user_role == UserRole.EMPLOYEE:
            return [UserFeatures.CUSTOMERS,UserFeatures.TASK, UserFeatures.SALES, UserFeatures.CALENDAR,UserFeatures.SIGN_OUT]
        elif user_role == UserRole.INTERN:
            return [UserFeatures.CALENDAR, UserFeatures.TASK, UserFeatures.SIGN_OUT]
        elif user_role is None:
            raise RuntimeError("The provided user role " + user_role + " is not supported")

 
class UserFeatureLabelResolver:
    
    user_feature_label_dict = None

    @staticmethod
    def get_user_feature_label(user_feature):
        return UserFeatureLabelResolver.__get_user_feature_label_dict().get(user_feature)
    
    @staticmethod
    def __get_user_feature_label_dict():
        if UserFeatureLabelResolver.user_feature_label_dict is None:
            UserFeatureLabelResolver.user_feature_label_dict = {
                UserFeatures.EMPLOYEES: "Employees",
                UserFeatures.DEPARTMENTS: "Departments",
                UserFeatures.PAYROLLS: "Payrolls",
                UserFeatures.HOLIDAYS: "Holidays",
                UserFeatures.ACCOUNTS: "Accounts",
                UserFeatures.CUSTOMERS: "Customers",
                UserFeatures.SALES: "Sales",
                UserFeatures.CALENDAR: "Calendar",
                UserFeatures.TASK: "Task",
                UserFeatures.SIGN_OUT: "Sign out",
            }
        
        return UserFeatureLabelResolver.user_feature_label_dict
    

# Create UserFeatureContentPanelResolver
class UserFeatureContentPanelResolver:
    user_feature_content_panel_map = None
    
    @staticmethod
    def get_user_feature_panel(user_feature):
        return UserFeatureContentPanelResolver.get_user_feature_content_panel_map().get(user_feature)
    
    @staticmethod
    def get_user_feature_content_panel_map():
        if UserFeatureContentPanelResolver.user_feature_content_panel_map is None:
            UserFeatureContentPanelResolver.user_feature_content_panel_map = {
                "Departments": "DepartmentManagerContentPanel()" ,
                "Employees": EmployeeManagerContentPanel(),
                "Task": TaskManagerContentPanel(),
                # "Payrolls": PayrollsManagerContentPanel(),
                # "Holidays": HolidaysManagerContentPanel(),
                # "Accounts": AccountsManagerContentPanel(),
                # "Reports": ReportsManagerContentPanel(),
                # "Customers": CostumersManagerContentPanel(),
                # "Sales": SalesManagerContentPanel(),
                # "Calendar": CalendarManagerContentPanel(),
                # "My Tasks": MyTasksManagerContentPanel()
            }
        return UserFeatureContentPanelResolver.user_feature_content_panel_map
