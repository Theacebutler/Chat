from django.urls import path
from . import views as v
urlpatterns = [
    path('message/new', v.MsgFormView.as_view(), name='form_create')
]