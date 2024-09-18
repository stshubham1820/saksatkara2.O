from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, employee_id, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,employee_id, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.role="ADMIN"
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_choice = (
        ('ADMIN','ADMIN'),
        ('USER','USER'),
        ('CANDIDATE','CANDIDATE')
    )
    id = models.AutoField(primary_key=True,unique=True,verbose_name='id')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    fullname = models.CharField(verbose_name='full name',max_length=100)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    role = models.CharField(max_length=100,choices=user_choice,default='USER')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    