from .models import Blogpost
from rest_framework import serializers

class Blogpostserializer(serializers.ModelSerializer):
    class Meta:
        model=Blogpost
        fields=[
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]
        #read_only_fields=['user']

    def validate_title(self,value):
        qs=Blogpost.objects.filter(title__iexact=value)
        if self.instance:
            qs=qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('already exists')
        return value