from django.urls import path
from . import views as v
urlpatterns = [
    path('groups/all', v.get_groups, name='groups_all'),
    path('chats/all', v.GetMessages.as_view(), name='chats_all'),
    path('', v.MainPageView.as_view(), name='main'),
]