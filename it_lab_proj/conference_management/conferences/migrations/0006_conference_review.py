# Generated by Django 5.0.3 on 2024-04-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0005_conference_research_paper_delete_researchpaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
