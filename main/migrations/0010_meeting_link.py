# Generated by Django 3.2.3 on 2021-09-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210925_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]