from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
from adminmodule.models.break_entry_model import BreakEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.time_entry_model import TimeEntry
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class BreakAPI(APIView):
    """ List all break start and start end."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request to fetch all the break entry records of an employee."""
        
        timee = timezone.now()
        timee_date = timee.date()
        employee = Employees.objects.get(user = request.user.id)
        try:
            timeentry = TimeEntry.objects.get(employee = employee, clock_in__date = timee_date )
        except TimeEntry.DoesNotExist:
            return Response(
                {
                    'message':' You have not clock_in yet..',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        snippet = BreakEntry.objects.filter(time_entry = timeentry)
        if not snippet.exists():
            return Response(
                {
                    'message':'There is no breaks yet..',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        serializer = BreakEntrySerializer(snippet, many=True)
        return Response(
            {
                'message':'All breaks on today fetched..',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """Handle POST request to add break entry record to a time entry of an employee."""
        
        timee = timezone.now()
        timee_date = timee.date()
        employee = Employees.objects.get(user = request.user.id)
        try:
            timeentry = TimeEntry.objects.get(employee = employee, clock_in__date = timee_date)
        except TimeEntry.DoesNotExist:
            return Response(
                {
                    'message':' You have not clock_in yet..',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        data = request.data
        data['break_start'] = timee
        data['time_entry'] = timeentry.id
        serializer = BreakEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'Break_start created successfully',
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

class BreakContinueAPI(APIView):
    """ Break continue to save break end time."""
    
    def post(self, request):
        """ Handle Post request to save break continue time.."""
        
        timee = timezone.now()
        timee_date = timee.date()
        employee = Employees.objects.get(user = request.user.id)
        try:
            timeentry = TimeEntry.objects.get(employee = employee, clock_in__date = timee_date)
        except TimeEntry.DoesNotExist:
            return Response(
                {
                    'message':' You have not clock_in yet..',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        try:
            breaks = BreakEntry.objects.filter(time_entry = timeentry).last()
        except BreakEntry.DoesNotExist():
            return Response(
                {
                    'message':'Break entry not found..',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        breaks.break_end=timee
        breaks.save()
        serializer = BreakEntrySerializer(breaks)
        return Response(
            {
                'message':'Break continue saved..',
                'data':serializer.data
            },
            status=status.HTTP_200_OK
        )





class BreakContinueDetailAPI(APIView):
    """ List a break.."""
    
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        """Handle GET request to fetch a particular break entry record."""
        
        try:
            snippet = BreakEntry.objects.get(id=id)
        except BreakEntry.DoesNotExist:
            return Response(
                {
                    'message':'Break Entry not found',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BreakEntrySerializer(snippet)
        return Response(
            {
                'message':'Break Entry fetched successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """Handle PUT request to update break entry record."""
        
        try:
            breaks = BreakEntry.objects.get(id = id)
        except BreakEntry.DoesNotExist():
            return Response(
                {
                    'message':'Break Entry not found',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BreakEntrySerializer(breaks, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'break entry updated..',
                    'data':serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'message':serializer.data,
                'data':[]
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        """Handle DELETE request to delete a particular break entry."""
        
        try:
            queryset = BreakEntry.objects.get(id=id)
        except BreakEntry.DoesNotExist:
            return Response(
                {
                    'message':' break entry not found',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset.delete()
        return Response(
            {
                'message':'break entry deleted',
                'data':[]
            },
            status=status.HTTP_204_NO_CONTENT
        )
