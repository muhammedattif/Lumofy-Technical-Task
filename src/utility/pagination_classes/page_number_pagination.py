# Python Standard Library Imports
from collections import OrderedDict

# REST Framework Imports
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# First Party Imports
from src.response_codes import GeneralCodes


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("code", GeneralCodes.SUCCESS),
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("data", data),
                ],
            ),
        )
