from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from assessment.models import Assessment,AssessmentCode
from django.core.exceptions import FieldDoesNotExist
from utils.custom_response_handler import CustomResponseHandler
from assessment.serializers import AssessmentCreateSerializer,CodeCreateSerializer


class AssessmentCreateView(generics.CreateAPIView):
    serializer_class = AssessmentCreateSerializer

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_create'

    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            cu_queryset = self.serializer_class(data=request.data)
            if cu_queryset.is_valid():
                cu_queryset.save()
                self.data = cu_queryset.data
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
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)
        

class AssessmentCodeView(generics.CreateAPIView):
    serializer_class = CodeCreateSerializer

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_code'



    def post(self, request, *args, **kwargs):
        try:
            cu_queryset = self.serializer_class(data=request.data)
            if cu_queryset.is_valid():
                cu_queryset.save()
                self.data = cu_queryset.data
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
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)
        

class AssessmentCheckView(generics.CreateAPIView):

    '''
    cr represents the custom_response_handler the response format will be constant
    in each and every situation
    '''
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_check'

    def post(self,request,pk):
        try :
            assessment_code = request.data.get('assessment_code')
            email = request.data.get('user_email')
            ac_instance = AssessmentCode.objects.prefetch_related('access_for').get(code=assessment_code)
            code = "access_denied"
            if email in  ac_instance.access_for.values_list('address', flat=True):
                code = "access_granted"
        except ParseError:
           code = 'json_parse_error'
        except Exception as err:
            code = 'server_error'
            self.errors = str(err)
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)