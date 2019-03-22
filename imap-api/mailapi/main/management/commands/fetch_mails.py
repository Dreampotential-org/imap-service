from django.core.management.base import BaseCommand
from main import models
from utils import imap_mail


class Command(BaseCommand):
    help = 'Fetching mail from mail accounts'

    def handle(self, *args, **options):
        messages = imap_mail.get_all_mails()
        for message in messages:
            mail = models.Mail()
            mail.subject = message['subject']
            mail.message = message['message']
            mail.local_date = message['local_date']
            mail.row_date = message['row_date']
            mail.account_id = message['account_id']
            check = models.Mail.objects.filter(
                message_id=mail.gen_message_id()
            ).count()

            if check == 0:
                mail.save()
