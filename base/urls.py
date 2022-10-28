from django.urls import path
# from . import views
from .views import AdvocateListAPIView,AdvocateDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)

urlpatterns = [
    # path('', views.endpoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('advocates/', views.advocate_list, name='advocates'),
    path('advocates/', AdvocateListAPIView.as_view(), name='advocates'),
    path('advocates/<str:username>/', AdvocateDetailAPIView.as_view()),
    # path('advocates/<str:username>/', AdvocateDetail.as_view()),
    # path('companies/', views.companies_list)
]