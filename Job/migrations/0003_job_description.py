# Generated by Django 3.1.1 on 2020-09-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
