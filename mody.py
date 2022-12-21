import streamlit as st
import pathlib
from PIL import Image
st.title("DR. MAHMOUD SITE.")

#image = Image.open("C:/medo1.jpg")
#st.image(image,use_column_width=True)


n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

