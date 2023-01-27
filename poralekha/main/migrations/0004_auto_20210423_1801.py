# Generated by Django 3.2 on 2021-04-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210422_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='honours_institute',
        ),
        migrations.AlterField(
            model_name='student',
            name='address_phone',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='address_present',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='student',
            name='institute',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='address_covered',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='address_phone',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='address_present',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='extra_facilities',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='preffered_class',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='preffered_subject',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='preffered_time',
            field=models.CharField(max_length=512),
        ),
    ]
