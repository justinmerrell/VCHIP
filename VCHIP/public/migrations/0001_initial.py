# Generated by Django 3.1.7 on 2021-02-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('target_name', models.CharField(max_length=128)),
                ('target_extra', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
