# Generated by Django 4.2.5 on 2024-01-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_room_options_remove_room_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='district',
            field=models.CharField(max_length=200, null=True),
        ),
    ]