# Generated by Django 2.0.5 on 2018-05-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='picture',
        ),
        migrations.AddField(
            model_name='process',
            name='icons',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
