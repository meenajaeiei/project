# Generated by Django 2.2.dev20180829101932 on 2018-12-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181216_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reason_of_staff',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reason_of_teacher',
            field=models.CharField(default='', max_length=300),
        ),
    ]
