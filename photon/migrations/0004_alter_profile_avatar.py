# Generated by Django 4.1.4 on 2022-12-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photon', '0003_remove_snapshot_location_profile_skill_snapshot_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/<django.db.models.fields.CharField>/avatar', verbose_name='Аватар'),
        ),
    ]
