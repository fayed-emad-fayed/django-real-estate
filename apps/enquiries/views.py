from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from real_estate.settings.development import DEFAULT_FROM_EMAIL

from .models import Enquiry
from .serializers import EnquirySerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data
    print(data)
    
    serializer = EnquirySerializer(data)
    
    if serializer.is_valid():
        enquiry = serializer.save()
        send_mail(subject=enquiry.subject,
                message=enquiry.message,
                email=enquiry.email,
                recipient_list=[DEFAULT_FROM_EMAIL],
                fail_silently=True)

        return Response({"success": "Your Enquiry was successfully submitted"}, status=201)
    return Response({"fail": "Your Enquiry was failed submitted"})