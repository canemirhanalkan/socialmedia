# Generated by Django 5.0.3 on 2024-05-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postplatform', '0003_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
