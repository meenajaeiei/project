# Generated by Django 2.1.2 on 2018-10-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20181013_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.IntegerField(default=1),
        ),
    ]
