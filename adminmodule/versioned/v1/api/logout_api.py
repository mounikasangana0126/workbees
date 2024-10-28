from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token", None)
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "message": "Logged out successfully."
        }, status=status.HTTP_200_OK)

        return Response({
            "message": "Refresh Token Invalid."
        }, status=status.HTTP_400_BAD_REQUEST)
