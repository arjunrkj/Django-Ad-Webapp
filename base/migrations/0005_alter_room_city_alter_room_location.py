# Generated by Django 4.2.5 on 2023-12-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_room_options_room_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]