# Generated by Django 4.2.1 on 2023-03-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='forum_categ_name_9270a2_idx'),
        ),
    ]
