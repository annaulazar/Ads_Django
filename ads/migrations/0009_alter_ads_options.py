# Generated by Django 4.1.3 on 2022-11-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_alter_ads_category_alter_users_locations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ads',
            options={'ordering': ['-price'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]