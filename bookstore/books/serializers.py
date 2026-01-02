from rest_framework import serializers
from .models import Book, Order, Category, Tag, Review  
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']


class BookListSerializer(serializers.ModelSerializer):
    #A read only field that represents its targets using their plain string representation
    category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'stock', 'is_available', 'category', 'created_at']


class ReviewSerilaizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True, required=False)
    comment = serializers.CharField()
    rating = serializers.IntegerField()
    class Meta:
        model = Review
        fields = ['id','username','comment','rating','book','created_at']
        read_only_fields = ['username']

    def validate_rating(self,value):
        if value > 5:
            raise serializers.ValidationError("Rating must be inside 1 to 5")
        return value


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerilaizer(many = True, read_only=True)
    #category = CategorySerializer(read_only=True) it will create a nested serializer
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    avg_rating = serializers.FloatField(read_only=True)
    total_reviews = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'published_date', 'price', 'stock','is_available', 'tags' ,'category','reviews','avg_rating','total_reviews']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'book',
            'quantity',
            'total_price',
            'status',
            'order_date'
        ]
