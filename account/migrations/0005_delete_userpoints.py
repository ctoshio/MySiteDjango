# Generated by Django 3.1.6 on 2021-09-08 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_earned_scores'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPoints',
        ),
    ]
