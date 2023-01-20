# Generated by Django 3.2.12 on 2023-01-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20230118_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='stage',
            field=models.CharField(blank=True, choices=[('DreamProject', 'DreamProject'), ('Lead', 'Lead'), ('In Progress', 'In Progress'), ('Halt', 'Halt'), ('Finish', 'Finish')], default='', max_length=100),
        ),
    ]
