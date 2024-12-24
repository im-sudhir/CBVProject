from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.shortcuts import get_object_or_404
# Create your views here.


#NOTE: Used ModelViewSet for CRUD Operations.
class CourseViewSet(ModelViewSet):
    queryset=CourseModel.objects.all()
    serializer_class=CourseSerializer


#NOTE:User Viewset for CRUD operations
'''class CourseViewSet(ViewSet):
    def list(self,request):
        courses=CourseModel.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        try:
            course=CourseModel.objects.get(pk=pk)
        except CourseModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def destroy(self,request,pk):
        queryset=CourseModel.objects.all()
        course= get_object_or_404(queryset,pk=pk)
        course.delete()
        return Response("{'messge':'object is deleted.'}", status=status.HTTP_200_OK)'''


#NOTE:Used Mixins and GenericAPIView for CRUD operations
'''class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=CourseModel.objects.all()
    serializer_class=CourseSerializer
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)'''


#NOTE: Used generics ListCreateView and RetrieveUpdateDestroyAPIView for CRUD Opeations.
'''class CourseListView(generics.ListCreateAPIView):
    serializer_class=CourseSerializer
    queryset=CourseModel.objects.all()


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CourseSerializer
    queryset=CourseModel.objects.all()
'''

'''class CourseDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset=CourseModel.objects.all()
    serializer_class=CourseSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)'''


#NOTE:Used Standard APIView class for CRUD operations.
'''class CourseListView(APIView):
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

class CourseDetailView(APIView):
    def get(self,request, pk):
        try:
            course=CourseModel.objects.get(pk=pk)
            serializer=CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CourseModel.DoesNotExist:
            return Response({"message":"Not Found"},status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            # Retrieve the existing instance
            course = CourseModel.objects.get(pk=pk)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        # Pass the existing instance to the serializer
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        try:
            course = CourseModel.objects.get(pk=pk)
            course.delete()
            return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except CourseModel.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)'''

