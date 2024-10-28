"""Web Login API."""

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer

class LoginAPI(APIView):
    """API for user login."""

    permission_classes = [AllowAny] 

    def post(self, request):
        """Handle POST request for user login with username/email and password."""
        
        username = request.data.get("username")  
        password = request.data.get("password")  
        
        user_exists = User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists()

        if not user_exists:
            return Response(
                {
                    "message": "Authentication failed. User does not exist."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(username=username).first() or User.objects.filter(email=username).first()

        if user:
            if user.check_password(password):  
                refresh = RefreshToken.for_user(user)  
                access_token = str(refresh.access_token) 

                serializer = UserSerializer(user)
                my_data = serializer.data
                my_data["access_token"] = access_token 
                my_data["refresh_token"] = str(refresh) 
                
                return Response(my_data, status=status.HTTP_200_OK) 

            return Response(
                {
                    "message": "Login Failed. Password is Incorrect"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "message": "Authentication failed. User does not exist."
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ResetPasswordAPI(APIView):
    """ Reset Password.."""
    
    permission_classes = [AllowAny]
    def post(self, request):
        """ Handle post request and reset password."""
        
        username = request.data.get('username')
        password = request.data.get('password')
        new_password = request.data.get('confirm_password')
        email = request.data.get('email')
        
        user_exists = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

        if not user_exists:
            return Response(
                {
                    "message": "User doesnot exists."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if password != new_password:
            return Response(
                {
                    'message':'Password and new_password is not same'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user_exists.set_password(new_password)
        user_exists.save()
        return Response(
            {
                
                'message':'Password changed..'
            },
            status=status.HTTP_202_ACCEPTED
        )
        