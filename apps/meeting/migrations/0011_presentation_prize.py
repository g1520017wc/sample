# Generated by Django 4.1 on 2023-10-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0010_alter_meeting_style"),
    ]

    operations = [
        migrations.AddField(
            model_name="presentation",
            name="prize",
            field=models.BooleanField(
                default=False, help_text="鈴木・岡田記念賞関連である場合True", verbose_name="鈴木・岡田記念賞"
            ),
        ),
    ]
