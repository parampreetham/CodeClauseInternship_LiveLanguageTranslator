from django.shortcuts import render, redirect
from .models import Language, Translation
from googletrans import Translator

def create_languages():
    languages = [
        "English",
        "Spanish",
        "French",
        "German",
        "Chinese",
        "Japanese",
        "Korean",
        "Russian",
        "Arabic",
        "Hindi",
        "Bengali",
        "Portuguese",
        "Italian",
        "Turkish",
        "Dutch",
        "Swedish",
        "Gujarati",
        "Punjabi",
        "Kannada",
        "Tamil",
        # Add more languages here
    ]

    for language_name in languages:
        Language.objects.get_or_create(name=language_name)


def translator(request):
    languages = Language.objects.all()
    translations = Translation.objects.all()[:10]  # Fetch recent translations
    original_text = ''
    translated_text = ''  # Add this line to initialize translated_text

    if request.method == 'POST':
        if 'translate' in request.POST:
            original_text = request.POST['original_text']
            source_language_id = request.POST['source_language']
            target_language_id = request.POST['target_language']

            source_language = Language.objects.get(id=source_language_id)
            target_language = Language.objects.get(id=target_language_id)

            translator = Translator()
            translated_text = translator.translate(original_text, src=source_language.name, dest=target_language.name).text

            Translation.objects.create(
                original_text=original_text,
                translated_text=translated_text,
                source_language=source_language,
                target_language=target_language
            )

        elif 'reset_original' in request.POST:
            original_text = ''
            translated_text = ''  # Reset translated_text when resetting original_text

        elif 'clear_history' in request.POST:
            Translation.objects.all().delete()

    return render(request, 'translator_app/translator.html', {
        'languages': languages,
        'translations': translations,
        'original_text': original_text,
        'translated_text': translated_text,  # Include translated_text in the context
    })

