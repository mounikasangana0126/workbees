from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.shift_timings_model import WorkShiftsModel
from adminmodule.versioned.v1.serializer.shift_timings_serializer import ShiftTimeSerializer
from rest_framework import status
from utils.helper.permission import SuperuserPermission
class ShiftTimingGetAPI(APIView):
    """Department Get API View."""
    permission_classes=[SuperuserPermission]
    def get(self, request):
        """Handle get request and return response"""
        queryset=WorkShiftsModel.objects.all()
        serializer=ShiftTimeSerializer(queryset,many=True)
        return Response(
            {
                "message":"Shift_Time fetched Successfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    def post(self,request):
        serializer=ShiftTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ShiftTimingDetailGetAPI(APIView):
    permission_classes=[SuperuserPermission]

    def get(self,request,id):
        try:
            queryset=WorkShiftsModel.objects.get(id=id)
        except:
            return Response({'error':'Data does not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=ShiftTimeSerializer(queryset)
        return Response(serializer.data)
        
    def put(self,request,id):
        try:
            queryset=WorkShiftsModel.objects.get(id=id)
        except:
            return Response({'error':'Data does not found'},status=status.HTTP_400_BAD_REQUEST)
        serialize=ShiftTimeSerializer(instance=queryset,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            queryset=WorkShiftsModel.objects.get(id=id)
        except:
            return Response({'error':'Data does not found'},status=status.HTTP_400_BAD_REQUEST)
        queryset.delete()
        return Response({'message':'Data deleted successfully'},status=status.HTTP_204_NO_CONTENT)



