# Generated by Django 4.2.1 on 2023-03-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d'),
        ),
    ]
