# Generated by Django 5.0.3 on 2024-03-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0003_property_pet_friendly_alter_property_price_pcm"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="pet_friendly",
        ),
    ]
