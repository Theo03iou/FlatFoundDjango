# Generated by Django 5.0.3 on 2024-04-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_num_beds_property_pet_friendly'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='num_beds',
            new_name='number_of_beds',
        ),
        migrations.AddField(
            model_name='property',
            name='number_of_bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
