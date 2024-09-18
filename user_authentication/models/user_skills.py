from django.db import models
from .user import User  

class UserSkill(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="skills", on_delete=models.CASCADE)
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
        db_table = 'user_skill'