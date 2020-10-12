from django import forms

from apps.users.models import Users
from django.contrib import messages

class UsersForms(forms.ModelForm):
    confirmpassword = forms.CharField()
    confirmpassword.label = 'Confirmar Contraseña'
    class Meta:
        
        model = Users

        fields  = [
            'first_name',
            'last_name',
            'typedocument',
            'numberdocument',
            'year_old',
            'phone',
            'email',
            'username',
            'password',
            'confirmpassword',
            'is_medical',
            'is_patient'
        ]
        
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'typedocument': 'Tipo de Documento',
            'numberdocument': 'Numero de Documento',
            'year_old': 'Edad',
            'phone': 'Telefono',
            'email': 'Correo',
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
            'is_medical': 'Doctor',
            'is_patient': 'Paciente',
        }

    def clean(self):
        data = super(UsersForms, self).clean()
        password1 = data.get('password')
        password2 = data.get('confirmpassword')

        if password1 != password2:
            raise forms.ValidationError({
                'confirmpassword': forms.ValidationError('Las contraseñas no coinciden.')
                })

        return super(UsersForms, self).clean()

