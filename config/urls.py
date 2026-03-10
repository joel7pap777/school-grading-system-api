from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet
from teachers.views import TeacherViewSet
from classes.views import ClassViewSet
from results.views import ResultViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'results', ResultViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]