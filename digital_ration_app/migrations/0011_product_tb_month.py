# Generated by Django 4.0.3 on 2022-04-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_ration_app', '0010_rename_subscribe_tb_subscribers_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='month',
            field=models.CharField(max_length=20, null='empty'),
            preserve_default='empty',
        ),
    ]
