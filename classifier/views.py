from django.shortcuts import render
from .forms import ClassificationForm
from .utils import forecast_class

def home(request):
    result = None
    
    if request.method == 'POST':
        form = ClassificationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = forecast_class(text)
    else:
        form = ClassificationForm()
    
    return render(request, 'classifier/home.html', {
        'form': form,
        'result': result,
    })