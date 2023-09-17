from rest_framework import serializers

from core.models import Course, Chapter, Section


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['url', 'id', 'name', 'published', 'updated']
