# Generated by Django 4.2 on 2023-04-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_featured_image_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
