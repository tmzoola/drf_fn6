from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Student,Book
from .serailizers import StudentSerializer,BookSerializer





#-------------------------------------------------
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailUpdateDestoyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#---------------------------------------------------------


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#----------------------------------------------------------------


@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail_view(request,pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['GET'])
def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response({"message":"book deletedd"})



#----------------------------------------------------------------











def index(request):
    return HttpResponse("Hello World")


class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()

        return Response({"studens": StudentSerializer(students, many=True).data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #validated_data
        serializer.save()

        return Response({"studens": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if not pk:
            return Response({"error": "pk required"})

        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "student does not exist"})

        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"studens": serializer.data})
