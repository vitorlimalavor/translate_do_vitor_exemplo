import streamlit as st
import pprint
import asyncio
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

st.title("Super Tradutor do Vitor")
async def translate_text(phrase,src,dest):
    async with Translator() as translator:
        
        result = await translator.translate(phrase, src=src, dest=dest)
        return result  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>


def voice(phrase):
    mp3_fp = BytesIO()
    tts = gTTS(phrase, lang='en')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp


phrase = st.text_input("Type your phrase")
if st.button("Traduzir"):
    with st.spinner("Gerando conteúdo..."):
            content = asyncio.run(translate_text(phrase,'pt','en'))          
            st.success("Translation: ")
            st.text_area("Translation: ",content.text, height=70)
            audio_test = voice(content.text)
            st.success("Voice")
            st.audio(audio_test, format="audio/mpeg")









