# Generated by Django 3.0.6 on 2020-05-20 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0028_auto_20200505_1149'),
        ('uni_ticket', '0104_organizationalstructurewsarchipro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalstructurewsarchipro',
            name='organizational_structure',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizational_area.OrganizationalStructure'),
        ),
    ]
