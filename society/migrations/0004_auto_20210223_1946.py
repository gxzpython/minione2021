# Generated by Django 3.1.7 on 2021-02-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0003_auto_20210223_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]