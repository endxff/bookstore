# Generated by Django 5.1.3 on 2024-11-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="categoriy",
            new_name="category",
        ),
    ]
