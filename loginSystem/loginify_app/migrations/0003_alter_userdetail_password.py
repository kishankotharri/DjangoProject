# Generated by Django 5.1.4 on 2025-01-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginify_app', '0002_rename_userdetails_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='password',
            field=models.CharField(blank=True, max_length=12, verbose_name='password'),
        ),
    ]
