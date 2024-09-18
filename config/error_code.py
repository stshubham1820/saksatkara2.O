
'''

    Here we are adding error_code that should map with our response['error_code']

'''

class error_code:
    response_code = {
    'data_not_created' : 'AiV_FW_ERR_480',
    'data_not_found' :'AiV_FW_ERR_481',
    'required_field' : 'AiV_FW_ERR_482',
    'request_failed' : 'AiV_FW_ERR_483',
    'json_parse_error' :'AiV_FW_ERR_484',
    'serializer_error' : 'AiV_FW_ERR_485',
    'field_error' : 'AiV_FW_ERR_486',
    'validation_error' : 'AiV_FW_ERR_487',
    '401':'AiV_FW_ERR_491',#unauthorised,
    'token_not_valid':'AiV_FW_ERR_492',
    'page_not_found' : 'AiV_FW_ERR_490',
    'server_error' : 'AiV_FW_ERR_500',
    'server_error' : 'AiV_SYS_ERR_500',
    'value_error' : 'AiV_SYS_ERR_502',
    'key_error' : 'AiV_SYS_ERR_503',
    'service_request_timeout' : 'AiV_SYS_ERR_504',
    'access_forbidden_error' : 'AiV_SYS_ERR_505',
    'service_unavailable' : 'AiV_SYS_ERR_506',
    'attribute_error' : 'AiV_SYS_ERR_507',
    'out_of_stock' : 'AiV_CUST_ERR_605',
    'update_failed' : 'AiV_CUST_ERR_602',
    'delete_failed' : 'AiV_CUST_ERR_603',
    'password-incorrect' : 'AiV_CUST_ERR_604',
    'method_not_allowed' : 'AiV_CUST_ERR_605',
    'otp_already_sent' : 'AiV_CUST_ERR_606',
    'limit_exceeded' : 'AiV_CUST_ERR_607',
    'audio_not_matched' : 'AiV_CUST_ERR_608',
    'invalid_access_key' : 'AiV_CUST_ERR_609',
    'audio_failed' : 'AiV_CUST_ERR_610',
    'permission_denied' : 'AiV_CUST_ERR_611',
    'key_limit_exceeded' : 'AiV_CUST_ERR_612',
    'user_already_exists' : 'AiV_CUST_ERR_613',
    'slot_not_found' : 'AiV_CUST_ERR_614',
    'user_not_found' : 'AiV_CUST_ERR_615',
    'refund_initiation_failed': 'AiV_CUST_ERR_616',
    'payment_failed' : 'AiV_CUST_ERR_617',
    'booking_time_expired' : 'AiV_CUST_ERR_618',
    'already_booked' : 'AiV_CUST_ERR_619',
    'slot_full' : 'AiV_CUST_ERR_620',
    'slot_already_got_booked' : 'AiV_CUST_ERR_621',
    }