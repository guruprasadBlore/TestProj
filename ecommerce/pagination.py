from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination
)

class MyCustomPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 4


class CustomPagePaginator(PageNumberPagination):
    page_size = 2