# Generated by Django 2.2.6 on 2019-12-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0011_mentor_sponsor_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='unnamed', max_length=29),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=29),
        ),
    ]
