# Generated by Django 2.1.1 on 2018-09-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuing', '0002_auto_20180903_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='register_id',
            field=models.CharField(max_length=7),
        ),
    ]
