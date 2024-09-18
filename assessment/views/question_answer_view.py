from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError,ParseError,ValidationError
from assessment.models import Assessment,AssessmentSkills,AssessmentQuestions
from django.core.exceptions import FieldDoesNotExist
from utils.custom_response_handler import CustomResponseHandler
from django.db.models import Prefetch
from assessment.service import QuestionService
from assessment.serializers import AssessmentQuestionSerializer,AssessmentAnswerSerializer
import json
from gtts import gTTS

class QuestionCreateView(generics.GenericAPIView):
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_question'

    def build_tree(self,skill):
        return {
            skill.name: [
                self.build_tree(sub_skill) for sub_skill in skill.sub_skills.all()
            ] or skill.name
        }

    def post(self,request,pk):
        try : 
            assessment = Assessment.objects.get(id=pk)
            assessment_skills = AssessmentSkills.objects.filter(assessment=assessment, parent_skill__isnull=True).prefetch_related(
                Prefetch('sub_skills', queryset=AssessmentSkills.objects.all())
            )

            result = {skill.name: self.build_tree(skill)[skill.name] for skill in assessment_skills}
            qs = QuestionService().prompt_text(result)
            qs_data = json.loads(qs)
            questions = qs_data.get('Questions')
            question_list = []
            for i in questions:
                aq = AssessmentQuestions(assessment=assessment,question=i,marks=10.00)
                question_list.append(aq)
            AssessmentQuestions.objects.bulk_create(question_list)
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
        


class QuestionReadView(generics.GenericAPIView):
    serializer_class = AssessmentQuestionSerializer
    cr = CustomResponseHandler 
    data = None
    errors = None
    app_name = 'assessment_question'

    def get(self,request,pk,id):
        try :
            aq = AssessmentQuestions.objects.get(id=id)
           
            if not aq.question_audio:
                language = 'en'
                myobj = gTTS(text=aq.question, lang=language, slow=False)
                name = f'/saksatkara/media/question_audio/{aq.id}.wav'
                myobj.save(name)
                aq.question_audio =f'/media/question_audio/{aq.id}.wav'
                aq.save()
                user_queryset = self.serializer_class(aq)
                self.data = user_queryset.data
                code = 'success'
        except ParseError:
           code = 'json_parse_error'
        except AssessmentQuestions.DoesNotExist:
            code = 'data_not_found'
        except Exception as err:
            self.errors = str(err)
            code = 'server_error'
        finally : 
            return self.cr.response(request,code,app_name=self.app_name,data=self.data,errors=self.errors)
        
    
    def post(self,request,pk,id):
        try:
            as_queryset = AssessmentAnswerSerializer(data=request.data)
            if as_queryset.is_valid():
                as_queryset.save()
                self.data = as_queryset.data
                code = 'created'
            else :
                self.errors = as_queryset.errors
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
