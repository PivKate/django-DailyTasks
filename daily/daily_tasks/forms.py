from django import forms 

class DailyForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter task.e.g. Delete junk files', 'aria-label' : 'Daily', 'aria-describedby' : 'add-btn'}))