from rest_framework.views import exception_handler
from config.error_code import error_code

'''
    Here we are overriding the default exception_handler method 
    to create custom exception response that should be in our desired format

    {
	    "success" : false,
	    "error_code" : "CDATS_FW_ERR_xxx",
	    "message" : "Error",
    }


    @version v1.0
    @return json
    
'''

def FailedResponseHandler(exception, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exception, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        try :
            if response.data.get('code'): 
                response.data['error_code'] = error_code.response_code.get(response.data.get('code'))
            else :
                response.data['error_code'] = error_code.response_code.get(str(response.status_code))
            response.data['message'] = response.data['detail']
            response.data['message'] = response.data['message']
            response.data['status'] = False
            response.data.pop('detail')
        except Exception :
            pass
        finally :
            return response