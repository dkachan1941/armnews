from django.contrib import admin

from .models import News
from .models import Comment

admin.site.register(News)
admin.site.register(Comment)