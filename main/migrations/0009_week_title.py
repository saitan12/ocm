# Generated by Django 3.2.3 on 2021-08-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210826_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]