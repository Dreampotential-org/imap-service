# Generated by Django 3.1.5 on 2021-01-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190304_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='hash_password',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]