# Django Imports
from django.urls import reverse

# REST Framework Imports
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# First Party Imports
from src.courses.factories import CourseFactory, EnrollmentFactory, LessonFactory, StudentFactory, TeacherFactory
from src.courses.models import Course, Lesson
from src.courses.serializers.v1 import CourseSerializer, LessonSerializer
from src.response_codes import CoursesCodes, GeneralCodes


class CoursesViewSetTest(APITestCase):
    def setUp(self):
        self.teacher = TeacherFactory()
        self.student = StudentFactory()
        self.teacher_token, _ = Token.objects.get_or_create(user=self.teacher.user)
        self.student_token, _ = Token.objects.get_or_create(user=self.student.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.student_token.key}")

    #####

    def test_list_courses_success(self):
        """Test listing courses."""

        CourseFactory.create()
        url = reverse("courses:-list")
        response = self.client.get(url)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"], serializer.data)

    #####

    def test_retrieve_course(self):
        """Test retrieving a course."""
        course = CourseFactory.create()
        url = reverse("courses:-detail", kwargs={"pk": course.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["name"], course.name)

    def test_retrieve_non_existing_course(self):
        """Test retrieving a non-existing course."""
        url = reverse("courses:-detail", kwargs={"pk": 999})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["code"], GeneralCodes.NOT_FOUND)

    def test_create_course(self):
        """Test creating a course."""
        url = reverse("courses:-list")
        data = {
            "name": "New Course",
            "description": "Description of new course.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)

    def test_create_course_invalid(self):
        """Test creating a course with invalid data."""
        url = reverse("courses:-list")
        data = {
            "name": "",  # Invalid data
            "description": "Description of new course.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_course(self):
        """Test updating a course."""
        course = CourseFactory.create(teacher=self.teacher)
        url = reverse("courses:-detail", kwargs={"pk": course.id})
        data = {
            "name": "Updated Course Name",
            "description": "Updated description.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.put(url, data)

        course.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(course.name, "Updated Course Name")

    def test_update_course_invalid(self):
        """Test updating a course with invalid data."""
        course = CourseFactory.create(teacher=self.teacher)
        url = reverse("courses:-detail", kwargs={"pk": course.id})
        data = {
            "name": "",  # Invalid data
            "description": "Updated description.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_non_existing_course(self):
        """Test updating a non-existing course."""
        url = reverse("courses:-detail", kwargs={"pk": 999})
        data = {
            "name": "Updated Course Name",
            "description": "Updated description.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #####

    def test_delete_course(self):
        """Test deleting a course."""
        course = CourseFactory.create(teacher=self.teacher)
        url = reverse("courses:-detail", kwargs={"pk": course.id})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 0)  # Check if the course count is 0

    def test_delete_non_existing_course(self):
        """Test deleting a non-existing course."""
        course = CourseFactory.create()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        url = reverse("courses:-detail", kwargs={"pk": course.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #####

    def test_list_lessons(self):
        """Test listing lessons for a course."""
        lesson = LessonFactory.create()
        url = reverse("courses:-list-lessons", kwargs={"pk": lesson.course_id})
        response = self.client.get(url)

        lessons = Lesson.objects.filter(course_id=lesson.course_id)
        serializer = LessonSerializer(lessons, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"], serializer.data)

    def test_list_lessons_no_lessons(self):
        """Test listing lessons when there are no lessons."""
        course = CourseFactory.create()
        url = reverse("courses:-list-lessons", kwargs={"pk": course.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"], [])

    #####

    def test_create_lesson(self):
        """Test creating a lesson for a course."""
        course = CourseFactory.create(teacher=self.teacher)
        url = reverse("courses:-list-lessons", kwargs={"pk": course.id})
        data = {
            "name": "New Lesson",
            "description": "Description of new lesson.",
            "content": "content of new lesson.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.count(), 1)  # Check if lesson count has increased

    def test_create_lesson_invalid(self):
        """Test creating a lesson with invalid data."""
        course = CourseFactory.create(teacher=self.teacher)
        url = reverse("courses:-list-lessons", kwargs={"pk": course.id})
        data = {
            # "name": "New Lesson", Invalid data
            "description": "Description of new lesson.",
            "content": "content of new lesson.",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #####

    def test_delete_lesson(self):
        """Test deleting a lesson."""
        course = CourseFactory.create(teacher=self.teacher)
        lesson = LessonFactory.create(course=course)
        url = reverse("courses:-retrieve-lesson", kwargs={"pk": course.id, "lesson_id": lesson.id})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.count(), 0)  # Check if lesson count is 0

    def test_delete_non_existing_lesson(self):
        """Test deleting a non-existing lesson."""
        course = CourseFactory.create()
        lesson = LessonFactory.create(course=course)
        url = reverse("courses:-retrieve-lesson", kwargs={"pk": course.id, "lesson_id": lesson.id})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.teacher_token.key}")
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    ####

    def test_track_lesson(self):
        """Test tracking a lesson."""
        enrollment = EnrollmentFactory(student=self.student)
        lesson = LessonFactory.create(course=enrollment.course)
        url = reverse("courses:-track-lesson", kwargs={"pk": enrollment.course_id, "lesson_id": lesson.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_track_lesson_not_enrolled(self):
        """Test tracking a lesson when the student is not enrolled."""
        lesson = LessonFactory.create()
        url = reverse("courses:-track-lesson", kwargs={"pk": lesson.course_id, "lesson_id": lesson.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["code"], CoursesCodes.NOT_ENROLED)

    def test_track_non_existing_lesson(self):
        """Test tracking a non-existing lesson."""
        url = reverse("courses:-track-lesson", kwargs={"pk": 999, "lesson_id": 999})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["code"], GeneralCodes.NOT_FOUND)
