# Generated by Django 5.0.1 on 2024-01-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avg_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
