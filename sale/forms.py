from django import forms
from django import forms
from django.forms import DateInput
Form_Choices=(
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
    ('#4', 'Seaborn Chart')
)
class SaleSearchForm(forms.Form):
    date_from = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=Form_Choices)

class PositionSearchForm(forms.Form):
    date_from = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=Form_Choices)