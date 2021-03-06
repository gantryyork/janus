# Generated by Django 3.0.5 on 2020-05-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('ipv4', models.CharField(max_length=15)),
            ],
        ),
    ]
