import qrcode, base64
from io import BytesIO
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from adminmodule.models.user_model import User
from django.conf import settings
from django.utils import timezone
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from django.http import JsonResponse
from dateutil import parser

class QrCodeGeneration(APIView):
    """ QR code generation."""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """ Handle get request and return response."""
        
        employee = str(request.user.id)
        expire_time = timezone.now()+timedelta(minutes=50)
        token_data = {
            'employee' : employee,
            'expire_time' : expire_time.isoformat()
        }
        token = jwt.encode(token_data,settings.SECRET_KEY,algorithm="HS256")
        qr = qrcode.make(token)
        buffered = BytesIO()
        qr.save(buffered, format = "PNG")
        qr_code_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return JsonResponse(
            {
                'qr_code_base64' : qr_code_base64
            }
        )
        
        
class QrCodeValidateAPI(APIView):
    
    def post(self, request):
        # Get the token from the request
        token = request.data.get('token')
        print(type(token))
        
        # Decode the token using the secret key
        try:
            decode_data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return Response({"error": "The token has expired."}, status=400)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token."}, status=400)
        
        # Extract employee and expire_time from the decoded data
        employee = decode_data.get('employee')
        expire_time = decode_data.get('expire_time')
        
        # Convert expire_time string back to a datetime object
        expire_time = parser.isoparse(expire_time)

        # Check if the QR code is expired
        if expire_time < timezone.now():
            return Response(
                {"error": "QR code expired."},
                status=400
            )
        
        # If valid, return a success response
        return Response(
            {"message": "Logged in successfully."}
        )
        