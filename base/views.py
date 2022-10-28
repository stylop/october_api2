from django.db.models import Q
from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer, AdvocateDetailSerializer
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .pagination import AdvocationLimitOffsetPagination, AdvocatePageNumberPagination
from .permissions import IsOwnerOrReadOnly







class AdvocateListAPIView(ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username','name']
    pagination_class =AdvocatePageNumberPagination



class AdvocateDetailAPIView(RetrieveAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateDetailSerializer
    lookup_field = 'username'






