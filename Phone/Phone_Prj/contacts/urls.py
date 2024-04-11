from django.urls import path
from .views import *
from .views import IndexView

urlpatterns = [
    # path('', list, name = "list"),
    path('result/', result, name = "result"),
    path('', IndexView.as_view(), name='list'),
]