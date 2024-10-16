""" Admin Model"""
from django.contrib import admin
from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.department_model import DepartmentModel,ParentModel
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.task_model import Task
from adminmodule.models.break_entry_model import BreakEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.shift_timings_model import WorkShiftsModel
from adminmodule.models.leave_model import Leave
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(DepartmentModel)
class DepartmentModelAdmin(ImportExportModelAdmin):
    """DepartmentModelAdmin."""
    list_display = ["id", "dept_name", "dept_code","parent", "dept_is_enabled"]
    list_filter = ["id","dept_name"]
    date_hierarchy = "created_at"
    
@admin.register(ParentModel)
class ParentModelAdmin(ImportExportModelAdmin):
    """ ParentModelAdmin.."""
    list_display = ["id", "parent_dept"]
    list_filter = ["id", "parent_dept"]
    date_hierarchy = "created_at"
@admin.register(DesignationModel)
class DesignationModelAdmin(ImportExportModelAdmin):
    """ DesignationModelAdmin. """
    list_display = ["id", "department","designation_name", "designation_is_active"]
    list_filter = ["id", "designation_name", "department"]
    date_hierarchy = "created_at"
@admin.register(TimeEntry)  
class TimeEntryModelAdmin(ImportExportModelAdmin):
    """ TimeEntryModelAdmin.."""
    list_display = ["id", "employee", "clock_in","clock_out", "is_completed"]
    list_filter = ["id", "employee","clock_in"]
    date_hierarchy = "created_at"
@admin.register(Task)  
class TaskModelAdmin(ImportExportModelAdmin):
    """ TaskModelAdmin.."""
    list_display = ["id","title", "department", "description","start_date"]
    list_filter = ["id", "priority","start_date"]
    date_hierarchy = "created_at"
@admin.register(BreakEntry)   
class BreakEntryModelAdmin(ImportExportModelAdmin):
    """ BreakEntryModelAdmin.."""
    list_display = ["id", "time_entry", "break_start", "break_end"]
    list_filter = ["id", "break_start", "time_entry"]
    date_hierarchy = "created_at"
@admin.register(Employees)  
class EmployeesModelAdmin(ImportExportModelAdmin):
    """  EmployeesModelAdmin.. """
    list_display = ["id", "employee_id", "user", "designation"]
    list_filter = ["id", "user"]
    date_hierarchy = "created_at"
@admin.register(WorkShiftsModel) 
class WorkShiftModelAdmin(ImportExportModelAdmin):
    """ WorkShiftModelAdmin."""
    list_display = ["id", "shift_name", "shift_start_time","shift_end_time"]
    list_filter = ["id", "shift_name"]
    date_hierarchy = "created_at"
@admin.register(Leave)  
class LeaveModelAdmin(ImportExportModelAdmin):
    """ LeaveModelAdmin.."""
    list_display = ["id","employee", "leave_type","start_date","end_date"]
    list_filter = ["id", "employee","start_date"]
    date_hierarchy = "created_at"
    

@admin.register(User)
class UserAdmin(BaseUserAdmin):  # pylint: disable=too-few-public-methods
    """Admin interface for users."""

    list_display = ("username", "name", "created_at", "is_active", "phone_number","is_admin")
    list_filter = (
        "is_superuser",
    )
    search_fields = ("phone_number", "username")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                    "name",
                    "phone_number",
                    "email",
                    "is_admin",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "name",
                    "phone_number",
                    "email",
                    "is_active",
                    "is_admin",
                ),
            },
        ),
    )


