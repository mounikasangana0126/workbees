from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.versioned.v1.serializer.shift_timings_serializer import ShiftTimeSerializer
from rest_framework import status

class ShiftTimingGetAPI(APIView):
    """Department Get API View."""

    def get(self, request, *args, **kwargs):
        """Handle get request and return response"""

        queryset=TimeEntry.objects.all()
        serializer=ShiftTimeSerializer(queryset,many=True)
        return Response(
            {
                "message":"Shift_Time fetched Successfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    def post(self,request,*args,**kwargs):
        queryset=TimeEntry.objects.all()
        serializer=ShiftTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ShiftTimingDetailGetAPI(APIView):
    def put(self,request,id):
        try:
            queryset=TimeEntry.objects.get(id=id)
        except:
            return Response({'error':'Data does not found'},status=status.HTTP_400_BAD_REQUEST)
        serialize=ShiftTimeSerializer(instance=queryset,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        queryset=TimeEntry.objects.all()
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



