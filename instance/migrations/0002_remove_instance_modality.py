# Generated by Django 3.2.16 on 2022-12-03 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instance',
            name='modality',
        ),
    ]