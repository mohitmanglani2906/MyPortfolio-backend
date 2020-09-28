from rest_framework import serializers
from .models import Skills

class SkillsSerializers(serializers.ModelSerializer):
    skills_set = serializers.ListField()
    class Meta:
        model = Skills
        fields = '__all__'
