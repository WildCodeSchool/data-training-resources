from zyphra import ZyphraClient

client = ZyphraClient(api_key="API_KEY")

# Text-to-speech
audio_data = client.audio.speech.create(
    text="Je suis le meilleur élève de la classe.",
    speaking_rate=15,
    language_iso_code = 'fr-fr',
    output_path="output.webm"
)