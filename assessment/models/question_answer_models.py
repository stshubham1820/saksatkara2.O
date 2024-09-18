from .assessment_model import Assessment
from django.db import models
from user_authentication.models import User

class AssessmentQuestions(models.Model):
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='assessment_questions')
    question = models.TextField()
    marks = models.DecimalField(max_digits=5,decimal_places=2)
    question_audio = models.FileField(upload_to='question_audio/',null=True,blank=True)

    class Meta:
        db_table = 'assessment_questions'


class AssessmentAnswers(models.Model):
    question = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='question_answers')
    answers = models.TextField(null=True,blank=True)
    given_marks = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    given_by = models.ForeignKey(User,on_delete=models.CASCADE)
    answer_audio = models.FileField(upload_to='answer_audio/',null=True,blank=True)
    answer_video = models.FileField(upload_to='answer_video/',null=True,blank=True)

    class Meta:
        db_table = 'question_answers'


class AssessmentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    current_question_index = models.IntegerField(default=0)

    class Meta:
        db_table = 'assessment_progress'