# Generated by Django 3.2.8 on 2021-11-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barghash', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
