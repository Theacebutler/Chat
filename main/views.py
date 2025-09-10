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
        all_msgs = []
        msgs = m.Message.objects.all().order_by('-date_created')
        for msg in msgs:
            x = {
                'text': msg.text,
                'writer': msg.writer.username,
            }
            all_msgs.append(x)
        x = {'messages': all_msgs}
        # res = serializers.serialize('json', msgs)
        res = json.dumps(x)
        
        return HttpResponse(res, content_type = 'application.json')
        


# TODO #4 creae the groups endpoint
class GetGroups(View):
    def get(self, requset):
        all_groups = []
        gs = m.Group.objects.all()
        for groups in gs:
            ...
# class GetChats