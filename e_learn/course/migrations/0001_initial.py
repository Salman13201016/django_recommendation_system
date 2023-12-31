# Generated by Django 4.1.7 on 2023-09-16 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="courses",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("fee", models.IntegerField()),
                ("discount", models.IntegerField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("description", models.TextField()),
                (
                    "cat_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.categories",
                    ),
                ),
            ],
        ),
    ]
