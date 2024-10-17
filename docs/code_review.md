# 1. Code Review Task

## Issues Identified

**Security Vulnerability:**

- Plaintext Password: The password is stored as plaintext. This poses a significant security risk because if the database is compromised, all passwords are exposed.

- Email Validation: The code does not validate the email format, which can lead to invalid entries.

**Performance:**

- Database Calls: The code performs a database call for user creation without checking for existing users. This can lead to duplicate users if the username or email is already taken.

**Maintainability:**
- Hardcoded Responses: The response message is hardcoded. For better maintainability, consider using Django's built-in messaging framework or serializers.

- Lack of Error Handling: There is no error handling for cases where user creation fails.

## Refactored Code

Here’s a refactored version of the register_user function addressing the identified issues:

```python
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

EMAIL_ALREADY_EXISTS = "001"
USERNAME_ALREADY_EXISTS = "002"
INVALID_EMAIL_FORMAT = "003"
USER_CREATED = "004"

@require_POST  # Ensures that only POST requests are processed
def register_user(request):

    # WHen working with APIs We usually create an input serializer to validate all incoming data

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    try:
        # Validate email format
        validate_email(email)
    except ValidationError:
        return JsonResponse({"code": INVALID_EMAIL_FORMAT}, status=400)

    # Check if the username or email already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({"code": USERNAME_ALREADY_EXISTS}, status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({"code": EMAIL_ALREADY_EXISTS}, status=400)

    # Hash the password before saving
    user = User(
        username=username,
        email=email,
        password=make_password(password)  # Hash the password
    )
    user.save()

    return JsonResponse({"code": USER_CREATED}, status=201)
```

**Improvements Made**
**Security:**
- Used make_password to hash the password before saving it, enhancing security.
- Added email validation using Django's validate_email function.

**Performance:**
- Added checks for existing usernames and emails before creating a new user, preventing unnecessary database calls and duplicate users.

**Maintainability:**
- Used decorators like @require_POST to ensure the function only handles POST requests.
- Added structured error handling to provide appropriate response code for different failure scenarios, improving clarity and maintainability.
