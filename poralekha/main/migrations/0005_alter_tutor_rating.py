# Generated by Django 3.2 on 2021-04-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210423_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
