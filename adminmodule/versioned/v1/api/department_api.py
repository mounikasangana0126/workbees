from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.department_model import DepartmentModel, ParentModel
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer, ParentSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ParentGetAPI(APIView):
    """Parent Get API View."""
    
    def get(self, request, *args, **kwargs):
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
    
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        """Handle GET requests and return response."""
        queryset = DepartmentModel.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = DepartmentSerializer(page, many=True)
        response_data = {
            "message": "Departments fetched successfully.",
            "data": serializer.data,
            "page_size": paginator.page_size,
            "page_number": paginator.page.number,
            "total_pages": paginator.page.paginator.num_pages
        }
        return paginator.get_paginated_response(response_data)
        
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
