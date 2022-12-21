import streamlit as st
import pathlib
from PIL import Image
st.title("DR. MAHMOUD SITE.")
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('blue_bg.png')    

#image = Image.open("C:/medo1.jpg")
#st.image(image,use_column_width=True)
url="https://github.com/dentist118/year/blob/main/awesome-gif.gif"
st.image(url)
n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

