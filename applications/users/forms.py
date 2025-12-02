#Forms
from django import forms
#
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Ingrese contraseña'
            }
        )
    )

    confirmar_password = forms.CharField(
        label='Confirmar contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Repita contraseña'
            }
        )
    )
    class Meta:
        model = User
        fields = (
            'email',
            'nombre_completo',
            'direccion',
            'telefono',
            'fecha_nacimiento',
        )


        widgets = {
            'fecha_nacimiento' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            )
        }
    

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        contrasena = self.cleaned_data['password']
        contrasena_2 = self.cleaned_data['confirmar_password']
        if contrasena_2 != contrasena:
            raise forms.ValidationError('Las contraseñas no coinciden')
        elif len(contrasena) < 8:
            raise forms.ValidationError('La contraeña debe tener mas de 8 digitos')
        return cleaned_data