# Generated by Django 3.2.23 on 2024-02-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('rno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
