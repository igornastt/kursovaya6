# Generated by Django 4.2.4 on 2023-08-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_mail_clients'),
        ('clients', '0003_alter_client_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='mails',
            field=models.ManyToManyField(through='clients.Enrollment', to='mailing.mail'),
        ),
    ]
