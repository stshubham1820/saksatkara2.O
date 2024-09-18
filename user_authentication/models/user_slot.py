from django.db import models
from .user import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        db_table = 'event'

class Slot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='event_slots')
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_slots = models.PositiveIntegerField()

    class Meta:
        db_table = 'slot'


class Booking(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE,related_name='slot_bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_slot_bookings')
    booking_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)  
    expires_at = models.DateTimeField()  
    payment_started = models.BooleanField(default=False)

    class Meta:
        db_table = 'booking'