from django.db import models
from .user import User

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_profile')

    profile_pic = models.ImageField(upload_to='profile-pic/',null=True,blank=True)

    '''
    decimal_places=2: This specifies the number of decimal places allowed for the number. In this case, up to 3 digits after the decimal point are allowed.

    max_digits=20: This defines the total number of digits allowed in the number, including both sides of the decimal point.
    
    '''
    credit_balance = models.DecimalField(decimal_places=2,max_digits=20,null=True,blank=True)

    class Meta:
        db_table = 'user_profile'
    