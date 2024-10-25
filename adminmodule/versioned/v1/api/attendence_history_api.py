from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import date, timedelta
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.leave_model import Leave
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from django.conf import settings


class AttendanceHistoryGetAPI(APIView):
    """Retrieve past 7 days of attendance history for an employee."""
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request and return past 7 days attendance response."""

        attendance_history = []
        employee = Employees.objects.get(user=request.user.id)
        holiday_dates = [date.fromisoformat(holiday) for holiday in settings.HOLIDAYS]

        for day_offset in range(7):
            current_date = date.today() - timedelta(days=day_offset)
            day_name = current_date.strftime('%A')
            weekday_number = current_date.weekday()
            
            day_entry = {
                "date": current_date,
                "day_name": day_name,
                "status": None,
                "clock_in": None,
                "clock_out": None,
                "total_work_time": None,
            }

            time_entry = TimeEntry.objects.filter(employee=employee, clock_in__date=current_date).first()
            leave_entry = Leave.objects.filter(employee=employee, start_date__lte=current_date, end_date__gte=current_date).first()
            
            if time_entry:
                serializer = TimeEntrySerializer(time_entry)
                entry_data = serializer.data
                day_entry["status"] = "Present"
                day_entry["clock_in"] = entry_data.get("clock_in")
                day_entry["clock_out"] = entry_data.get("clock_out")
                day_entry["total_work_time"] = entry_data.get("total_work_time")
            elif weekday_number == 6:
                day_entry["status"] = "Holiday - Sunday"
            elif current_date in holiday_dates:
                day_entry["status"] = "Holiday"
            elif leave_entry: 
                day_entry["status"] = "Leave"
            else:
                day_entry["status"] = "Absent"
            
            attendance_history.append(day_entry)

        return Response(
            {
                'message': 'Last 7 days attendance history of an employee.',
                'data': attendance_history
            },
            status=status.HTTP_200_OK
        )
