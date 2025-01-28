from gtts import gTTS

def translation(text, language, arquive):
    gtts_object = gTTS(text = text, 
                  lang = language,
                  slow = False)
    gtts_object.save(f'audios/{arquive}')

translation("How are you doing?", "en", "audio.wav")