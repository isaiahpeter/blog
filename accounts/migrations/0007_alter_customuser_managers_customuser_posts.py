# Generated by Django 4.2.1 on 2023-07-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_post_category'),
        ('accounts', '0006_profile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='posts',
            field=models.ManyToManyField(related_name='forum_posts', to='forum.post'),
        ),
    ]
