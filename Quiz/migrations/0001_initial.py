# Generated by Django 3.2.5 on 2021-07-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('options1', models.CharField(max_length=100)),
                ('options2', models.CharField(max_length=100)),
                ('options3', models.CharField(max_length=100)),
                ('options4', models.CharField(max_length=100)),
            ],
        ),
    ]
