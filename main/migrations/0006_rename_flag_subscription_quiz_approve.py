# Generated by Django 3.2.3 on 2021-09-24 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210924_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='flag',
            new_name='quiz_approve',
        ),
    ]
