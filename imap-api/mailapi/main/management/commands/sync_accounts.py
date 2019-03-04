from django.core.management.base import BaseCommand
import subprocess

from main.models import Account


class Command(BaseCommand):
    help = 'Syncing email accounts'

    def handle(self, *args, **options):
        accounts = Account.objects.filter(active_on_server=False)
        for account in accounts:
            cmd = 'sudo ../../docker-mailserver/setup.sh email add'.split()
            cmd.append(account.email)
            cmd.append(account.password)
            subprocess.call(cmd)
            account.active_on_server = True
            account.save()
            self.stdout.write("{account.email} created", ending='')
