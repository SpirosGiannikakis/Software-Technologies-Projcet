# Generated by Django 3.1.1 on 2020-09-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]