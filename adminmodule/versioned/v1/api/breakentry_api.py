from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.break_entry_model import BreakEntry
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer

class BreakEntryGetAPI(APIView):
    
    def get(self,request, *args, **kwargs):
        queryset = BreakEntry.objects.all()
        serializer = BreakEntrySerializer(queryset, many =True)
        return Response(
            {
                "messege":"BreakEntry fetched successfullt",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )
        
    def post(self, request):
        serializer = BreakEntrySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            queryset = BreakEntry.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = BreakEntrySerializer(queryset, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)