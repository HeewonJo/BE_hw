from django.urls import path
from .views import *
# from .views import IndexView

urlpatterns = [
    # path('', IndexView.as_view(), name='list'),
    path('', list, name = "list"),
    path('result/', result, name = "result"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),
]