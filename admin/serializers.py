from rest_framework import serializers

from core.models import Course, Chapter, Section


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'published']


class CreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'published', 'updated']