from django.urls import path,include
from .views import BookListcreate,BookDetail,UploadCover

urlpatterns = [
    path('api/books/',BookListcreate.as_view()),
    path('api/books/<int:pk>/',BookDetail.as_view()),
    path('api/books/<int:pk>/upload-cover/',UploadCover.as_view())
]
