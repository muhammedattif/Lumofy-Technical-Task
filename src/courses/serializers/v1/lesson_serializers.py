# REST Framework Imports
from rest_framework import serializers

# First Party Imports
from src.courses.models import Lesson
from src.response_codes import LessonsCodes
from src.utility.serializers import SerializerErrorCodesMixin


class LessonCreateSerializer(SerializerErrorCodesMixin, serializers.ModelSerializer):

    ERROR_CODES_DICT = {
        "name": LessonsCodes.INVALID_NAME,
        "description": LessonsCodes.INVALID_DESCRIPTION,
        "content": LessonsCodes.INVALID_CONTENT,
    }

    class Meta:
        model = Lesson
        fields = ["name", "description", "content"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "content", "created_at"]
