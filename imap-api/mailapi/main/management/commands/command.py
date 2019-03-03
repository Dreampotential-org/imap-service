from django.core.management.base import BaseCommand
from main import models
from utils import imap_mail


class Command(BaseCommand):
    help = 'Mail Command'

    def handle(self, *args, **options):
        messages = imap_mail.get_all_mails()
        for message in messages:
            mail = models.Mail()
            mail.subject = message['subject']
            mail.message = message['message']
            mail.local_date = message['local_date']
            mail.row_date = message['row_date']
            mail.account_id = message['account_id']
            mail.save()
