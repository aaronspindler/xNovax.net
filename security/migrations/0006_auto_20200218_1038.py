# Generated by Django 3.0.3 on 2020-02-18 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0005_auto_20200212_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fingerprint',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ip',
            name='user',
        ),
    ]