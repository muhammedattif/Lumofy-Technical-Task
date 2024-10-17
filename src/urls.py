"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django Imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# REST Framework Imports
from rest_framework.authtoken import views

# First Party Imports
from src.courses.urls import courses_router_v1
from src.drive.urls import uploaded_files_router_v1

admin_urls = [
    path("admin/", admin.site.urls),
]

third_parties_urls = [
    path("i18n/", include("django.conf.urls.i18n")),
]

apis_urls = [
    # Auth APIs V1
    # NOTE: I always implement a custom auth but used it for quick implementation
    path("api/v1/obtain-token-auth/", views.obtain_auth_token),
    # Drive APIs v1
    path("api/v1/drive/", include((uploaded_files_router_v1.urls, "drive"), namespace="drive-apis-v1")),
    # Drive APIs v1
    path("api/v1/courses/", include((courses_router_v1.urls, "courses"), namespace="courses-apis-v1")),
]

normal_url_patterns = []

if settings.DEBUG:
    normal_url_patterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    normal_url_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = admin_urls + third_parties_urls + apis_urls + normal_url_patterns
admin.site.index_title = settings.SITE_INDEX_TITLE
admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
