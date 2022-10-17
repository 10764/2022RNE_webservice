import streamlit as st
import pandas as pd
from PIL import Image

st.title('상관관계 : 유흥주점과 강력범죄율')

data = pd.read_csv('유흥주점비율.csv')
img = Image.open('Mangnyangnyang/RNE_sample/KakaoTalk_20221017_132830006.png')

st.dataframe(data)
st.image(img)