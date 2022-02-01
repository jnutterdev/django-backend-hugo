# Generated by Django 4.0.1 on 2022-01-31 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=280),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
