from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.shift_timings_model import WorkShiftsModel
from adminmodule.versioned.v1.serializer.shift_timings_serializer import ShiftTimeSerializer
from rest_framework import status
from utils.helper.permission import SuperuserPermission

class ShiftTimingGetAPI(APIView):
    """ ShiftTiming class."""
    permission_classes = [SuperuserPermission]

    def get(self, request):
        """ Handle Get request and return response."""
        
        queryset = WorkShiftsModel.objects.all()
        if not queryset.exists():
            return Response(
                {
                    'message':'No shift_times till now',
                    'data':[]
                },
                status=status.HTTP_200_OK
            )
        serializer = ShiftTimeSerializer(queryset, many=True)
        return Response(
            {
                "message": "Shift timings fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """ Handle post request and add data."""
        
        serializer = ShiftTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Shift timing created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message': 'Invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class ShiftTimingDetailGetAPI(APIView):
    """ ShiftTimingDetail class."""
    
    permission_classes = [SuperuserPermission]

    def get(self, request, id):
        """ Handle get request and return response.."""
        try:
            queryset = WorkShiftsModel.objects.get(id=id)
        except WorkShiftsModel.DoesNotExist:
            return Response(
                {
                    'message': 'Shift timing not found',
                    'data':[]
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShiftTimeSerializer(queryset)
        return Response(
            {
                'message': 'Shift timing fetched successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )
        
    def put(self, request, id):
        try:
            queryset = WorkShiftsModel.objects.get(id=id)
        except WorkShiftsModel.DoesNotExist:
            return Response(
                {
                    'error': 'Shift timing not found',
                    'data':[]
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShiftTimeSerializer(instance=queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Shift timing updated successfully',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'message': 'Invalid data',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        try:
            queryset = WorkShiftsModel.objects.get(id=id)
        except WorkShiftsModel.DoesNotExist:
            return Response(
                {
                    'error': 'Shift timing not found',
                    'data':[]
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

        queryset.delete()
        return Response(
            {
                'message': 'Shift timing deleted successfully',
            },
            status=status.HTTP_204_NO_CONTENT
        )
