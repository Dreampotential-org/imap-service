from django.db import models
import hashlib


class Account(models.Model):
    email = models.CharField(max_length=512)
    password = models.CharField(max_length=512)

    def __str__(self):
        return self.email


class Mail(models.Model):
    message_id = models.CharField(max_length=512, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    mail_from = models.EmailField()
    mail_to = models.EmailField()
    subject = models.CharField(max_length=512)
    message = models.TextField()
    local_date = models.CharField(max_length=128)
    row_date = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        val = self.subject + '-' + self.row_date
        self.message_id = hashlib.sha256(val.encode()).hexdigest()
        super(Mail, self).save(*args, **kwargs)
