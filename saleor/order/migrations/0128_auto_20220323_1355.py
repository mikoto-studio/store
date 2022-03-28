# Generated by Django 3.2.12 on 2022-03-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0127_merge_20220302_1520"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="price_expiration_for_unconfirmed",
        ),
        migrations.AddField(
            model_name="order",
            name="should_refresh_prices",
            field=models.BooleanField(default=True),
        ),
    ]