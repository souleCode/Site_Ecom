# Generated by Django 4.1.6 on 2023-04-29 12:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shope", "0002_commande"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commande",
            name="password",
        ),
    ]
