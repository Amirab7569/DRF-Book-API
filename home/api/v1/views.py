from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Filtering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serilizers import BookSerializer
from ...models import Book
from .permissions import IsOwnerOrReadOnly


"""
# Class Base View : APIView

class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        srz_data = BookSerializer(books, many=True)
        return Response({"data" : srz_data.data})
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"New Book Created"},status=status.HTTP_201_CREATED)
        else:
            return Response({"data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    serializer_class = BookSerializer
    
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"data":"Not found book"})
    
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = self.serializer_class(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = self.serializer_class(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    '''
        if book.DoesNotExist:
            return Response({"data": f"{book} Does Not Exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BookSerializer(book, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": f"{book} info has updated"}, status=status.HTTP_200_OK)
            else:
                return Response({"data": f"{book} info does not updated"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({"detail" : f"item {book} deleted"}, status=status.HTTP_204_NO_CONTENT)
    '''

"""



"""
# Class Base View : generics
class BookList(ListCreateAPIView):
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    
    
class BookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.filter(is_published=True)
    serializer_class = BookSerializer
"""


"""
# viewset
class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
"""

"""
class BookList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""

class BooksModelViewSets(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author','is_published']
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    search_fields = ("is_published","title")
    ordering = ("-created_at")
    
    