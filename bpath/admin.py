from django.contrib import admin
from .models import Respite
from .models import Post
from .models import Comment


admin.site.register(Respite)
admin.site.register(Post)
admin.site.register(Comment)
