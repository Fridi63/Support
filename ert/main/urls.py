from django.urls import path, include

from .views import ExampleView

urlpatterns = [

    path('example/', ExampleView.as_view()),


]
