# Generated by Django 3.0.6 on 2020-05-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0114_auto_20200521_1300"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizationalstructurewsarchipro",
            name="protocollo_agd",
            field=models.CharField(default=1, max_length=12, verbose_name="AGD"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organizationalstructurewsarchipro",
            name="protocollo_fascicolo_anno",
            field=models.IntegerField(
                default=1, max_length=4, verbose_name="Fascicolo anno"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="organizationalstructurewsarchipro",
            name="protocollo_uo",
            field=models.CharField(default=1, max_length=12, verbose_name="UO"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticketcategorywsarchipro",
            name="protocollo_agd",
            field=models.CharField(default=1, max_length=12, verbose_name="AGD"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticketcategorywsarchipro",
            name="protocollo_fascicolo_anno",
            field=models.IntegerField(
                default=1, max_length=4, verbose_name="Fascicolo anno"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticketcategorywsarchipro",
            name="protocollo_uo",
            field=models.CharField(default=1, max_length=12, verbose_name="UO"),
            preserve_default=False,
        ),
    ]
