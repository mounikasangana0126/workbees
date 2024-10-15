
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserGetAPI(APIView):
    """Department Get API View."""
    permission_classes=[IsAuthenticated]
    def get(self, request,):
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
            return Response( serializer.errors, status =status.HTTP_400_BAD_REQUEST  
            )
class UserPutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,id):
        """Handle the patch request and update the request.data."""
        try:
            queryset=User.objects.get(pk=id)
        except:
            return Response({'error':'querry set is not found'},status=status.HTTP_404_NOT_FOUND)
        serializer =UserSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        try:
            snippet=User.objects.get(id=id)
        except:
            return Response({'error':'querry set is not found'},status=status.HTTP_404_NOT_FOUND)
        snippet.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)



