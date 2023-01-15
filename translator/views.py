from django.shortcuts import render
from . import translate
#from .models import Post
#from django.views import generic
# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        print(original_text)
        output = translate.translate(original_text)
        return render(request, 'translate.html', {'output_text': output, 'my_textarea': original_text})
    else:
        return render(request, 'translate.html')