# Generated by Django 4.0.3 on 2022-04-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_ration_app', '0002_rename_contact_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, null='empty')),
            ],
        ),
    ]
