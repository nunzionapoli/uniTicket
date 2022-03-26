# Generated by Django 2.2.3 on 2019-07-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0036_ticketreply_read"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ticketreply",
            old_name="user",
            new_name="owner",
        ),
        migrations.AddField(
            model_name="ticketreply",
            name="from_owner",
            field=models.BooleanField(default=True),
        ),
    ]
