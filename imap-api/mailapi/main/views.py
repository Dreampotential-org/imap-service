from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from main.serializers import MailSerializer
from main.models import Mail


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all().order_by('-id')
    serializer_class = MailSerializer
