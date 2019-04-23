from django import forms

class TextForm(forms.Form):
    #class Meta : this shouldn't be there
    text = forms.CharField(max_length = 2000, widget = forms.Textarea(), help_text = 'Write here your text!')
    ner = forms.BooleanField(required=False)
    sent_2 = forms.BooleanField(required=False)
    sent_11 = forms.BooleanField(required=False)

class TextResult(forms.Form):
    ner_result = forms.CharField(max_length = 4000)
    sent_2_result = forms.CharField(max_length = 4000)
    sent_11_result = forms.CharField(max_length = 4000 )
