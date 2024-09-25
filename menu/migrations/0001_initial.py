# Generated by Django 4.2.16 on 2024-09-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('drink', models.CharField()),
                ('cost', models.FloatField()),
                ('calories', models.IntegerField()),
                ('vegetarian', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('gluten', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('food', models.CharField()),
                ('cost', models.FloatField()),
                ('calories', models.IntegerField()),
                ('vegetarian', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('gluten', models.BooleanField()),
            ],
        ),
    ]
