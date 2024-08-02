from django.shortcuts import render, redirect
from translator import codes_languages, translator

def home(request):
    codes, languages = codes_languages()
    return render(request, 'index.html', {
        'codes_and_languages': zip(codes, languages),
        'codes_languages': zip(codes, languages)
    })

def get_data_and_translate(request):
    if request.method == 'POST':
        inp_val = request.POST.get('input_language_code')
        out_val = request.POST.get('output_language_code')
        result = translator(inp_val, out_val)
        
        codes, languages = codes_languages()

        error = result.get('error', None)
        user_said = result.get('user_saying', None)
        translation_text = result.get('converted', None)

        context = {
            'codes_and_languages': zip(codes, languages),
            'codes_languages': zip(codes, languages),
            'error': error
        }

        if user_said:
            context['input'] = user_said
        if translation_text:
            context['trans'] = translation_text

        return render(request, 'index.html', context)
    else:
        return redirect('home')
