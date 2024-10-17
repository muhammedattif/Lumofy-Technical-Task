# Django Imports
from django.http import Http404

# REST Framework Imports
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# First Party Imports
from src.constants import NUMERIC_REGEX
from src.drive.models import UploadedFile
from src.drive.serializers.v1 import UploadedFileCreateSerializer, UploadedFileSerializer
from src.response_codes import GeneralCodes


class UploadedFilesViewSet(viewsets.GenericViewSet):

    lookup_value_regex = NUMERIC_REGEX
    queryset = UploadedFile.objects.order_by("-created_at")
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    #####

    def list(self, *args, **kwargs):
        """List Uploaded Files View"""

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is None:
            return Response(
                {
                    "code": GeneralCodes.SUCCESS,
                    "data": [],
                },
                status=status.HTTP_200_OK,
            )
        serializer = UploadedFileSerializer(page, context={"request": self.request}, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        """Retrieve an Uploaded File View"""

        try:
            uploaded_file = self.get_object()
        except Http404:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UploadedFileSerializer(uploaded_file, context={"request": request})
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        """Create Uploaded File View"""

        serializer = UploadedFileCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "code": serializer.error_code,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        uploaded_file = serializer.save()
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": UploadedFileSerializer(uploaded_file, context={"request": request}).data,
            },
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk, *args, **kwargs):
        """Delete an Uploaded File View"""

        try:
            uploaded_file = self.get_object()
        except Http404:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        uploaded_file.delete()
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
            },
            status=status.HTTP_200_OK,
        )
