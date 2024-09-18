from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from user_authentication.models import User,Slot,Booking
from django.core.exceptions import FieldDoesNotExist
from user_authentication.serializers import UserSerializer,UserCreateSerializer
from utils.custom_response_handler import CustomResponseHandler
from user_authentication.serializers import BookingSerializer
from django.db import transaction
from django.utils import timezone
from datetime import timedelta


class SlotCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'user_authentication_slot'

    def post(self, request,pk, *args, **kwargs):
        try:
            with transaction.atomic():
                user = User.objects.get(pk=pk)
                slot_id = request.data.get('slot_id')
                slot = Slot.objects.select_for_update().get(id=slot_id)

                if slot.total_slots > Booking.objects.filter(slot=slot, is_confirmed=True).count():
                    # Create a pending booking with 5 minutes expiration time
                    expires_at = timezone.now() + timedelta(minutes=5)
                    # booking = Booking.objects.create(
                    #     slot=slot, user=user, expires_at=expires_at
                    # )
                    booking_dict = {"slot":slot_id,"user":pk,"expires_at":expires_at}
                    
                    cu_queryset = self.serializer_class(data=booking_dict)
                
                    if cu_queryset.is_valid():
                        cs = cu_queryset.save()
                        rd = self.serializer_class(cs).data
                        self.data = rd
                        code = 'created'
                    else :
                        self.errors = cu_queryset.errors
                        code = 'field_error'
                else:
                    code = 'slot_full'
            
        except ParseError:
           code = 'json_parse_error'
        except FieldDoesNotExist as err:
            code = 'field_error'
        except ValidationError as err:
            code = 'required_field'
            self.errors = str(err)
        except Slot.DoesNotExist as err:
            code = 'slot_not_found'
        except User.DoesNotExist as err:
            code = 'user_not_found'
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)


def confirm_payment():
    return True

def refund_payment():
    return True

class ReserveSlotView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'user_authentication_slot'

    def post(self, request,pk, *args, **kwargs):
        try:
            with transaction.atomic():
                # Fetch the booking and lock the slot
                user = User.objects.get(id=pk)
                booking_id = request.data.get('booking_id')
                slot_id = request.data.get('slot_id')
                booking = Booking.objects.select_for_update().get(id=booking_id, user=user)

                # Revalidate the slot's availability by locking the slot row
                slot = Slot.objects.select_for_update().get(id=slot_id)

                confirmed_bookings = Booking.objects.filter(slot=slot, is_confirmed=True).count()

                if confirmed_bookings >= slot.total_slots:
                    
                    booking.delete()  # Or mark as failed
                    code = 'slot_already_got_booked'

                else:
                    if booking.expires_at < timezone.now():
                        code = 'booking_time_expired'
                    elif booking.is_confirmed:
                        code = 'already_booked'
                    else :
                        cp = confirm_payment()
                        code = 'payment_failed'
                        if cp :
                            if confirmed_bookings >= slot.total_slots:
                                rp = refund_payment()
                                code = 'refund_initiation_failed'
                                if rp:
                                    code = 'refund_initiated'
                            else:
                                booking.is_confirmed = True
                                booking.save()
                                code = 'slot_booked'

        except Booking.DoesNotExist:
            code = 'booking_not_found'
        except Slot.DoesNotExist:
            code = 'slot_not_found'
        except ParseError:
           code = 'json_parse_error'
        except FieldDoesNotExist as err:
            code = 'field_error'
        except ValidationError as err:
            code = 'required_field'
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)
            
            