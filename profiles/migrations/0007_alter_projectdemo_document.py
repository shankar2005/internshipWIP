# Generated by Django 3.2.12 on 2023-04-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_projectdemo_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdemo',
            name='document',
            field=models.FileField(default='settings.MEDIA_ROOT\\profile_pics\\default.jpg', upload_to=''),
        ),
    ]