# Generated by Django 3.0.5 on 2020-05-04 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_schedulerconfig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulerconfig',
            old_name='values',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='schedulerconfig',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
