# Generated by Django 4.0.6 on 2022-11-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aksara', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogJson',
            fields=[
                ('id', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('catalog_meta', models.JSONField()),
                ('catalog_name', models.CharField(max_length=400)),
                ('catalog_category', models.CharField(max_length=300)),
                ('time_range', models.CharField(max_length=100)),
                ('geographic', models.CharField(max_length=300)),
                ('dataset_begin', models.IntegerField(default=0)),
                ('dataset_end', models.IntegerField(default=0)),
                ('data_source', models.CharField(max_length=100)),
                ('catalog_data', models.JSONField()),
            ],
        ),
    ]
