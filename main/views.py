from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models as m, forms as f

import json

from MyUtils.log import log

# Create your views here.




class HomeView(View):
    '''The main home view'''
    def get(self, requset):
        ctx = {
            'get_groups': reverse_lazy('groups_all'),
            'get_messages': reverse_lazy('chats_all')
        }
        return render(requset, 'home.html')


class MainPageView(View):
    def get(self, requset):
        form = f.MsgForm()
        ctx = {
            'form': form,
            'url': reverse_lazy('chats_all')
        }
        return render(requset, 'main.html', context=ctx)


    def post(self, requset):

        form = f.MsgForm(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.writer = self.request.user
            obj.save()
        return redirect(reverse_lazy('main'))



class GetMessages(View):
    def get(self, requset):
        msgs = m.Message.objects.all()
        res = serializers.serialize('json', msgs)
        
        return HttpResponse(res, content_type = 'application.json')
        
        return JsonResponse(res, safe=False)
    



def get_groups(request):
    data = {1: 'this is a mesage', 2: '3 min ago'}
    return JsonResponse(data=data)

# class GetChats