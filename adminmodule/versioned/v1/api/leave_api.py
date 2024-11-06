"""Leave api."""

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave
from adminmodule.versioned.v1.serializer.leave_serializer import GetLeaveSerializer,PostLeaveSerializer
from adminmodule.models.employee_model import Employees
from rest_framework.permissions import IsAuthenticated
class LeaveAPI(APIView):
    """Leave API"""
    permission_class=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        """Handle get request to get all leaves."""
        employee = Employees.objects.get(user__name=request.user)
        leave=Leave.objects.filter(employee=employee)
        if not leave.exists():
            return Response(
                {
                    "message":"Leave does not exist",
                    "data":[]
                },
                status=status.HTTP_200_OK
            )
        serializer = GetLeaveSerializer(leave, many=True)
        return Response(
            {
                'message':'Leaves fetched successfully',
                'data':serializer.data
            },
            status=status.HTTP_200_OK
        )
    def post(self,request,*args,**kwargs):
        """ Handle post request to add leave record of an employee."""

        employee = Employees.objects.get(user__name = request.user)
        serializer=PostLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee = employee)
            return Response(
                {
                    'message':'leave request sent successfully',
                    'data':serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message':serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
            )

class LeaveDetailAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        """ Handle get request to get a particular leave record of an employee"""
        
        try:
            snippet=Leave.objects.get(id=id,employee=request.user.employees)
        except:
            return Response(
                {
                    'message':'Leave not found',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer=GetLeaveSerializer(snippet)
        return Response(
            {
                'message':'leave record fetched successfully',
                'data':serializer.data
            },
            status=status.HTTP_200_OK
        )
    def put(self,request,id):
        try:
            snippet=Leave.objects.get(id=id,employee=request.user.employees)
        except:
            return Response(
                {
                    'message':'leave record not found',
                    'data':[]
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer=GetLeaveSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':'Data updated sucessfully',
                    'data':serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'message':'Provided data was invalid.',
            },
            status=status.HTTP_400_BAD_REQUEST
        )

