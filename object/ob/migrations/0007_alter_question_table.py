# Generated by Django 4.1.2 on 2022-11-07 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob', '0006_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='ob_question',
        ),
    ]
