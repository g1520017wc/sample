# Generated by Django 4.2.2 on 2023-10-27 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0015_alter_meeting_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="category",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="meetingcategory",
                related_query_name="fmeetingcategory",
                to="meeting.meetingcategory",
                verbose_name="カテゴリ",
            ),
        ),
    ]
