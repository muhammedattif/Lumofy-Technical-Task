# Lumofy Technical Task

[![python](https://img.shields.io/badge/Python-v3.8-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)  [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Table of Contents
- [Overview](#Overview)
- [Tech Stack](#Tech-Stack)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Features](#Features)
    - [Section 1: General Coding & Problem Solving](docs/general_coding.md)
    - [Section 2: API Design & Implementation](docs/api_design.md)
    - [Section 3: Code Review & Engineering Mindset](docs/code_review.md)
    - [Section 4: React Integration](docs/react_integration.md)
- [Documentation](#Documentation)
- [Assumptions and Design Decisions](#Assumptions-and-Design-Decisions)
- [TODO](#TODO)

# Learning Management System (LMS) API

## Overview

This project is a Learning Management System (LMS) API built using Django and Django REST Framework, with PostgreSQL as the database. The API supports managing courses, lessons, and student progress, along with file uploads.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Frontend**: Basic React

### Prerequisites

- Python 3.8
- Django
- Django REST Framework
- PostgreSQL
- react.js (for React component)


## Installation

- Create the `.env` file by copying the data from `sample.env`
- `docker compose build` : you need this command just for the first time to build your dockerfile
- `docker-compose build --build-arg PLATFORM=linux/arm64` : you need this command just for the first time to build your dockerfile if you are using an m2 Mac device
- `docker compose up`: use this command each time you want to run the container
- `docker compose exec app <command>` : to run a specific command at the container, for example, to access the Django shell

```bash
docker compose exec app python manage.py shell_plus
```


## Features

1. [Section 1: General Coding & Problem Solving](docs/general_coding.md)
   - Design a database schema for a Learning Management System (LMS)
   - Users can upload files and access them later.
   - Files are validated by type and size.

2. [Section 2: API Design & Implementation](docs/api_design.md)
   - Create, update, delete, and retrieve courses.
   - Add and remove lessons from courses.
   - Track student progress for each lesson.

3. [Section 3: Code Review & Engineering Mindset](docs/code_review.md)

4. [Section 4: React Integration](docs/react_integration.md)
    - Implement a simple React component to integrate with the courses API

## Documentation
[Postman Documentation Link](https://documenter.getpostman.com/view/16211738/2sAXxV7W1D)


## Assumptions-and-Design-Decisions
**Project Structure**: single-app Django project

**Unified Response Templates**: Used the response codes technique instead of returning any text messages to the front end, Using codes in APIs enhances clarity, efficiency, and consistency, making it easier for both developers and clients to work with the API effectively. Combining codes with well-structured messages can provide the best of both worlds, ensuring robust error handling and clear communication.

**Abstract Model**: Create an abstract model containing the common fields that will be used across all the models.

**Custom User Model**: Overriding the Django user model provides a powerful way to tailor user management to our application's specific needs. It enhances data integrity, usability, and flexibility while integrating seamlessly with Django's built-in features. This approach ultimately leads to a more robust and maintainable application.

## TODO

- **APIs Rate Limiting**
- **Logging**
- **APIs to the students to see their enrolled courses**
- **Add more Filters to the Courses APIs**
- **Enable the students to see the progress of their enrolled courses**
- **Write test cases for the followng: serializers, Signals, Admin, Utility functions and validators**
