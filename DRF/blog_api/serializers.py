#what data you want to serilaize

from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #what data is going to manage
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
