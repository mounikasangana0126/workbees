from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.designation_model import DesignationModel
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer


class DesignationGetAPI(APIView):
    
    def get(self,request, *args, **kwargs):
        """Handle GET request and return Response"""
        
        queryset = DesignationModel.objects.all()
        serializer = DesignationSerializer(queryset, many=True)
        return Response(
            {
                'messege': 'Designations fetched successfully',
                'data': serializer.data
            },
            status = status.HTTP_200_OK
        )
        
    def post(self, request):
        """ Handle POST requests and save the data in designation models"""
        
        serializer = DesignationSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        """Handle PATCH requests and update the data in designation models"""
        
        try:
            queryset = DesignationModel.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = DesignationSerializer(queryset, data = request.data , partial=True)
        
        if serializer. is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)