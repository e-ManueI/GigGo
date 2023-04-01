# Generated by Django 4.1.7 on 2023-04-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigGo_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['user'], 'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('inprogress', 'In Progress'), ('Reviewing', 'Reviewing'), ('complete', 'Complete')], max_length=20, null=True),
        ),
    ]
