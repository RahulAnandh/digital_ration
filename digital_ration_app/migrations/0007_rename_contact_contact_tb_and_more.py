# Generated by Django 4.0.3 on 2022-04-08 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital_ration_app', '0006_rename_product_product_tb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contact_tb',
        ),
        migrations.RenameModel(
            old_name='Subscribe',
            new_name='Subscribe_tb',
        ),
        migrations.RenameModel(
            old_name='user_registration',
            new_name='User_registration_tb',
        ),
    ]
