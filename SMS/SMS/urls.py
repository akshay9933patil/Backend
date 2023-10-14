from django.contrib import admin
from django.urls import path, include
from Student.views import SubjectsView, StudentView
from rest_framework.routers import DefaultRouter

student_router = DefaultRouter()
subject_router = DefaultRouter()

student_router.register('student',StudentView)
subject_router.register('subject',SubjectsView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Auth.urls')),
    path('student1/', include('Student.urls')),
    path('student/', include(student_router.urls)),
    path('subject/', include(subject_router.urls)),
]
