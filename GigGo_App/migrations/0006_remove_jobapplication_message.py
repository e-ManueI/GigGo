# Generated by Django 4.1.7 on 2023-04-01 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GigGo_App', '0005_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='message',
        ),
    ]