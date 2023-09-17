from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from core.models import Course, Chapter
from .serializers import CourseSerializer, ChapterSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ChapterSerializer