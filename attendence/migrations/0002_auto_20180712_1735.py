# Generated by Django 2.0.2 on 2018-07-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='description',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='subject',
        ),
        migrations.AddField(
            model_name='attendence',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
