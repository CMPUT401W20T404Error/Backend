from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import RedditwordsSerializer      # add this
from .models import Redditwords                    # add this

class RedditwordsView(viewsets.ModelViewSet):       # add this
	serializer_class = RedditwordsSerializer          # add this
	queryset = Redditwords.objects.all()              # add this