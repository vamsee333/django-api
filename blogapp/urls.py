from django.urls import path
from .views import BlogPostRudView,BlogPostAPIView

urlpatterns=[
    path('blog/<int:pk>/',BlogPostRudView.as_view(),name='blog-post'),
    path('bloglist/',BlogPostAPIView.as_view(),name='blog-list')

]