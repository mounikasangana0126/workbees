from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.task_model_serializer import TaskModelSerializer
from adminmodule.models.task_model import Task

class TaskModelGetAPI(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Task.objects.all()
        serializer=TaskModelSerializer(queryset,many=True)
        return Response({
            "message":"Data fatched Successfully",
            "data":serializer.data
        },
        status=status.HTTP_200_OK
        )
    def post(self,request,*args,**kwargs):
        serializer=TaskModelSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,format=None):
        queryset=Task.objects.get(pk=id)
        serializer=TaskModelSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    