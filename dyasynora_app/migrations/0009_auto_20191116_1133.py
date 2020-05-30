# Generated by Django 2.2.6 on 2019-11-16 11:33

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0008_auto_20191111_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]