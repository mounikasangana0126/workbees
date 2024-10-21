from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class TimeEntryCheckInAPI(APIView):
    """ List of all time entries, and post a new time entry api."""
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Handle Get request and return response.."""
        user = User.objects.get(id = request.user.id)
        if not user:
            return Response(
                {
                    'message':'user not found',
                    'data':[]
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        employee = Employees.objects.filter(user = user).first()
        if not employee:
            return Response(
                {
                    'message':'Employee is not created for this user..',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        timeentries = TimeEntry.objects.filter(employee = employee)
        if not timeentries.exists():
            return Response(
                {
                    'message':'No time entry is created by these employee',
                    'data':[]
                },
                status=status.HTTP_204_NO_CONTENT
            )
        serializer = TimeEntrySerializer(timeentries, many= True)
        return Response(
            {
                'message':'Time entries of an employee fetched successfully',
                'data':serializer.data
            },
            status=status.HTTP_200_OK
        )

    
    def post(self, request):
        """ Handle Post request for create a new Time entry and return Response"""
        
        timee = timezone.now()
        timee_date = timee.date()
        print(timee)
        user = User.objects.get(id = request.user.id)
        if not user:
            return Response(
                {
                    'message':'user not found',
                    'data':[]
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        employee = Employees.objects.filter(user = user).first()
        if not employee:
            return Response(
                {
                    'message':'Employee is not created for this user..',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            timeentry = TimeEntry.objects.get(employee=employee, clock_in__date=timee_date)
            if timeentry:
                return Response(
                {
                    'message':'Clock_in has already created for this employee',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
                
        except TimeEntry.DoesNotExist:
            timeentry = None
        data= request.data
        data['employee']=employee.id
        data['clock_in']=timee
        data['date'] = timee_date 
        serializer = TimeEntrySerializer(data = data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'Clock_in created for today',
                    'data':serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message':serializer.errors,
                'data':[]
            },
            status=status.HTTP_400_BAD_REQUEST
        )


        
class TimeEntryCheckOutAPI(APIView):
    """ To save clock_out time..."""
    
    def post(self, request):
        """ Handle Post request and save request data."""
        employee = Employees.objects.get(user = request.user.id)
        timee = timezone.now()
        timee_date = timee.date()
        try:
            timeentry = TimeEntry.objects.get(employee = employee, clock_in__date = timee_date)
        except TimeEntry.DoesNotExist():
            return Response(
                {
                    'message':'You have not clock_in today.',
                    'data':[] 
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        data['clock_in'] = timeentry.clock_in
        data['clock_out'] = timee
        data['is_completed'] = True
        data['employee'] = employee.id
        # breaks = BreakEntry.objects.filter(time_entry = timeentry)
        serializer = TimeEntrySerializer(timeentry, data=data, partial =True)
        # break_serializer = BreakEntrySerializer(breaks, many =True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':' Clock_out time saved successfully..',
                    'data':serializer.data
                    # 'breaks':break_serializer.data
                },
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {
                'message':serializer.errors,
                'data':[]
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
        


class TimeEntryCheckInCheckOutDetailsAPI(APIView):
    """ To get or update time entry"""
    
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        """ Handle Get request and return Response.."""
        try:
            timeentry = TimeEntry.objects.get(id = id)
        except TimeEntry.DoesNotExist:
            return Response(
                {
                    'message':'Time Entry not found.',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TimeEntrySerializer(timeentry)
        return Response(
            {
                'message':'Time entry or clock_in fetech successfully',
                'data':serializer.data
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """ Handle put request and return response.."""
        timee = timezone.now()
        try:
            timeentry = TimeEntry.objects.get(id = id)
        except TimeEntry.DoesNotExist:
            return Response(
                {
                    'message':'Time entry or clock_in not found..',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.get(id = request.user.id)
        print(request.user.id)
        employee = Employees.objects.get(user = user)
        data = request.data
        data['clock_in'] = timeentry.clock_in
        data['clock_out'] = timee
        data['employee'] = employee.id
        serializer = TimeEntrySerializer(timeentry, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'Clock_out time saved',
                    'data':serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                'message':serializer.errors,
                'data':[]
            },
            status = status.HTTP_400_BAD_REQUEST
        )
