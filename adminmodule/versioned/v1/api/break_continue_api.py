from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
from adminmodule.models.break_entry_model import BreakEntry
from datetime import datetime
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class BreakContinueAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        snippet=BreakEntry.objects.filter(time_entry__employee__user=request.user)
        serializer=BreakEntrySerializer(snippet,many=True)
        return Response(serializer.data)
    def post(self,request):
        time_entry=request.data.get('time_entry')
        serializer=BreakEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BreakContinueDetailAPI(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request, id):
        try:
            snippet=BreakEntry.objects.get(id=id)
        except:
            return Response({'message':'BreakEntry not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=BreakEntrySerializer(snippet)
        return Response(serializer.data)

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

    def delete(self, request, id):
        try:
            queryset = BreakEntry.objects.get(pk=id)
        except BreakEntry.DoesNotExist:
            return Response({"error": "BreakEntry not found"}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({"message": "BreakEntry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

