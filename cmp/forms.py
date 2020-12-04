from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor #Con que modelo trabajara.
        exclude = ['um','fm','uc','fc']
        widget={'descripción':forms.TextInput} #Que elementos del bootstrap va a ocupar en la vista.
    
    #Todos los elementos que se renderizaran utilizaran el form-control.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })