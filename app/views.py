from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import status
# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        courses=CourseModel.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        data=request.data
        serializer=CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)



