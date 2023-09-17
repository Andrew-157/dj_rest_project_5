from rest_framework import serializers

from core.models import Course, Chapter, Section


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['url', 'id', 'name', 'published', 'updated']


class ChapterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chapter
        fields = ['url', 'id', 'number', 'title',
                  'introduction', 'published', 'updated',
                  'course']
