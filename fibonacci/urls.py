from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/fibonacci/<int:index>/', 
        views.FibonacciValueByIndex.as_view(),
        name='fibonacci-index'
        ),
]

