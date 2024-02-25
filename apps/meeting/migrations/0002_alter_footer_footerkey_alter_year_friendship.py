# Generated by Django 4.2.2 on 2023-08-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer",
            name="footerkey",
            field=models.CharField(
                help_text="フッターキーを入力してください．", max_length=50, verbose_name="フッターキー"
            ),
        ),
        migrations.AlterField(
            model_name="year",
            name="friendship",
            field=models.CharField(
                blank=True,
                help_text="懇親会費を入力してください．",
                max_length=200,
                null=True,
                verbose_name="懇親会費",
            ),
        ),
    ]
