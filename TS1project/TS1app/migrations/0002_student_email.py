# Generated by Django 4.2.3 on 2023-07-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TS1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]