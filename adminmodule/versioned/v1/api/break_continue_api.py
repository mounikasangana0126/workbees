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
        """ Handle get request to fetch all the break entry records of an employee."""
        snippet=BreakEntry.objects.filter(time_entry__employee__user=request.user)
        serializer=BreakEntrySerializer(snippet,many=True)
        return Response({
            'message':'Break entry records of an employee fetched successfully',
            'data':serializer.data
        }, status= status.HTTP_200_OK)
        
    def post(self,request):
        """ Handle post request to add break entry record to time entry of an employee."""
        serializer=BreakEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Break entry created successfully',
                'data':serializer.data
                },status=status.HTTP_201_CREATED)
        return Response({
            'message': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

class BreakContinueDetailAPI(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request, id):
        """ Handle get request to fetch a particular break entry record.."""
        try:
            snippet=BreakEntry.objects.get(id=id)
        except:
            return Response({'message':'BreakEntry not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=BreakEntrySerializer(snippet)
        return Response({
            'message':'break record fetched successfully',
            'data':serializer.data
        },status= status.HTTP_200_OK)

    def put(self, request,id):
        """ Handle put request to update break entry record"""
        try:
            time_entry = request.data.get('time_entry')
            if not time_entry:
                return Response({"error": "time_entry not provided"}, status=status.HTTP_400_BAD_REQUEST)

            queryset = BreakEntry.objects.get(id=id)
        except BreakEntry.DoesNotExist:
            return Response({"error": "BreakEntry not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        queryset.break_end = timezone.now()
        queryset.save()
        total_seconds=(queryset.break_end-queryset.break_start).total_seconds()
        serializer=BreakEntrySerializer(queryset)
        return Response({
            'message': 'Break time updated successfully',
            'data':serializer.data,
            'total_seconds':total_seconds
            }, 
            status=status.HTTP_200_OK)

    def delete(self, request, id):
        """ Handle delete request to delete a particular break entry."""
        try:
            queryset = BreakEntry.objects.get(id=id)
        except BreakEntry.DoesNotExist:
            return Response({"error": "BreakEntry not found"}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({"message": "BreakEntry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

