from django import forms 

class jugadorFormulario(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()


class sportFormulario(forms.Form):
    sport = forms.CharField()
    country = forms.CharField()


class colorFormulario(forms.Form):
    color1 = forms.CharField(max_length=30)
    color2 = forms.CharField(max_length=30) 

class coachFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    surname = forms.CharField(max_length=30)
    age = forms.IntegerField()
