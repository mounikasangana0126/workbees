
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer
from rest_framework import status

class UserGetAPI(APIView):
    """Department Get API View."""

    def get(self, request, *args, **kwargs):
            """Handle GET requests and return response."""
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(
                {
                    "message": "Departments fetched successfully.",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
    def post(self,request):
            """Handle the post requests and Post the request.data"""
            
            serializer =UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()   
                return Response(
                    serializer.data, status =status.HTTP_201_CREATED 
                )
            return Response( serializer.error, status =status.HTTP_400_BAD_REQUEST  
            )
    def patch(self,request,id):
        """Handle the patch request and update the request.data."""
        try:
            queryset=User.objects.get(pk=id)
        except:
            return Response({'error':'querry set is not found'},status=status.HTTP_404_NOT_FOUND)
        serializer =UserSerializer(queryset,data=request.data,parparital=True)
        if serializer.is_avalid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

