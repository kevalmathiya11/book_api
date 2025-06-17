from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .decorators import require_api_key
from rest_framework import status
from django.shortcuts import get_object_or_404

class BookListcreate(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many = True)
        return Response(serializer.data)
    
    @require_api_key
    def post(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
class BookDetail(APIView):
    def get(self,request,pk):
        book = get_object_or_404(Book,pk = pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    @require_api_key
    def put(self,request,pk):
        book = get_object_or_404(Book ,pk = pk)
        serializer = BookSerializer(book,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= 400)
    
    @require_api_key
    def delete(self,request,pk):
        book = get_object_or_404(Book,pk = pk)
        book.delete()
        return Response(status=204)
    
class UploadCover(APIView):

    @require_api_key
    def post(self,request,pk):
        book = get_object_or_404(Book,pk=pk)
        file = request.FILES.get('cover')

        if not file:
            return Response({"error":"NO_FILE","message":"No file uploaded "},status=400)
        
        if file.content_type not in ['image/png','image/jpg','image/webp']:
            return Response({"error":"INVALID_FILE_TYPE","message":"Only PNG , JPG and WEBP files are allowed"},status= 400)
        
        if file.size > 2 * 1024 * 1024 :
            return Response({"error":"FILE_TOO_LARGE","message":"File size exceeds 2MB limit"},status=413)

        book.cover_image = file
        book.save()

        return Response({
            "id" : book.id,
            "title":book.title,
            "cover_url" : request.build_absolute_uri(book.cover_image.url),
            "message": "Cover Uploaded Successfully"
        })    


