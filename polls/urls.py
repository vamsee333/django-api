from django.urls import path,re_path
from .views import polllist,polldetail,choicelist,votelist

#import statements for viewsets and routers
from rest_framework.routers import DefaultRouter


#
# router=DefaultRouter()
# router.register('polls',PollViewSet,base_name='polls')

urlpatterns=[
    # path('polls/',polls_list,name='pollslist'),
    # path('polldetails/<int:pk>',polls_details,name='pollsdetails')
    path('polls/',polllist.as_view(),name='pollslist'),
    path('polls/<int:pk>',polldetail.as_view(),name='pollsdetails'),
    path('polls/<int:pk>/choice/',choicelist.as_view(),name='choice details'),
    path('polls/<int:pk>/choice/<int:choice_pk>/vote',votelist.as_view(),name='vote details')


]

# urlpatterns+=router.urls
