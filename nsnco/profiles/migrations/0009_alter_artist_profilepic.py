# Generated by Django 3.2.12 on 2023-01-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_artist_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profilePic',
            field=models.ImageField(blank=True, default='avatar.png', upload_to='artist_pics'),
        ),
    ]
