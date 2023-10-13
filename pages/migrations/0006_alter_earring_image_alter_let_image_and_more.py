# Generated by Django 4.2.5 on 2023-10-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_earring_delete_earing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="earring",
            name="image",
            field=models.ImageField(blank=True, upload_to="earrings/"),
        ),
        migrations.AlterField(
            model_name="let",
            name="image",
            field=models.ImageField(blank=True, upload_to="lets/"),
        ),
        migrations.AlterField(
            model_name="necklace",
            name="image",
            field=models.ImageField(blank=True, upload_to="necklaces/"),
        ),
    ]
