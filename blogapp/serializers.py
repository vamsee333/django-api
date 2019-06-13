from .models import Blogpost
from rest_framework import serializers

class Blogpostserializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Blogpost
        fields=[
            'url',
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]
        #read_only_fields=['user']

    def get_url(self,obj):
        return obj.get_api_url()


    def validate_title(self,value):
        qs=Blogpost.objects.filter(title__iexact=value)
        if self.instance:
            qs=qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('already exists')
        return value
