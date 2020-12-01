from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

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

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca #Con que modelo trabajara.
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

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida #Con que modelo trabajara.
        fields = ['descripcion','estado'] #Que campos va a tomar.
        labels = {'descripcion':"Descripción de la unidad de medida",'estado':"Estado"} #Etiquetas para los campos.
        widget={'descripción':forms.TextInput} #Que elementos del bootstrap va a ocupar en la vista.
    
    #Todos los elementos que se renderizaran utilizaran el form-control.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields=['codigo','codigo_barra','descripcion','estado',
        'precio','existencia','ultima_compra','marca','subcategoria',
        'unidad_medida']
        exclude=['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True
