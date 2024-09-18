from config.error_code import error_code
from config.response_status import response_status
from config.response_message import response_message
from rest_framework.response import Response
from config.error_level import error_level
import logging

'''

   Here we are making custom response that is handling the api response

'''


class CustomResponseHandler :

   #todo: integrate this in response itself
   def pagination_response(code,data=None,errors=None):

      if error_code.response_code.get(code) :
         if data == None:
            data = {}
            data['success']=False
            data['error_code']=error_code.response_code.get(code)
            if errors != None:
               data['errors'] = errors

      return Response(data,status=response_status.status_code.get(code))



   def response(request,code, app_name=None,data=None,errors=None,links=None):
      logger = logging.getLogger('django')
      response_data = {
         'success':True
      }
      # Handle error code
      if error_code.response_code.get(code) :
         response_data['success']=False
         response_data['error_code']=error_code.response_code.get(code)

      # Handle error message
      if response_message.message.get(code) :
         response_data['message'] = response_message.message.get(code)

      # Handle data

      if data != None:
        response_data['data'] = data

      if errors != None:
        response_data['errors'] = errors

      if links != None:
        response_data['links'] = links

      if response_data.get('success')==False:
         mapping = {
            'app_name':app_name,
            'error_code':response_data['error_code'],
            'method':request.method,
            'url':request.get_full_path(),
            'data':data,
            }
         logger = logging.LoggerAdapter(logger, mapping)
         if error_level.response_code.get(code) == 'warning' :
            logger.warning(response_data['message'])
         elif error_level.response_code.get(code) == 'error':
            logger.error(response_data['message'])
         else :
            logger.error(response_data['message'])

      return Response(response_data, status=response_status.status_code.get(code))
