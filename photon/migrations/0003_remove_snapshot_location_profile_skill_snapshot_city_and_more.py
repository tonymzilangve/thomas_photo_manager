# Generated by Django 4.1.4 on 2022-12-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photon', '0002_alter_comment_options_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snapshot',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Скилл'),
        ),
        migrations.AddField(
            model_name='snapshot',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='snapshot',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='snapshot',
            name='person_list',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Кто на фото?'),
        ),
        migrations.AddField(
            model_name='snapshot',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='category',
            field=models.ManyToManyField(blank=True, default='Разное', to='photon.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='snapshot',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='Longitude'),
        ),
    ]
