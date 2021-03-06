# Generated by Django 4.0.1 on 2022-01-17 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Weather_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-created_date', 'id']},
        ),
        migrations.AddField(
            model_name='city',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
