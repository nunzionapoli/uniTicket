# Generated by Django 2.2.4 on 2019-08-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0040_ticketreply_read_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategory',
            name='allow_guest',
            field=models.BooleanField(default=False, verbose_name='Accessibile agli ospiti'),
        ),
        migrations.AddField(
            model_name='ticketcategory',
            name='allow_operator',
            field=models.BooleanField(default=False, verbose_name='Accessibile agli operatori interni'),
        ),
        migrations.AddField(
            model_name='ticketcategory',
            name='allow_utente',
            field=models.BooleanField(default=False, verbose_name="Accessibile agli utenti dell'organizzazione"),
        ),
    ]