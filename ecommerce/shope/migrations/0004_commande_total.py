# Generated by Django 4.1.6 on 2023-04-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shope", "0003_remove_commande_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="commande",
            name="total",
            field=models.CharField(default="500", max_length=200),
            preserve_default=False,
        ),
    ]
