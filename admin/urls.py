from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'chapters', views.ChapterViewSet, basename='chapter')
router.register(r'sections', views.SectionViewSet, basename='section')

urlpatterns = [
    path('', include(router.urls))
]
