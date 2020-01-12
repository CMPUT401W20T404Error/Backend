from django.contrib import admin

# Register your models here.
from .models import Redditwords # add this

class RedditwordsAdmin(admin.ModelAdmin):  # add this
	list_display = ('title', 'description', 'completed') # add this
	# Register your models here.
admin.site.register(Redditwords, RedditwordsAdmin) # add this
