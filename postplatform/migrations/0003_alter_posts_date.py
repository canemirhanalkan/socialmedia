# Generated by Django 5.0.3 on 2024-05-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postplatform', '0002_alter_posts_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
