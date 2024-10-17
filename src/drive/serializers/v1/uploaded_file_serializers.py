# REST Framework Imports
from rest_framework import serializers

# First Party Imports
from src.drive.models import UploadedFile
from src.response_codes import UploadedFilesCodes
from src.utility.serializers import SerializerErrorCodesMixin


class UploadedFileSerializer(serializers.ModelSerializer):

    size_unit = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ["id", "file", "type", "size", "size_unit", "created_at"]

    def get_size_unit(self, obj):
        return UploadedFile.SIZE_UNIT


class UploadedFileCreateSerializer(SerializerErrorCodesMixin, serializers.ModelSerializer):

    ERROR_CODES_DICT = {
        "file": UploadedFilesCodes.INVALID_FILE,
    }

    class Meta:
        model = UploadedFile
        fields = ["file"]

    def create(self, validated_data):
        # We overrided this method to use the .create() method created in the model
        return UploadedFile.create(**validated_data)
