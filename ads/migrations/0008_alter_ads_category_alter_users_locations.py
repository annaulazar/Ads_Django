# Generated by Django 4.1.3 on 2022-11-10 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ads.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='users',
            name='locations',
            field=models.ManyToManyField(to='ads.location', verbose_name='Адрес'),
        ),
    ]