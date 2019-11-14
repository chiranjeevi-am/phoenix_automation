from django import forms

class EmpForm(forms.Form):
    emp_id = forms.IntegerField(label="Employee ID",max_value=8)
    first_name = forms.CharField(label="Enter First name", max_length=50)
    last_name = forms.CharField(label="Enter Last name",max_length=100)
    phone_number = forms.IntegerField(label="Mobile number",max_value=10)