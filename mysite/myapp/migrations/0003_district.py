# Generated by Django 3.2.9 on 2022-02-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('District', models.CharField(default='', max_length=30, unique=True)),
                ('Cases', models.IntegerField(default='')),
                ('Recovered', models.IntegerField(default='')),
                ('Deaths', models.IntegerField(default='')),
            ],
            options={
                'db_table': 'District',
            },
        ),
    ]