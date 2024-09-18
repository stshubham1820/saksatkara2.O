from config.error_code import error_code
from config.response_status import response_status
from config.response_message import response_message
from rest_framework.response import Response
from config.error_level import error_level
import logging 
from rest_framework import status
'''

   Here we are making custom response that is handling the api response 

'''


class PaginatedResponseHandler :
   def response(count=None,total=None,size=None,current=None,previous=None,next=None,data=None):
      
      # Handle data
      if data != None:
        response_data = {
         'success' : True,
         'data': data
        }
      if count != None:
         response_data['count']=count
      if total != None:
         response_data['total']=total
      if size != None:
         response_data['size']=size
      if current != None:
         response_data['current']=current
      if previous != None:
         response_data['previous']=previous
      if next != None:
         response_data['next']=next
         
      return Response(response_data, status=status.HTTP_200_OK)