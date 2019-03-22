from django.core.management.base import BaseCommand
import subprocess

from main.models import Account


class Command(BaseCommand):
    help = 'Syncing email accounts'

    def handle(self, *args, **options):
        accounts = Account.objects.filter(active_on_server=False)
        for account in accounts:
            cmd = 'doveadm pw -s SHA512-CRYPT -p'.split()
            cmd.append(account.password)
            output = subprocess.check_output(cmd)
            output = output.decode('utf-8').replace('\n', '')
            account.active_on_server = True
            account.hash_password = output
            account.save()
            password_line = account.email + '|{SHA512-CRYPT}' + output

            with open('/postfix-accounts.cf', 'a') as f:
                f.write(password_line)

            self.stdout.write("%s created" % account.email, ending='\n')
