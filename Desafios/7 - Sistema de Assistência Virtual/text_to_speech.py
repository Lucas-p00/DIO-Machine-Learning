from gtts import gTTS

def translation(text, language, arquive):
    gtts_object = gTTS(text = text, 
                  lang = language,
                  slow = False)
    gtts_object.save(f'audios/{arquive}')

text = input("Digite sua frase em português:\n")

translation(text, "pt", "audio.wav")