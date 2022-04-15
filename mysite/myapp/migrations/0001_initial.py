# Generated by Django 3.2.9 on 2022-01-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=30, unique=True)),
                ('age', models.IntegerField(default='')),
            ],
            options={
                'db_table': 'Book1',
            },
        ),
        migrations.CreateModel(
            name='Hospital_beds',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('District', models.CharField(default='', max_length=30, unique=True)),
                ('Number_of_beds_per_1000', models.IntegerField(default='')),
            ],
            options={
                'db_table': 'Hospital_beds',
            },
        ),
    ]