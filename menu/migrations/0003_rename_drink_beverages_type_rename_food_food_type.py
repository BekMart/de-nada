# Generated by Django 4.2.16 on 2024-09-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_beverages_title_alter_food_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beverages',
            old_name='drink',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food',
            new_name='type',
        ),
    ]
