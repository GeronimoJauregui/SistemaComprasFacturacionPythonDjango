from django import forms
from .models import Proveedor, ComprasEnc

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

class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Meta:
        model = ComprasEnc
        fields=['proveedor','fecha_compra','observacion',
        'no_factura','fecha_factura','sub_total',
        'descuento','total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True