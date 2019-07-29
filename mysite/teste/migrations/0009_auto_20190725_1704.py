# Generated by Django 2.1 on 2019-07-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0008_auto_20190722_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/poster'),
        ),
    ]
