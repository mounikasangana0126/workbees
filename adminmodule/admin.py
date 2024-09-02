from django.contrib import admin

from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.department_model import DepartmentModel,ParentModel
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.task_model import Task
from adminmodule.models.break_entry_model import BreakEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.shift_timings_model import WorkShiftsModel,UserShiftTimingsModel

# Register your models here.

admin.site.register(DepartmentModel)
admin.site.register(ParentModel)
admin.site.register(DesignationModel)
admin.site.register(User)
admin.site.register(TimeEntry)
admin.site.register(Task)
admin.site.register(BreakEntry)
admin.site.register(Employees)
admin.site.register(WorkShiftsModel)
admin.site.register(UserShiftTimingsModel)