# Generated by Django 2.0.1 on 2018-07-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_platform', '0002_auto_20180721_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='latitude',
            field=models.FloatField(default=39.90923, verbose_name='景点纬度'),
        ),
        migrations.AlterField(
            model_name='story',
            name='longitude',
            field=models.FloatField(default=116.397428, verbose_name='景点经度'),
        ),
    ]
