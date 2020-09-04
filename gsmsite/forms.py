from django import forms
from .models import Usermodel
from .models import AddEvent
from .models import AddPackage

#  creating RegisterForm
class  RegisterForm( forms.ModelForm):

    class Meta:

        model =  Usermodel
        fields = "__all__"

# class LoginForm( forms.ModelForm):

#     class Meta:

#         model = Usermodel
#         fields = ['username','password']

  #crete add event      

class  AddEventForm( forms.ModelForm):

    class Meta:

        model =  AddEvent
        fields = "__all__"        
    

#   create add package      
class AddPackageForm(forms.ModelForm):
    class Meta:
        model = AddPackage
        fields="__all__"            
        