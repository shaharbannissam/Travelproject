# Generated by Django 3.2.12 on 2022-02-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='photos')),
                ('descn', models.TextField()),
            ],
        ),
    ]
