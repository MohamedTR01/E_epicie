# Generated by Django 4.1.7 on 2023-02-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epiciers', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='dateCreation',
        ),
        migrations.AddField(
            model_name='client',
            name='adresse',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]