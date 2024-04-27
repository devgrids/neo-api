# from ai.text_to_speech.google_text_to_speech import GoogleTextToSpeech

# text_to_speech = GoogleTextToSpeech()

# text_to_speech.generate("Probando la api de google que convierte texto a audio", "data.mp3", "es")

from ai.automatic_speech_recognition.facebook_automatic_speech_recognition import FacebookAutomaticSpeechRecognition

automatic_speech_recognition = FacebookAutomaticSpeechRecognition()

print(automatic_speech_recognition.generate("data.mp3"))