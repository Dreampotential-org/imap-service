from main.models import Mail
from rest_framework import serializers


class MailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mail
        fields = (
            'id', 'message_id', 'subject', 'message', 'row_date', 'local_date'
        )
