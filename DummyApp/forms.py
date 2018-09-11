from django import forms
from models import Employee
class EmpForm(forms.Form):
    class Meta:
        model = Employee
        fields = ('name','department')