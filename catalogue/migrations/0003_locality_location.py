# Generated by Django 5.0.dev20230428110408 on 2023-05-06 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('designation', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locations', to='catalogue.locality')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
    ]
