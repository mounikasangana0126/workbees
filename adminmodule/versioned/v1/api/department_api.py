from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.department_model import DepartmentModel
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer
from rest_framework import status


class DepartmentGetAPI(APIView):
    """Department Get API View."""
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests and return response."""
        
        queryset = DepartmentModel.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(
            {
                "message": "Departments fetched successfully.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    