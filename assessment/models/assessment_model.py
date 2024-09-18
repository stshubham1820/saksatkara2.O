from django.db import models
from user_authentication.models import User
import uuid

class Assessment(models.Model):

    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_assessment')
    assessment_title = models.CharField(max_length=150)
    assessment_for = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'assessment'

class Email(models.Model):
    address = models.EmailField(unique=True)

    def __str__(self):
        return self.address
    
    class Meta:
        db_table = 'email_table'


class AssessmentCode(models.Model):

    choice = (
        ('ONE','ONE'),
        ('MANY','MANY')
    )

    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='assessment_link')
    code = models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4, editable=False)
    access_for = models.ManyToManyField(Email, blank=True)
    assessment_type = models.CharField(max_length=100,choices=choice,default='ONE')
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'assessment_code'


class AssessmentSkills(models.Model):

    name = models.CharField(max_length=255)
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='assessment_skills')
    parent_skill = models.ForeignKey('self', related_name="sub_skills", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_sub_skills(self, level=0):
        """
        Recursively get all sub-skills up to n levels
        """
        sub_skills = []
        for sub_skill in self.sub_skills.all():
            sub_skills.append((sub_skill, level))
            sub_skills.extend(sub_skill.get_sub_skills(level + 1))
        return sub_skills
    
    class Meta:
        db_table = 'assessment_skills'

    
