# Generated by Django 2.0.2 on 2018-02-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='marked',
            field=models.BooleanField(default=True),
        ),
    ]
