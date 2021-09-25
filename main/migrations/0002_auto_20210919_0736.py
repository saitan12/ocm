# Generated by Django 3.2.3 on 2021-09-19 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='university',
        ),
        migrations.AddField(
            model_name='certificate',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='files',
            name='week',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.week'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]