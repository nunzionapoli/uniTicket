# Generated by Django 3.0 on 2020-01-07 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0053_delete_tickethistory"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TaskHistory",
        ),
    ]