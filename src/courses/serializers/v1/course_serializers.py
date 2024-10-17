# REST Framework Imports
from rest_framework import serializers

# First Party Imports
from src.courses.models import Course
from src.response_codes import CoursesCodes
from src.utility.serializers import SerializerErrorCodesMixin

from .lesson_serializers import LessonSerializer


class CourseCreateUpdateSerializer(SerializerErrorCodesMixin, serializers.ModelSerializer):

    ERROR_CODES_DICT = {
        "name": CoursesCodes.INVALID_NAME,
        "description": CoursesCodes.INVALID_DESCRIPTION,
    }

    class Meta:
        model = Course
        fields = ["name", "description"]

    def create(self, validated_data):
        return Course.create(**validated_data)


class CourseSerializer(serializers.ModelSerializer):

    # NOTE: It will lead to a bad performance if the course has a lot of lessons
    # So the best practice here is to remove it and implement a paginated API to retrieve a list of lessons in the course
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "description", "teacher", "created_at", "lessons"]
