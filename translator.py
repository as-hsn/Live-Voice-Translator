import googletrans
import speech_recognition as sr

def codes_languages():
    LANGUAGES = googletrans.LANGUAGES
    codes = list(LANGUAGES.keys())
    languages = list(LANGUAGES.values())
    return codes, languages

def translator(inp_lan, out_lan):
    user_said = None
    translate_text = None
    error = None

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # Recognize speech
        text = recognizer.recognize_google(audio, language=inp_lan)
        user_said = text
        # print(f"Recognized text: {user_said}")

        # Translate recognized speech
        if user_said:
            translator = googletrans.Translator()
            translation = translator.translate(text=user_said, dest=out_lan)
            translate_text = translation.text
            # print(f"Translated text: {translate_text}")
        else:
            error = "No speech recognized."

    except sr.UnknownValueError:
        error = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        error = f"Could not request results from Google Speech Recognition service; {e}"
    except ValueError as e:
        error = f"Value error: {e}"
    except Exception as e:
        error = f"An unexpected error occurred: {e}"
    
    # print(f"Error: {error}")
    
    return {
        'user_saying': user_said,
        'converted': translate_text,
        'error': error
    }
