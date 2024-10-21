from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.department_model import DepartmentModel, ParentModel
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer, ParentSerializer
from rest_framework import status
from utils.helper.permission import SuperuserPermission

class ParentGetAPI(APIView):
    """Parent Get API View."""
    permission_classes = [SuperuserPermission]  # Superuser permissions required for access

    def get(self, request):
        """Handle GET requests to retrieve all parent records."""
        # Fetch all ParentModel records
        queryset = ParentModel.objects.all()
        
        # Serialize the queryset
        serializer = ParentSerializer(queryset, many=True)
        
        # Return the response with standardized format
        return Response(
            {
                "message": "Parent records fetched successfully.",
                "data": serializer.data if serializer.data else []
            },
            status=status.HTTP_200_OK
        )

class DepartmentGetAPI(APIView):
    """Department Get API View."""
    permission_classes = [SuperuserPermission]  # Superuser permissions required for access

    def get(self, request):
        """Handle GET requests to retrieve all department records."""
        # Fetch all DepartmentModel records
        queryset = DepartmentModel.objects.all()
        
        # Serialize the queryset
        serializer = DepartmentSerializer(queryset, many=True)
        
        # Return the response with standardized format
        return Response({
            "message": "Departments fetched successfully.",
            "data": serializer.data if serializer.data else []
            },
            status=status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests to create a new department."""
        # Initialize serializer with request data
        serializer = DepartmentSerializer(data=request.data)
        
        # Validate and save if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Department created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return validation errors with standardized format
        return Response({
            "message": "Department creation failed.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class DepartmentGetDetailAPI(APIView):
    """Department Detail API View."""
    permission_classes = [SuperuserPermission]  # Superuser permissions required for access

    def get(self, request, id):
        """Retrieve a specific department by its ID."""
        try:
            # Fetch the department by its ID
            department = DepartmentModel.objects.get(id=id)
            
            # Serialize the department data
            serializer = DepartmentSerializer(department)
            
            # Return the response with standardized format
            return Response({
                "message": "Department details fetched successfully.",
                "data": serializer.data if serializer.data else []
            }, status=status.HTTP_200_OK)
        except DepartmentModel.DoesNotExist:
            # Handle the case where the department is not found
            return Response({
                "message": "Department not found.",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        """Handle PATCH requests to partially update a department."""
        try:
            # Fetch the department by its ID
            queryset = DepartmentModel.objects.get(id=id)
        except DepartmentModel.DoesNotExist:
            # Handle the case where the department is not found
            return Response({
                "message": "Department not found.",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Initialize serializer with the existing department instance and new data
        serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
        
        # Validate and save if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Department updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        # Return validation errors if the data is invalid
        return Response({
            "message": "Department update failed.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Handle DELETE requests to delete a department by its ID."""
        try:
            # Fetch the department by its ID
            queryset = DepartmentModel.objects.get(id=id)
        except DepartmentModel.DoesNotExist:
            # Handle the case where the department is not found
            return Response({
                "message": "Department not found.",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the department
        queryset.delete()
        
        # Return success message for deletion
        return Response({
            "message": "Department deleted successfully.",
            "data": []
        }, status=status.HTTP_204_NO_CONTENT)
