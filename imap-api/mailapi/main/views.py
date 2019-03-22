from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from main.serializers import MailSerializer, AccountSerializer
from main.models import Mail, Account


class MailViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Mail.objects.all().order_by('-id')
    serializer_class = MailSerializer
    http_method_names = ['get', 'head']


class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializer
