
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookDetailListApi,BookListApi,CategoryListApi,BookDetailSerializer,OrderListCreateApi,ReviewListApi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListApi.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailListApi.as_view(), name='book-detail'),
    path('reviews/', ReviewListApi.as_view(), name='review-list'),
    path('categories/', CategoryListApi.as_view(), name='category-list'),
    path('orders/', OrderListCreateApi.as_view(), name='order-list'),
    path('api-auth/', include('rest_framework.urls')),
]
