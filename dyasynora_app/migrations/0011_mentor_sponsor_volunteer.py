# Generated by Django 2.2.6 on 2019-11-23 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dyasynora_app', '0010_auto_20191116_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(verbose_name='%d/%m/%Y %H:%M:%S')),
                ('end_datetime', models.DateTimeField(verbose_name='%d/%m/%Y %H:%M:%S')),
                ('message', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyasynora_app.Activity')),
                ('volunteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_datetime', models.DateTimeField(verbose_name='%d/%m/%Y %H:%M:%S')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyasynora_app.Project')),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_datetime', models.DateTimeField(verbose_name='%d/%m/%Y %H:%M:%S')),
                ('description', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyasynora_app.Activity')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]