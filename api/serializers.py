from .models import Tutor, Tutee
from rest_framework import serializers


class TutorSerializer(serializers.ModelSerializer):
    tutees = serializers.SlugRelatedField(queryset=Tutee.objects.all(), slug_field="full_name", many=True)

    class Meta:
        model = Tutor
        fields = ['id', 'full_name', 'email', 'notes', 'tutees']


class TuteeSerializer(serializers.ModelSerializer):
    tutor = serializers.SlugRelatedField(queryset=Tutor.objects.all(), slug_field="full_name")

    class Meta:
        model = Tutee
        fields = ['id', 'full_name', 'email', "tutor", "subjects"]
