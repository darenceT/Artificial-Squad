# Generated by Django 3.2.7 on 2021-10-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20210907_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='finance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='marketing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='product_management',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='user_experience',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='web_development',
            field=models.BooleanField(default=False),
        ),
    ]
