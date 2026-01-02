from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveAPIView
from .models import Review, Book, Category, Order
from .serializers import ReviewSerilaizer, BookDetailSerializer,CategorySerializer, OrderSerializer,BookListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Count, Avg
# Create your views here.

class CategoryListApi(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ReviewListApi(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerilaizer
    permission_classes = [IsAuthenticated] # Ensures a user is logged in

    def perform_create(self, serializer):
        # This method is called when valid data is posted.
        # It injects the currently authenticated user before saving the new Review instance.
        serializer.save(user=self.request.user)

class BookListApi(ListAPIView):
    queryset = Book.objects.filter(is_available = True).order_by("-created_at")
    serializer_class = BookListSerializer
    pagination_class = LimitOffsetPagination
    
class BookDetailListApi(RetrieveAPIView):

    queryset = Book.objects.filter(is_available = True).annotate(avg_rating = Avg('reviews__rating'),total_reviews = Count('reviews'))
    serializer_class = BookDetailSerializer

class OrderListCreateApi(ListCreateAPIView):
    
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        books = serializer.validated_data['book']
        quantity = serializer.validated_data['quantity']
        total_price = sum(book.price for book in books) * quantity
        serializer.save(user=self.request.user, total_price=total_price)

