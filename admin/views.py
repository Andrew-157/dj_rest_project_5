from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from core.models import Course, Chapter, Section
from .serializers import CourseSerializer, ChapterSerializer, SectionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ChapterSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SectionSerializer
