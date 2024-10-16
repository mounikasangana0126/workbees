from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.designation_model import DesignationModel
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer
from utils.helper.permission import SuperuserPermission


class DesignationGetAPI(APIView):
    permission_classes=[SuperuserPermission]
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
    

class DesignationGetDetailAPI(APIView):
    """Designation Detail API View."""
    permission_classes=[SuperuserPermission]
    def get(self, request, id):
        """Retrieve a specific department by ID."""
        try:
            designation = DesignationModel.objects.get(id=id)
            serializer = DesignationSerializer(designation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DepartmentModel.DoesNotExist:
            return Response({"error": "Designation not found"}, status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, id):
        """Handle DELETE requests and delete data from designation model."""
        
        try:
            queryset = DesignationModel.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        queryset.delete()
        return Response({"message":"designation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
