# 1. SQL and Database Design

## Database Schema

**1- Entities:**
- Course: Each course will have multiple lessons and be assigned to teachers.
- Student: Students can enroll in multiple courses.
- Teacher: Teachers can teach multiple courses.
- Lesson: Each course contains multiple lessons.
- Progress: Tracks the completion status of lessons by students.

**Example schema:**

```bash

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE REFERENCES users(id),
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE REFERENCES users(id),
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    teacher_id INT REFERENCES teachers(id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    content TEXT
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)  # -- Ensures a student can enroll in a course only once
);

CREATE TABLE lesson_progress (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT FALSE,
    UNIQUE (student_id, lesson_id)  # -- Ensures a student's progress for a lesson is tracked only once
);
```

**2- SQL Queries:**

1. Retrieve all students enrolled in a given course:
```sql
SELECT students.name
FROM students
JOIN enrollments ON students.id = enrollments.student_id
WHERE enrollments.course_id = <course_id>;
```

2. Get the progress of each student per course based on lesson completion:
```sql
SELECT students.name, lessons.title, lesson_progress.completion_status
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN lessons ON lessons.course_id = enrollments.course_id
JOIN lesson_progress ON lesson_progress.lesson_id = lessons.id
WHERE enrollments.course_id = <course_id>;
```

3.Retrieve the courses a teacher is assigned to:
```sql
SELECT courses.title
FROM courses
WHERE courses.teacher_id = <teacher_id>;
```


------------

# 2. Python/Django Problem

- [Files Uploads](/src/drive/)
