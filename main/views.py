from django.shortcuts import render
from django.views import View
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models as m, forms as f

# Create your views here.


class MsgFormView(generic.CreateView):
    template_name = 'msg_form.html'
    model = m.Message
    fields = '__all__'


