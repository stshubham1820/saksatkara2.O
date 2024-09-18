from rest_framework import status

'''

    Here we are adding HTTP response status that should map with our response

'''


class response_status:
    status_code = {
    'data_not_created' : status.HTTP_304_NOT_MODIFIED,
    'data_not_found' : status.HTTP_404_NOT_FOUND,
    'required_field' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'update_failed' : status.HTTP_304_NOT_MODIFIED,
    'delete_failed' : status.HTTP_304_NOT_MODIFIED,
    'request_failed' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'json_parse_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'serializer_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'field_error' : status.HTTP_400_BAD_REQUEST,
    'success' : status.HTTP_200_OK,
    'created' : status.HTTP_201_CREATED,
    'updated' : status.HTTP_200_OK,
    'deleted' : status.HTTP_204_NO_CONTENT,
    'resumed' : status.HTTP_200_OK,
    'paused' : status.HTTP_200_OK,
    'enabled' : status.HTTP_200_OK,
    'server_error' : status.HTTP_500_INTERNAL_SERVER_ERROR,
    'value_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'key_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'service_request_timeout' : status.HTTP_500_INTERNAL_SERVER_ERROR,
    'access_forbidden_error' : status.HTTP_403_FORBIDDEN,
    'service_unavailable' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'attribute_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'password-incorrect' : status.HTTP_200_OK,
    'failed' : status.HTTP_400_BAD_REQUEST,
    'method_not_allowed' : status.HTTP_400_BAD_REQUEST,
    'audio_not_matched' : status.HTTP_401_UNAUTHORIZED,
    'invalid_access_key' : status.HTTP_401_UNAUTHORIZED,
    'audio_failed' : status.HTTP_400_BAD_REQUEST,
    'permission_denied':status.HTTP_403_FORBIDDEN,
    'key_limit_exceeded' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'user_already_exists' : status.HTTP_401_UNAUTHORIZED,
    'slot_not_found' : status.HTTP_404_NOT_FOUND,
    'user_not_found' : status.HTTP_404_NOT_FOUND,
    'slot_booked' : status.HTTP_200_OK,
    'slot_already_got_booked' : status.HTTP_200_OK,
    'refund_initiation_failed' : status.HTTP_400_BAD_REQUEST,
    'refund_initiated' : status.HTTP_200_OK,
    'payment_failed' : status.HTTP_400_BAD_REQUEST,
    'booking_time_expired' : status.HTTP_200_OK,
    'already_booked' : status.HTTP_200_OK,
    'slot_full' : status.HTTP_200_OK,
    }
