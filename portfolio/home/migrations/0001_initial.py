# Generated by Django 3.1.4 on 2021-01-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
    ]