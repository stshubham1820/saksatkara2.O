from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math
from utils.paginated_response_handler import PaginatedResponseHandler


class CustomPagination(PageNumberPagination):
    size = 10
    max_page_size = 1000
    page_size_query_param = 'size' 
      
    def get_paginated_response(self, data):
        
        if self.request.query_params.get('size'):
            self.size = int(self.request.query_params.get('size'))
            
       
        total_page = math.ceil(self.page.paginator.count / self.size)
        
        return PaginatedResponseHandler.response(
            count=self.page.paginator.count,
            total=total_page,
            size=self.size,
            current=self.page.number,
            previous=self.get_previous_link(),
            next=self.get_next_link(),
            data=data
        )