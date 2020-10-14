# Generated by Django 3.0.1 on 2019-12-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40)),
                ('company_logo', models.FileField(blank='True', null='True', upload_to='')),
                ('company_city', models.CharField(max_length=40)),
            ],
        ),
    ]
