#!/usr/bin/env python
import sys
import imaplib
# import getpass
import email
import email.header
import datetime


EMAIL_ACCOUNT = "test2@postgecko.com"
EMAIL_PASSWORD = "test"
EMAIL_FOLDER = "INBOX"


def get_mails(mail_client):
    rv, data = mail_client.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = mail_client.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return


        msg = email.message_from_bytes(data[0][1])
        print(msg)
        hdr = email.header.make_header(
            email.header.decode_header(msg['Subject'])
        )
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple)
            )
            print(
                "Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S")
            )


mail_client = imaplib.IMAP4_SSL('mailserver.postgecko.com')

try:
    rv, data = mail_client.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!!")
    sys.exit(1)

print(rv, data)

rv, data = mail_client.select(EMAIL_FOLDER)
if rv == 'OK':
    print("Processing mailbox...\n")
    get_mails(mail_client)
    mail_client.close()
else:
    print("ERROR: Unable to open mailbox ", rv)
