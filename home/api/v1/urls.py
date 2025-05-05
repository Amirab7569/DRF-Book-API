from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'
router = DefaultRouter()
router.register("book", views.BooksModelViewSets, basename="book")
urlpatterns = router.urls

# urlpatterns = [
#     # path('book/', views.BookListCreate.as_view() ,name='api-book-list'),
#     # path('book/<int:pk>', views.BookDetails.as_view() ,name='api-book-update-get-delete'),
#     # path('book/', views.BookList.as_view() ,name='api-book-list'),
#     # path('book/<int:pk>/', views.BookDetails.as_view() ,name='api-book-details'),
#     # path('book/', views.BookList.as_view() ,name='api-book-list'),
#     # path('book/<int:pk>/', views.BookDetail.as_view() ,name='api-book-detail'),
# ]
