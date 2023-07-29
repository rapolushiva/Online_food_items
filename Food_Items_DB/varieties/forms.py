from django import forms

from varieties.models import food

class foodForm(forms.ModelForm):
    class Meta:
        model = food
        fields=['Item_Image', 'Item_Name','Item_Quantity','Item_Category','Item_Cost','Item_Review']

        widgets ={
            'Item_Image':forms.FileInput(attrs ={'class':'form-control'}),
            'Item_Name':forms.TextInput(attrs ={'class':'form-control'}),
            'Item_Quantity':forms.TextInput(attrs ={'class':'form-control'}),
            'Item_Category':forms.Select(attrs={'class':'form-control'}),
            'Item_Cost':forms.TextInput(attrs ={'class':'form-control'}),
            'Item_Review':forms.Textarea(attrs ={'class':'form-control'}),
            #'Manufactured_Date':forms.DateTimeField(attrs={'class':'form-control'}),
            #'is_published':forms.Select(attrs ={'class':'form-control'})
        }
        
