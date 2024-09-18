from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from user_authentication.models import User
from django.core.exceptions import FieldDoesNotExist
from user_authentication.serializers import UserSerializer,UserCreateSerializer
from utils.custom_response_handler import CustomResponseHandler
from user_authentication.serializers import UserCreateSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'user_authentication'

    def post(self, request, *args, **kwargs):
        try:
            cu_queryset = self.serializer_class(data=request.data)
            if cu_queryset.is_valid():
                cu_queryset.save()
                code = 'created'
            else :
                self.errors = cu_queryset.errors
                code = 'field_error'
        except ParseError:
           code = 'json_parse_error'
        except FieldDoesNotExist as err:
            code = 'field_error'
        except ValidationError as err:
            code = 'required_field'
            self.errors = str(err)
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get_object(self):
#         try:
#             return super().get_object()
#         except User.DoesNotExist:
#             raise NotFound(detail="User not found.")

#     def put(self, request, *args, **kwargs):
#         try:
#             return super().put(request, *args, **kwargs)
#         except ValidationError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         try:
#             return super().delete(request, *args, **kwargs)
#         except User.DoesNotExist:
#             raise NotFound(detail="User not found.")
