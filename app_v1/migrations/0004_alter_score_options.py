# Generated by Django 4.0.4 on 2022-05-10 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0003_alter_score_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ('-score', 'date_created', 'name')},
        ),
    ]
