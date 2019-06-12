from django.shortcuts import render
from rest_framework import generics,mixins
# Create your views here.
from .serializers import Blogpostserializer
from .models import Blogpost

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):     #retrive - read update -write Destroy -delete
    lookup_field='pk'
    serializer_class=Blogpostserializer

    def get_queryset(self):
        return Blogpost.objects.all()



class BlogPostAPIView(mixins.CreateModelMixin,mixins.UpdateModelMixin, generics.ListAPIView):
    lookup_field='pk'
    serializer_class=Blogpostserializer

    def get_queryset(self):
        return Blogpost.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)