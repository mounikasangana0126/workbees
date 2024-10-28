from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import urlsafe_base64_decode
from rest_framework.permissions import AllowAny
from adminmodule.models.user_model import User

# User = get_user_model() 

class PasswordResetRequestAPI(APIView):
    """ Password reset request """
    
    permission_classes = [AllowAny]
    def post(self, request):
        """ Handle post request and return response."""
        
        email = request.data.get('email')
        username = request.data.get('username')
        user = User.objects.filter(email=email).first() or User.objects.filter(username = username).first()

        if not user:
            return Response(
                {
                    "message": "User with this email does not exist."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_link = f"http://127.0.0.1:8000/adminmodule/reset_password/{uid}/{token}/"
        message = render_to_string('password.html', {'reset_link': reset_link, 'user': user})
        send_mail('Password Reset Request', message, 'tippanaveerababu96321@gmail.com', [email])

        return Response(
            {
                "message": "Password reset link sent."
            },
            status=status.HTTP_200_OK
        )

class PasswordResetConfirmAPI(APIView):
    """ Password reset confirm."""
    
    permission_classes = [AllowAny]
    def post(self, request, uidb64, token):
        """ Password reset confirm api """
        
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response(
                {
                    "message": "Passwords do not match."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                {
                    "message": "Invalid reset link."
                    }, 
                status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response(
                {
                    "message": "The reset link is invalid or has expired."
                    }, 
                status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response(
            {
                "message": "Password has been reset successfully."
                }, 
            status=status.HTTP_200_OK)
