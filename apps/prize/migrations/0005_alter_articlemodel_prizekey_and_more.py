# Generated by Django 4.2.2 on 2023-08-03 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prize", "0004_studentaward"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlemodel",
            name="prizekey",
            field=models.ForeignKey(
                help_text="賞のIDを選択してください．",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="prizearticle",
                related_query_name="fprizearticle",
                to="prize.yearmodel",
                verbose_name="賞ID",
            ),
        ),
        migrations.AlterField(
            model_name="studentaward",
            name="prizekey",
            field=models.ForeignKey(
                help_text="賞のIDを選択してください．",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="prizestudentaward",
                related_query_name="fprizestudentaward",
                to="prize.yearmodel",
                verbose_name="賞ID",
            ),
        ),
        migrations.AlterField(
            model_name="suzukiokadamodel",
            name="prizekey",
            field=models.ForeignKey(
                help_text="賞のIDを選択してください．",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="prizesuzukiokada",
                related_query_name="fprizesuzukiokada",
                to="prize.yearmodel",
                verbose_name="賞ID",
            ),
        ),
    ]
