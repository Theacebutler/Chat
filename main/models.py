from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.


# a user model

# TODO #2 extend the django user model

# a group model
class Group(models.Model):
    '''the group model'''
    title = models.CharField(max_length=30, 
                             validators= [MinLengthValidator(2)])
    date_created = models.DateTimeField(auto_created=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
# a msg model
class Message(models.Model):
    '''the message modle'''
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=256, 
                            validators=[MinLengthValidator(2)])
    # TODO #1 add images to message
    
    def __str__(self):
        return f'{self.text}'
