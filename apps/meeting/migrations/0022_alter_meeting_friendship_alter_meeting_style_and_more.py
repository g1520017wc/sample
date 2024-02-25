# Generated by Django 4.2.2 on 2024-01-11 03:46

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0021_alter_footer_body_alter_meeting_joint_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="friendship",
            field=ckeditor.fields.RichTextField(
                blank=True,
                help_text="懇親会費を入力してください．(段落の書式は「標準」が推奨)",
                null=True,
                verbose_name="懇親会費",
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="style",
            field=models.IntegerField(
                default="0",
                help_text="0:通常, 1:表彰有, 2:pdfスタイル",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(2),
                ],
                verbose_name="表示スタイル",
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="time",
            field=models.CharField(
                blank=True,
                default="13:00-17:00",
                help_text="時間を入力してください．例) 13:00-18:00",
                max_length=20,
                null=True,
                verbose_name="時間",
            ),
        ),
        migrations.AlterField(
            model_name="presentation",
            name="order",
            field=models.IntegerField(
                default="1",
                help_text="講演の順番を数字で入力してください．(休憩等も含む)",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(20),
                ],
                verbose_name="順番",
            ),
        ),
    ]
