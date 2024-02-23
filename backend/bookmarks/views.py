from django.shortcuts import render
from rest_framework import viewsets
from .models import Bookmark
from .serializers import BookmarkSerializer

# Create your views here.
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer