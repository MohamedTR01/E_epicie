from django.db import models

# Create your models here.
    
# N.B : Lorsqu'on a modifier ces donnees il faut ecrire dans terminal python manage.py makemigrations et en suivant python manage.py migrate 


class Client(models.Model):
    nom= models.CharField(max_length=200)
    adresse=models.CharField(max_length=200)
    telephone=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)

    # image=models.ImageField(upload_to='photos', height_field="45", width_field="45")
  
    montant_de_credit=models.FloatField(null=True)
    montant_à_payer=models.FloatField(null=True)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
    nom=models.CharField(max_length=200)
    description=models.TextField()
    catégorie=models.CharField(max_length=200)
    prix=models.FloatField(null=True)
    quantité_en_stock=models.FloatField(null=True)
    quantité_vendues=models.FloatField(null=True)

    def __str__(self):
        return self.nom
    


