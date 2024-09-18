from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from django.core.exceptions import FieldDoesNotExist
from utils.custom_response_handler import CustomResponseHandler
from django.db.models import Prefetch
from assessment.serializers import SkillSerializer,AssessmentSkillSerializer
from assessment.models import AssessmentSkills,Assessment




class AssessmentSkillView(GenericAPIView):

    serializer_class = SkillSerializer
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_skill'

    def get(self, request,pk, *args, **kwargs):
        try :
            user = Assessment.objects.get(id=pk)

            '''
            Optimized query to fetch top-level skills and their sub-skills
            '''
            assessment_skills = AssessmentSkills.objects.filter(assessment=user, parent_skill__isnull=True).prefetch_related(
                Prefetch('sub_skills', queryset=AssessmentSkills.objects.all())
            )
            user_queryset = AssessmentSkillSerializer(assessment_skills,many=True)
            self.data = user_queryset.data
            code = 'success'
        except ParseError:
           code = 'json_parse_error'
        except Assessment.DoesNotExist:
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