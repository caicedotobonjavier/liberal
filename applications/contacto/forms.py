from django import forms
#
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = (
            'nombre_completo',
            'email',
            'telefono',
            'asunto',
            'mensaje',
        )

        widgets = {
            'nombre_completo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese su nombre completo'
                }
            ),

            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Ingrese su correo electronico'
                }
            ),

            'telefono' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese su telefono de contacto'
                }
            ),

            'asunto' : forms.TextInput(
                attrs={
                    'placeholder' : 'Asunto del mensaje'
                }
            )
        }