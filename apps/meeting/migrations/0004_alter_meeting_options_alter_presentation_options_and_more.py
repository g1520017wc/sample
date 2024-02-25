# Generated by Django 4.2 on 2023-09-15 08:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0003_meeting_presentation_remove_year_application_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="meeting",
            options={"verbose_name_plural": "研究会テーブル"},
        ),
        migrations.AlterModelOptions(
            name="presentation",
            options={"verbose_name_plural": "講演テーブル"},
        ),
        migrations.RemoveField(
            model_name="meeting",
            name="year",
        ),
        migrations.RemoveField(
            model_name="meeting",
            name="year_wa",
        ),
    ]
