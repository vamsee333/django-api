from django.shortcuts import render
from rest_framework import generics,mixins
# Create your views here.
from .serializers import Blogpostserializer
from .models import Blogpost
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):     #retrive - read update -write Destroy -delete
    lookup_field='pk'
    serializer_class=Blogpostserializer
    permission_classes=[IsOwnerOrReadOnly]

    def get_queryset(self):
        return Blogpost.objects.all()

    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}




class BlogPostAPIView(mixins.CreateModelMixin,mixins.UpdateModelMixin, generics.ListAPIView):
    lookup_field='pk'
    serializer_class=Blogpostserializer

    def get_queryset(self):
        qs=Blogpost.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)|Q(content__icontains=query))
        return qs


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


    # get serializer context is the predefined method that is used to get the request and send to serializer
    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}
