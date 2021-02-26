from rest_framework import viewsets, permissions
from .serializers import TuteeSerializer, TutorSerializer
from .models import Tutor, Tutee


class TutorAPI(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "full_name"


class TuteeAPI(viewsets.ModelViewSet):
    queryset = Tutee.objects.all()
    serializer_class = TuteeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "full_name"
