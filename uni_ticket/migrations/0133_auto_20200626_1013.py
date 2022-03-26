# Generated by Django 3.0.7 on 2020-06-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0132_auto_20200626_1007"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationalstructurewsarchipro",
            name="protocollo_email",
            field=models.EmailField(
                blank=True,
                default="amministrazione@pec.unical.it",
                max_length=255,
                verbose_name="E-mail",
            ),
        ),
        migrations.AlterField(
            model_name="ticketcategorywsarchipro",
            name="protocollo_email",
            field=models.EmailField(
                blank=True,
                default="amministrazione@pec.unical.it",
                max_length=255,
                verbose_name="E-mail",
            ),
        ),
    ]
