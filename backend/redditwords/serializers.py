from rest_framework import serializers
from .models import Redditwords

class RedditwordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Redditwords
		fields = ('id', 'title', 'description', 'completed')