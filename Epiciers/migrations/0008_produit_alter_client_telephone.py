# Generated by Django 4.1.7 on 2023-02-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epiciers', '0007_client_montant_de_credit_client_montant_à_payer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('catégorie', models.CharField(max_length=200)),
                ('prix', models.FloatField(null=True)),
                ('quantité_en_stock', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
