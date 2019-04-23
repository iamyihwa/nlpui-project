from django import forms

class TextForm(forms.Form):
    class Meta:
        body = forms.CharField(max_length = 2000, widget = forms.Textarea(), help_text = 'Write here your text!')
        ner = forms.BooleanField(required=False, initial=True)
        sent_2 = forms.BooleanField(required=False, initial=True)
        sent_11 = forms.BooleanField(required=False, initial=True)

class TextResult(forms.Form):
    class Meta:
        ner_result = forms.CharField(max_length = 4000)
        sent_2_result = forms.CharField(max_length = 4000)
        sent_11_result = forms.CharField(max_length = 4000 )