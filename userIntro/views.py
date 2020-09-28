from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IntroSerializers
from .models import Intro

# Create your views here.

class UserInroduction(APIView):

    def get(self, request):

        userIntro = Intro.objects.all()
        serializer = IntroSerializers(userIntro, many=True)
        return Response({ "success": True, "data": serializer.data})

    def post(self, request):
        serializer = IntroSerializers(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data})

        return Response({"success": False, "data": serializer.error_messages})


