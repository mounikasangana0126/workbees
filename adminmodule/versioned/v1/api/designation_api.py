from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.designation_model import DesignationModel  
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer  
from utils.helper.permission import SuperuserPermission  

class DesignationGetAPI(APIView):
    """Designation Get API View to fetch and create designations."""
    
    permission_classes = [SuperuserPermission]  
    
    def get(self, request, *args, **kwargs):
        """Handle GET request and return Response with all designations."""
        queryset = DesignationModel.objects.all()  
        serializer = DesignationSerializer(queryset, many=True) 
        
        return Response(
            {
                'message': 'Designations fetched successfully',
                'data': serializer.data if serializer.data else []
            },
            status=status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests and save the data in Designation model."""
        serializer = DesignationSerializer(data=request.data) 
        
        if serializer.is_valid():  
            serializer.save()  
            return Response({
                'message': 'Designation created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class DesignationGetDetailAPI(APIView):
    """Designation Detail API View to handle individual designation records."""
    
    permission_classes = [SuperuserPermission]  
    
    def get(self, request, id):
        """Retrieve a specific designation by ID."""
        try:
            designation = DesignationModel.objects.get(id=id)  
            serializer = DesignationSerializer(designation)  
            
            return Response({
                'message': 'Designation fetched successfully',
                'data': serializer.data if serializer.data else []
            }, status=status.HTTP_200_OK)
        
        except DesignationModel.DoesNotExist:
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        """Handle PATCH requests and update the data in Designation model."""
        try:
            queryset = DesignationModel.objects.get(id=id)  
        except DesignationModel.DoesNotExist:
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        
    
        serializer = DesignationSerializer(queryset, data=request.data, partial=True)
        
        if serializer.is_valid(): 
            serializer.save()  
            return Response({
                'message': 'Designation updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Handle DELETE requests and delete data from Designation model."""
        try:
            queryset = DesignationModel.objects.get(id=id)  
        except DesignationModel.DoesNotExist:
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        
        queryset.delete()
        return Response({
            'message': 'Designation deleted successfully',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
