import streamlit as st
import pandas as pd
from PIL import Image

st.title('연구결과')
st.write('ㅋㅋㅋ')

data = pd.read_csv('유흥주점비율.csv')
img = Image.open('graph.png')

st.dataframe(data)
st.image(img)