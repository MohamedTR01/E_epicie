from django.forms import ModelForm
from .models import Client
from .models import Produit
class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class ProduitForm(ModelForm):
    class Meta:
        model=Produit
        fields='__all__'
