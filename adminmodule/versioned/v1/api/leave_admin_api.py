from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer
from adminmodule.models.employee_model import Employees
from rest_framework.permissions import IsAuthenticated
from utils.helper.permission import SuperuserPermission

class LeaveAdminAPI(APIView):
    permission_classes=[SuperuserPermission]

    def get(self,request):
        query=Leave.objects.all()
        serializer=LeaveSerializer(query,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        try:
            employee_id=Employees.objects.filter(employee__user=request.user).first()
            print(employee_id)
        except:
            return Response({'message':'Employee not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaveAdminDetailAPI(APIView):
    permission_classes=[SuperuserPermission]

    def get(self,request,id):
        try:
            snippet=Leave.objects.get(id=id)
        except:
            return Response({'message':'Leave not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(snippet)
        emp_id=serializer.data['employee']
        snippet2=Employees.objects.get(id=emp_id)
        snippet2_data=EmployeeSerializer(snippet2)
        print(snippet2_data)
        self.check_object_permissions(request,snippet2_data.data)
        return Response(serializer.data)

    def put(self,request,id):
        try:
            snippet=Leave.objects.get(id=id)
        except:
            return Response({'message':'Employee not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(snippet)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
