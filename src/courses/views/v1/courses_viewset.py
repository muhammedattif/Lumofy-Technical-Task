# Django Imports
from django.http import Http404

# REST Framework Imports
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# First Party Imports
from src.constants import NUMERIC_REGEX
from src.courses.models import Course, Lesson, Student
from src.courses.permissions import StudentPermission, TeacherPermission
from src.courses.serializers.v1 import (
    CourseCreateUpdateSerializer,
    CourseSerializer,
    LessonCreateSerializer,
    LessonSerializer,
)
from src.response_codes import CoursesCodes, GeneralCodes


class CoursesViewSet(viewsets.GenericViewSet):

    lookup_value_regex = NUMERIC_REGEX
    queryset = Course.objects.order_by("-created_at")
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, TeacherPermission | StudentPermission]

    def get_permissions(self):
        if self.action in ["create", "update", "destroy", "create_lesson", "delete_lesson"]:
            return [IsAuthenticated(), TeacherPermission()]
        return super().get_permissions()

    #####

    def list(self, *args, **kwargs):
        """List Courses View"""

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
        serializer = CourseSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        """Retrieve a Course View"""

        try:
            course = self.get_object()
        except Http404:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CourseSerializer(course)
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        """Create Course View"""

        serializer = CourseCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "code": serializer.error_code,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        course = serializer.save(teacher=request.user.teacher)
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": CourseSerializer(course).data,
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk, *args, **kwargs):
        """Update Course View"""

        try:
            course = Course.objects.get(id=pk, teacher=request.user.teacher)
        except Course.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CourseCreateUpdateSerializer(
            data=request.data,
            instance=course,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(
                {
                    "code": serializer.error_code,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        course = serializer.save()
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": CourseSerializer(course).data,
            },
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, pk, *args, **kwargs):
        """Delete Course View"""

        try:
            course = Course.objects.get(id=pk, teacher=request.user.teacher)
        except Course.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        course.delete()
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
            },
            status=status.HTTP_200_OK,
        )

    # Lessons

    @action(
        methods=["GET"],
        detail=True,
        url_path="lessons",
    )
    def list_lessons(self, request, pk, *args, **kwargs):
        """Lessons List View"""

        lessons = Lesson.objects.filter(course_id=pk).order_by("created_at")

        page = self.paginate_queryset(lessons)
        if page is None:
            return Response(
                {
                    "code": GeneralCodes.SUCCESS,
                    "data": [],
                },
                status=status.HTTP_200_OK,
            )
        serializer = LessonSerializer(lessons, many=True)
        return self.get_paginated_response(serializer.data)

    @list_lessons.mapping.post
    def create_lesson(self, request, pk):
        """Create Lesson View"""
        try:
            course = self.get_queryset().get(pk=pk, teacher=request.user.teacher)
        except Course.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = LessonCreateSerializer(
            data=request.data,
        )
        if not serializer.is_valid():
            return Response(
                {
                    "code": serializer.error_code,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        lesson = serializer.save(course=course)
        return Response(
            {"code": GeneralCodes.SUCCESS, "data": LessonSerializer(lesson).data},
            status=status.HTTP_200_OK,
        )

    @action(
        methods=["GET"],
        detail=True,
        url_path=r"lessons/(?P<lesson_id>\d+)",
    )
    def retrieve_lesson(self, request, pk, lesson_id, *args, **kwargs):
        """Lesson Retrieve View"""

        try:
            lesson = Lesson.objects.get(pk=lesson_id, course_id=pk)
        except Lesson.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "code": GeneralCodes.SUCCESS,
                "data": LessonSerializer(lesson).data,
            },
            status=status.HTTP_200_OK,
        )

    @retrieve_lesson.mapping.delete
    def delete_lesson(self, request, pk, lesson_id):
        """Delete Lesson View"""
        try:
            lesson = Lesson.objects.get(pk=lesson_id, course_id=pk, course__teacher=request.user.teacher)
        except Lesson.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        lesson.delete()
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
            },
            status=status.HTTP_200_OK,
        )

    @action(
        methods=["POST"],
        detail=True,
        url_path=r"lessons/(?P<lesson_id>\d+)/track",
        permission_classes=[IsAuthenticated, StudentPermission],
    )
    def track_lesson(self, request, pk, lesson_id, *args, **kwargs):
        """Lesson Track View"""

        try:
            lesson = Lesson.objects.get(pk=lesson_id, course_id=pk)
        except Lesson.DoesNotExist:
            return Response(
                {
                    "code": GeneralCodes.NOT_FOUND,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        student: Student = request.user.student
        if not student.get_enrolled_courses().filter(id=lesson.course_id).exists():
            return Response(
                {
                    "code": CoursesCodes.NOT_ENROLED,
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        lesson.track(student=student)
        return Response(
            {
                "code": GeneralCodes.SUCCESS,
            },
            status=status.HTTP_200_OK,
        )
