from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer
from adminmodule.models.employee_model import Employees
class LeaveAPI(APIView):
    def get(self,request):
        quary=Leave.objects.all()
        serializer=LeaveSerializer(quary,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        try:
            employee_id=Employees.objects.get(id=request.data.get('employee'))
            print(employee_id)
        except:
            return Response({'message':'Employee not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        try:
            snippet=Leave.objects.get(id=request.data.get('employee'))
        except:
            return Response({'message':'Employee not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(snippet)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
