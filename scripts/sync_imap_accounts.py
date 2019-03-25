import subprocess

cmd = 'docker exec -it imap-server_mail-api_1  ./scripts/sync_imap_accounts.sh'

# vals = subprocess.getoutput(cmd)
output = subprocess.check_output(cmd.split())

output = output.decode('utf-8').replace('\n', '')
output = output.replace('\r', '')

cmds = output.split(',')
cmds = [item for item in cmds if item != '']
print(cmds)

for val in cmds:
    email_add = './docker-mailserver/setup.sh email add'.split()
    email_add = email_add + val.split()
    print(email_add)
    subprocess.check_output(email_add)
