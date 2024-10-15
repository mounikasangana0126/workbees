from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from rest_framework import status

class TimeGetAPI(APIView):
    """Department Get API View."""

    def get(self, request, *args, **kwargs):
            """Handle GET requests and return response."""
            queryset = TimeEntry.objects.all()
            serializer = TimeEntrySerializer(queryset, many=True)
            return Response(
                {
                    "message": "Departments fetched successfully.",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
    def post(self,request):
            """Handle the post requests and Post the request.data"""
        
            serializer =TimeEntrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()   
                return Response(
                    serializer.data, status =status.HTTP_201_CREATED 
                )
            return Response( serializer.error, status =status.HTTP_400_BAD_REQUEST  
            )
class patch_modelGetAPI(APIView):
        def put(self,request,id):
            queryset=TimeEntry.objects.get(id=id)
            serializer=TimeEntrySerializer(instance=queryset,data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
