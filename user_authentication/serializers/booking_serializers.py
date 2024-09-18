from rest_framework import serializers
from user_authentication.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'expires_at': instance.expires_at
        }