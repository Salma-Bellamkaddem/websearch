from django.forms import ModelForm
from .models import Project



class projectForm(ModelForm):
    class Meta:
        model = Project
        fields ='__all__'
        exclude=['vote_total','vote_ratio']