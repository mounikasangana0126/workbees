from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.color_serializer import colorSerializer
from rest_framework import status

class colourGetAPI(APIView):
    def green(self,request,id):
        queryset=Employees.objects.get(pk=id)
        serializer=colorSerializer(queryset.data)
        if serializer.emp_is_active==True:
            return Response({
                'colour':'green'

            })
    

