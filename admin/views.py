from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from core.models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer
