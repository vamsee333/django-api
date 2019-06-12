from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import poll,Choice,Vote
#required for REST API's
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import pollserializer,choiceserializer,voteserializer
from rest_framework import generics,status
from rest_framework import viewsets


# Create your views here.
# def polls_list(request):
#     obj=poll.objects.all()
#     data={"results":list(obj.values("question","created_by","pub_date"))}
#     return JsonResponse(data)
#
#
#
#
#
# def polls_details(request,pk):
#     obj=poll.objects.get(id=pk)
#     data={"result":{
#         "question":obj.question,
#         "created by":obj.created_by.username,
#         "pub_date":obj.pub_date
#     }}
#     return JsonResponse(data)




# new API models

# class polllist(APIView):
#     def get(self,request):
#         polls=poll.objects.all()
#         data=pollserializer(polls,many=True).data
#         return Response(data)
#
# class polldetail(APIView):
#     def get(self,request,pk):
#         polls=poll.objects.get(id=pk)
#         data=pollserializer(polls).data
#         return Response(data)




class polllist(generics.ListCreateAPIView):
    queryset=poll.objects.all()
    serializer_class=pollserializer

class polldetail(generics.RetrieveDestroyAPIView):
    queryset=poll.objects.all()
    serializer_class=pollserializer


#replacing above two views with singel view
# class PollViewSet(viewsets.ModelViewSet):
#     queryset=poll.objects.all()
#     serializer_class=pollserializer


class choicelist(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset=Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset
    serializer_class=choiceserializer


class votelist(APIView):
    def post(self,request,pk,choice_pk):
        voted_by=1
        data={'choice':choice_pk,'poll':pk,'voted_by':voted_by}
        serializer=voteserializer(data=data)
        if serializer.is_valid():
            Vote=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
