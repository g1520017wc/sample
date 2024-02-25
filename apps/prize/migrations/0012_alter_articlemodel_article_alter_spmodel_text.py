# Generated by Django 4.1 on 2024-02-13 11:16

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):
    dependencies = [
        ("prize", "0011_alter_articlemodel_options_alter_articlemodel_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlemodel",
            name="article",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text='記事を入力してください．(書式は"Paragraph")',
                null=True,
                verbose_name="記事",
            ),
        ),
        migrations.AlterField(
            model_name="spmodel",
            name="text",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text='画像を含めて作成してください。(書式は"Paragraph")',
                null=True,
                verbose_name="記事",
            ),
        ),
    ]
