# Generated by Django 4.2.2 on 2024-01-11 02:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("information", "0007_alter_book_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="comment",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="書籍紹介(段落の書式は「標準」が推奨)"
            ),
        ),
        migrations.AlterField(
            model_name="webbookmark",
            name="comment",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="紹介文(段落の書式は「標準」が推奨)"
            ),
        ),
    ]
