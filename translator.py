import streamlit as st
import pprint
import asyncio
from googletrans import Translator

st.title("Super Tradutor do Vitinho")




async def translate_text(phrase,src,dest):
    async with Translator() as translator:
        
        result = await translator.translate(phrase, src=src, dest=dest)
        return result  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>


phrase = st.text_input("Type this phrase")
if st.button("Traduzir"):
    with st.spinner("Gerando conteúdo..."):
            content = asyncio.run(translate_text(phrase,'en','pt'))          
            st.success("Successful Translation ")
            st.text_area("Translation: ",content, height=200)
    











