from rest_framework.pagination import  LimitOffsetPagination, PageNumberPagination



class AdvocationLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class AdvocatePageNumberPagination(PageNumberPagination):
    page_size = 5
