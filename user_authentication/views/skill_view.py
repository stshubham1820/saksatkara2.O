from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from user_authentication.models import UserSkill,User
from django.core.exceptions import FieldDoesNotExist
from user_authentication.serializers import UserSerializer,UserCreateSerializer
from utils.custom_response_handler import CustomResponseHandler
from user_authentication.serializers import SkillSerializer,UserSkillSerializer
from django.db.models import Prefetch



class UserSkillView(GenericAPIView):

    serializer_class = SkillSerializer
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'user_authentication_user_skill'

    def get(self, request,pk, *args, **kwargs):
        try :
            user = User.objects.get(id=pk)

            '''
            Optimized query to fetch top-level skills and their sub-skills
            '''
            user_skills = UserSkill.objects.filter(user=user, parent_skill__isnull=True).prefetch_related(
                Prefetch('sub_skills', queryset=UserSkill.objects.all())
            )
            user_queryset = UserSkillSerializer(user_skills,many=True)
            self.data = user_queryset.data
            code = 'success'
        except ParseError:
           code = 'json_parse_error'
        except User.DoesNotExist:
            code = 'data_not_found'
        except Exception as err:
            self.errors = str(err)
            code = 'server_error'
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)

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