# Generated by Django 4.2.2 on 2023-06-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prize", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="yearmodel",
            name="prizekey",
            field=models.CharField(
                help_text="賞のIDを入力してください．例：2021_鈴木・岡田記念賞",
                max_length=100,
                unique=True,
                verbose_name="賞ID",
            ),
        ),
    ]
