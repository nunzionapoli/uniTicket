# Generated by Django 3.0.3 on 2020-04-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0090_auto_20200416_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategory',
            name='receive_email',
            field=models.BooleanField(default=False, verbose_name='Operatori ricevono notifica email per ogni ticket aperto'),
        ),
    ]