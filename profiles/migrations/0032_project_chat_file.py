# Generated by Django 3.2.12 on 2023-06-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_projectdemo_content_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='chat_file',
            field=models.FileField(blank=True, null=True, upload_to='chat_files/'),
        ),
    ]