from django.shortcuts import render
from .forms import TextForm, TextResult
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
            text = filled_form.cleaned_data['body']
            result_form = TextResult()
            if filled_form.cleaned_data['ner']:

            if filled_form.cleaned_data['sent_2']:
                result_form['sent_2_result'] =
            if filled_form.cleaned_data['sent_11']:
                result_form['sent_11_result']
            ner_result = forms.CharField(max_length = 4000)

    else:

    #Analyze with the added text
    return render(request, 'nlpmodules/English.html', {'form': form})



def spanish(request):
    return render(request, 'nlpmodules/Spanish.html')

def romanian(request):
    return render(request, 'nlpmodules/Romanian.html')

def multilanguages(request):
    return render(request, 'nlpmodules/MultiLanguages.html')
