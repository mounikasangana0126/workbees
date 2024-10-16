"""Web Login API."""

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer


class LoginAPI(APIView):
    """Login API."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Get user with given username and password."""
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.filter(username=username).exists()
        if not user:
            user = User.objects.filter(email=username).exists()

        if user:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

            if user.check_password(password):
                
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                serializer = UserSerializer(user)
                my_data = serializer.data
                my_data["access_token"] = access_token
                my_data["refresh_token"] = str(refresh)
                return Response(my_data, status=status.HTTP_200_OK)

            return Response({"message": "Login Failed. Password is Incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Authentication failed. User does not exist."}, status=status.HTTP_400_BAD_REQUEST)
