from django.urls import path
from .views import WigetList, WigetDetails

urlpatterns = [
    path('', WigetList.as_view()),
    path('<int:pk>/', WigetDetails.as_view())
]