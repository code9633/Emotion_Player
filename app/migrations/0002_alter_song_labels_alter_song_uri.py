# Generated by Django 4.1.6 on 2023-10-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='labels',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='uri',
            field=models.CharField(max_length=255),
        ),
    ]