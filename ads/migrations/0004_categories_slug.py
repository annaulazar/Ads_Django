# Generated by Django 4.1.3 on 2022-12-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_adsselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
