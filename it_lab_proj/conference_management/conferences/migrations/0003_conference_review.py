# Generated by Django 5.0.3 on 2024-04-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_chair_reviewer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='review',
            field=models.FileField(blank=True, null=True, upload_to='conference_reviews'),
        ),
    ]
