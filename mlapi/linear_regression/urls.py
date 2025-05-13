from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.PredictNextLoginLinearRegressionView.as_view(), name='linear-regression-predict'),
]
