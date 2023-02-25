# Generated by Django 4.1.7 on 2023-02-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Epiciers', '0005_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('telephone', models.FloatField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
