# Generated by Django 2.2.dev20180829101932 on 2018-12-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_room_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable'), ('pending', 'pending'), ('in progress', 'in progress')], default='available', max_length=15),
        ),
    ]
