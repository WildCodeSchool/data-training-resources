import streamlit as st
import asyncio
import nest_asyncio
from zyphra import AsyncZyphraClient, ZyphraError
import base64

# Apply nest_asyncio to allow nested event loops (helps when running in Streamlit)
nest_asyncio.apply()

# Retrieve the Zyphra API key

# Replace with your actual API key or use st.secrets["api_key"] if using Streamlit Secrets
API_KEY = "API_KEY"

with open("record_out.wav", "rb") as f:
    speaker_audio = base64.b64encode(f.read()).decode('utf-8')  

async def generate_audio_tts(text: str, speaking_rate: int, language_iso_code: str, mime_type: str, speaker_audio):
    """
    Asynchronously generate speech audio from text using the Zyphra API.
    """
    async with AsyncZyphraClient(api_key=API_KEY) as client:
        audio_data = await client.audio.speech.create(
            text=text,
            speaker_audio=speaker_audio,
            speaking_rate=speaking_rate,
            language_iso_code=language_iso_code,
            mime_type=mime_type
        )
    return audio_data

def main():
    st.title("Text-to-Speech with Zyphra (Async)")
    st.write("Rentrez du texte afin de pouvoir transcrire.")

    # User inputs
    text_input = st.text_area("Enter text to synthesize:", height=150)
    speaking_rate = st.slider("Speaking rate", min_value=5, max_value=35, value=15)
    language = st.selectbox("Language", options=["en-us", "fr-fr", "de", "ja", "ko", "cmn"], index=0)
    mime_type = st.selectbox("Output Format", 
                             options=["audio/webm", "audio/ogg", "audio/wav", "audio/mp3", "audio/mpeg", "audio/mp4", "audio/aac"],
                             index=0)

    if st.button("Generate Audio"):
        if not text_input.strip():
            st.error("Please enter some text before generating audio.")
        else:
            st.info("Generating audio... please wait.")
            try:
                # Run the asynchronous function. The use of nest_asyncio allows asyncio.run() here even if an event loop is already running.
                audio_data = asyncio.run(
                    generate_audio_tts(
                        text=text_input,
                        speaker_audio=speaker_audio,
                        speaking_rate=speaking_rate,
                        language_iso_code = language,
                        mime_type=mime_type
                    )
                )
                
                st.success("Audio generated successfully!")
                # Play the generated audio in the Streamlit app
                st.audio(audio_data, format=mime_type)
            except ZyphraError as e:
                st.error(f"Zyphra API Error: {e.status_code} - {e.response_text}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
