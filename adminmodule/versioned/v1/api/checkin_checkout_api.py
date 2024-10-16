from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
class CheckInCheckOutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data = TimeEntry.objects.filter(employee__user=request.user)
        serializer = TimeEntrySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user_name)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CheckInCheckOutDetailsAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request,id):
        try:
            queryset = TimeEntry.objects.filter(id=id)
        except:
            return Response({'message':'user details not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = TimeEntrySerializer(queryset, many=True)
        return Response({'data':serializer.data,
                        'work_from_home':TimeEntry.objects.filter(work_mode='WFH').count(),
                        'work_from_office':TimeEntry.objects.filter(work_mode='WFO').count(),

                         },status=status.HTTP_200_OK)

    def put(self,request,id,date):
        try:
            queryset = TimeEntry.objects.filter(id=id, clock_in__date=date)
            if not queryset.exists():
                return Response({'message': 'Time entry not found for the given id and date'}, status=status.HTTP_404_NOT_FOUND)
            user_id=request.user.id
            user=User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(instance=queryset.first(), data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)