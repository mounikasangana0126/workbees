from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.break_entry_model import BreakEntry
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from adminmodule.versioned.v1.serializer.check_in_check_out_serializer import EmployeeCheckInCheckOut 
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
class CheckInCheckOutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        """ Handle get request and response of all employees """
        data = Employees.objects.all()
        if not data.exists():
            return Response({
                'message':'No employees all timeentries and breakentries'
            }, status=status.HTTP_204_NO_CONTENT)
        serializer = EmployeeCheckInCheckOut(data, many=True)
        return Response({
            'message':'Fetched all employees - timeentries and breakentries..',
            'data':serializer.data
        }, status=status.HTTP_200_OK)

    def post(self,request):
        """ Handle post request and add new time entry to an employee"""
        serializer=TimeEntrySerializer(data=request.data)
        employee = Employees.objects.get(id = request.data.get('employee'))
        if serializer.is_valid():
            serializer.save(employee = employee)
            return Response({
                'message':'Clock_in added successfully.',
                'data':serializer.data},
                status=status.HTTP_201_CREATED) 
        return Response({
                'message':serializer.errors},
                status=status.HTTP_201_CREATED)

class CheckInCheckOutDetailsAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request,id):
        """Handle get request and response data"""
        try:
            queryset = Employees.objects.filter(id=id)
        except:
            return Response({'message':'Employee Timeentry details not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer =EmployeeCheckInCheckOut (queryset, many=True)
        return Response({
                        'message':' To retrive all timeentries of an employee',
                        'data':serializer.data
                        },
                        status=status.HTTP_200_OK
                    )

    def put(self,request,id):
        """ Handle put request by timeentry id to change details."""
        try:
            queryset = TimeEntry.objects.filter(id=id)
            if not queryset.exists():
                return Response({'message': 'Time entry not found for the given id and date'}, status=status.HTTP_404_NOT_FOUND)
            user_id=request.user.id
            user=User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(instance=queryset.first(), data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Time entry details changed successfully',
                'data':serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)