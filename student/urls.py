from django.urls import path

from student import views

urlpatterns = [

    #----- API view------------
    path('', views.index),
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>/', views.StudentView.as_view()),

    #-------class based views-----------
    # path('books/', views.BookApiView.as_view()),
    # path('books/create/', views.BookCreateApiView.as_view()),
    # path('books/<int:pk>/', views.BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete/', views.BookDeleteApiView.as_view()),
    # path('books/update/<int:pk>/', views.BookUpdateApiView.as_view()),



    #--------------------------
    path('books/', views.BookListCreateView.as_view()),
    path('book_change/<int:pk>/', views.BookDetailUpdateDestoyView.as_view()),

    #--------function based views-----------
    path('book_list/', views.book_list_view),
    path('book_detail/<int:pk>/', views.book_detail_view),
    path('book_delete/<int:pk>/delete/', views.book_delete),
]