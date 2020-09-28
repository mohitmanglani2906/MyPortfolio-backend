from rest_framework import serializers
from .models import Intro

class IntroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intro
        fields = ('profilePic', 'introduction')