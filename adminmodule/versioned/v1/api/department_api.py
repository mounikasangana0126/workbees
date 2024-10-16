from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.department_model import DepartmentModel, ParentModel
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer, ParentSerializer
from rest_framework import status
from utils.helper.permission import SuperuserPermission

class ParentGetAPI(APIView):
    """Parent Get API View."""
    permission_classes=[SuperuserPermission]
    
    def get(self, request):
        """Handle GET requests and return response."""
        queryset = ParentModel.objects.all()
        serializer = ParentSerializer(queryset, many=True)
        return Response(
            {
                "message": "Parent fetched successfully.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class DepartmentGetAPI(APIView):
    """Department Get API View."""
    permission_classes=[SuperuserPermission]

    def get(self, request, *args, **kwargs):
        """Handle GET requests and return response."""
        queryset = DepartmentModel.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response({
            "messege":"Departments fetched successfully",
            "data": serializer.data
            },
            status= status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests and save the request data."""
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentGetDetailAPI(APIView):
    """Department Detail API View."""
    permission_classes=[SuperuserPermission]
    def get(self, request, id):
        """Retrieve a specific department by ID."""
        try:
            department = DepartmentModel.objects.get(id=id)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DepartmentModel.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        """Handle PATCH requests and update the department."""
        try:
            queryset = DepartmentModel.objects.get(pk=id)
        except DepartmentModel.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Handle DELETE requests and delete data from department model."""
        
        try:
            queryset = DepartmentModel.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        queryset.delete()
        return Response({"message":"Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
