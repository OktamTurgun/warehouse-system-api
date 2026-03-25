from django.urls import path
from .views import CalculateMaterialsView

urlpatterns = [
  path("calculate/", CalculateMaterialsView.as_view(), name="calculate"),
]