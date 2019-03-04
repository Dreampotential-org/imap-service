from rest_framework import viewsets
from main.serializers import MailSerializer, AccountSerializer
from main.models import Mail, Account


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all().order_by('-id')
    serializer_class = MailSerializer
    http_method_names = ['get', 'head']


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializer
