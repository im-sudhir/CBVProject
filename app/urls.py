from django.urls import path,include
# from .views import CourseListView,CourseDetailView
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router=DefaultRouter()
router.register('courses',CourseViewSet, basename='course')

urlpatterns=[
    # path('courses', CourseListView.as_view()),
    # path('courses/<int:pk>', CourseDetailView.as_view()),
    path('',include(router.urls)),

]