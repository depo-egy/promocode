# Generated by Django 3.0.6 on 2020-08-13 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promocode', '0002_auto_20200813_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo_code',
            name='title',
        ),
    ]
