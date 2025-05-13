<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.PredictNextLoginLinearRegressionView.as_view(), name='linear-regression-predict'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.PredictNextLoginLinearRegressionView.as_view(), name='linear-regression-predict'),
]
>>>>>>> 6c728f5 (Conflict Resolve)
