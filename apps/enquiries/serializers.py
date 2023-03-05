from rest_framework import serializers

from .models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        # __all__ in fields means iclude all fields
        fields = "__all__"
        
        