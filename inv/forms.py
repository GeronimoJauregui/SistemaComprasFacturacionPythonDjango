from django import forms
from .models import Categoria, SubCategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria #Con que modelo trabajara.
        fields = ['descripcion','estado'] #Que campos va a tomar.
        labels = {'descripcion':"Descripción de la categoría",'estado':"Estado"} #Etiquetas para los campos.
        widget={'descripción':forms.TextInput} #Que elementos del bootstrap va a ocupar en la vista.
    
    #Todos los elementos que se renderizaran utilizaran el form-control.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria #Con que modelo trabajara.
        fields = ['categoria','descripcion','estado'] #Que campos va a tomar.
        labels = {'descripcion':"Subcategoría",'estado':"Estado"} #Etiquetas para los campos.
        widget={'descripción':forms.TextInput} #Que elementos del bootstrap va a ocupar en la vista.
    
    #Todos los elementos que se renderizaran utilizaran el form-control.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione categoria" #Para cuando no se haya seleccionado ningun campo.