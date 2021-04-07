from django.forms import ModelForm
from .models import StudentData

class StudentForm(ModelForm):
    class Meta:
        model=StudentData
        fields='__all__'
