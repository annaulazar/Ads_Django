# Generated by Django 4.1.3 on 2022-11-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ads_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Описание'),
        ),
    ]
