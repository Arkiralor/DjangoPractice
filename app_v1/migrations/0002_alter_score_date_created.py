# Generated by Django 4.0.4 on 2022-05-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
