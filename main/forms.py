from django import forms

from . import models as m


# TODO make a updated user login form 

# a group create form

class MsgForm(forms.ModelForm):
    '''Message form'''
    class Meta:
        model = m.Message
        fields = [
            'text'
            ]
