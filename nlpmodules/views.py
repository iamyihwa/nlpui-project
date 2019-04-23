from django.shortcuts import render
from .forms import TextForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'nlpmodules/home.html')

def english(request):
    form = TextForm()
    if request.method == 'POST':
        #create an object from it
        filled_form = TextForm(request.POST)
        if filled_form.is_valid():
            returned_text = filled_form.cleaned_data['text']
            #result_form = TextResult()
            ner_on = filled_form.cleaned_data['ner']
            sent_2_on = filled_form.cleaned_data['sent_2']
            sent_11_on = filled_form.cleaned_data['sent_11']
            if ner_on or sent_2_on or sent_11_on:
                if ner_on:
                    ner_text = 'ner on '
                else:
                    ner_text = ''
                if sent_2_on :
                    sent_2_text = 'sent 2 on'
                else:
                    sent_2_text = ''
                if sent_11_on:
                    sent_11_text = 'sent 11 on'
                else:
                    sent_11_text =''

                return render(request, 'nlpmodules/English.html', {'form': form, 'returned_text': returned_text, 'ner_text' : ner_text, 'sent_2_text': sent_2_text, 'sent_11_text': sent_11_text})

            else:
                error = 'Need to have at least one of the modules selected!!! '
                return render(request, 'nlpmodules/English.html', {'form': form, 'error': error})

            #if filled_form.cleaned_data['ner']:
#                ner_text = 'Ner is on!'
#            if filled_form.cleaned_data['sent_2']:
#                result_form['sent_2_result'] =
#            if filled_form.cleaned_data['sent_11']:
#                result_form['sent_11_result']
            #ner_result = forms.CharField(max_length = 4000)
    else:
    #Analyze with the added text
        return render(request, 'nlpmodules/English.html', {'form': form})



def spanish(request):
    return render(request, 'nlpmodules/Spanish.html')

def romanian(request):
    return render(request, 'nlpmodules/Romanian.html')

def multilanguages(request):
    return render(request, 'nlpmodules/MultiLanguages.html')
