# Generated by Django 3.0.6 on 2020-05-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
