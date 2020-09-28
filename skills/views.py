from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SkillsSerializers
from .models import Skills


# Create your views here.

class UserSkills(APIView):

    def get(self, request):
        #skills = Skills.objects.all()
        skill =Skills.objects.filter(id=request.data["id"])
        serializer = SkillsSerializers(skill, many=True)
        return Response({"success": True, "data": serializer.data})


    def post(self,request):
        serializer = SkillsSerializers(data= request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data})

        return Response({"success": False, "data": serializer.error_messages})