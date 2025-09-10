from django.urls import path
from . import views as v
urlpatterns = [
    # api urls
    path('chats/all', v.GetMessages.as_view(), name='chats_all'),

    # page urls
    path('', v.MainPageView.as_view(), name='main'),
]