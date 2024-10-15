from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
from adminmodule.models.break_entry_model import BreakEntry
from datetime import datetime
from django.utils import timezone
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class BreakContinueAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        snippet=BreakEntry.objects.all()
        serializer=BreakEntrySerializer(snippet,many=True)
        return Response(serializer.data)
    def post(self,request):
        time_entry=request.data.get('time_entry')
        print(time_entry)
        serializer=BreakEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        try:
            time_entry = request.data.get('time_entry')
            if not time_entry:
                return Response({"error": "time_entry not provided"}, status=status.HTTP_400_BAD_REQUEST)

            queryset = BreakEntry.objects.get(pk=request.data.get('id'))
        except BreakEntry.DoesNotExist:
            return Response({"error": "BreakEntry not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        queryset.break_end = timezone.now()
        queryset.save()
        total_seconds=(queryset.break_end-queryset.break_start).total_seconds()
        serializer=BreakEntrySerializer(queryset)
        return Response({'data':serializer.data,
                         'total_seconds':total_seconds,
                         'message': 'Break time updated successfully'}, 
                         status=status.HTTP_200_OK)

