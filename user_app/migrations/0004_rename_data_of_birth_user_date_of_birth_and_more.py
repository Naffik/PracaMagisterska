# Generated by Django 4.1.1 on 2022-10-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_user_data_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]