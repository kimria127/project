# Generated by Django 4.2.5 on 2023-10-11 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content_list",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pages.necklace"
            ),
        ),
    ]
