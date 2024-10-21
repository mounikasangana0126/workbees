from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.department_model import DepartmentModel
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer
from utils.helper.permission import SuperuserPermission

class DesignationGetAPI(APIView):
    """ Designation class."""
    permission_classes = [SuperuserPermission]
    
    def get(self, request, *args, **kwargs):
        """ Handle Get request and return response."""
        
        queryset = DesignationModel.objects.all()
        if not queryset.exists():
            return Response(
                {
                    'message':'No departments are registered till now',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        serializer = DesignationSerializer(queryset, many=True)
        return Response(
            {
                'message': 'Designations fetched successfully',
                'data': serializer.data if serializer.data else []
            },
            status=status.HTTP_200_OK
        )
        
    def post(self, request):
        """ Handle post request and add new designation."""
        print(request.data)
        
        try:
            department = DepartmentModel.objects.filter(dept_name = request.data['department']).first()
        except:
            return Response(
                {
                    'error':'Department doestnot exists.',
                    'data':[]
                },
                status=status.HTTP_404_NOT_FOUND
            )
        print(department.id)
        data = request.data
        data['department'] = department.id
        serializer = DesignationSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response(
                {
                    'message': 'Designation created successfully',
                    'data': serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message': 'Invalid data provided',
                'errors': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

class DesignationGetDetailAPI(APIView):
    """ Designation class.."""
    
    permission_classes = [SuperuserPermission]
    
    def get(self, request, id):
        """Handle get request and return response."""
        try:
            designation = DesignationModel.objects.get(id=id)
        except DesignationModel.DoesNotExist:
            return Response(
                {
                    "message": "Designation not found",
                    "data": []
                }, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DesignationSerializer(designation)
        return Response(
            {
                'message': 'Designation fetched successfully',
                'data': serializer.data if serializer.data else []
            }, 
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """ Handle put request and update data."""
        try:
            queryset = DesignationModel.objects.get(id=id)
        except DesignationModel.DoesNotExist:
            return Response(
                {
                    "message": "Designation not found",
                    "data": []
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        department = DepartmentModel.objects.get(dept_name = queryset.department)
        data= request.data
        data['department'] = department.id
        serializer = DesignationSerializer(queryset, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Designation updated successfully',
                    'data': serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                'message': 'Invalid data provided',
                'errors': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        """ Handle delete request."""
        try:
            queryset = DesignationModel.objects.get(id=id)
        except DesignationModel.DoesNotExist:
            return Response(
                {
                    "message": "Designation not found",
                    "data": []
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        queryset.delete()
        return Response(
            {
                'message': 'Designation deleted successfully',
                'data': []
            }, 
            status=status.HTTP_204_NO_CONTENT
        )
