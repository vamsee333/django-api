from rest_framework import serializers
from .models import poll,Choice,Vote

class voteserializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class choiceserializer(serializers.ModelSerializer):
    votes=voteserializer(many=True, required=False)
    class Meta:
        model=Choice
        fields='__all__'


class pollserializer(serializers.ModelSerializer):
    choices=choiceserializer(many=True,read_only=True,required=False)
    class Meta:
        model=poll
        fields='__all__'


