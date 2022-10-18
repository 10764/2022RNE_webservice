import streamlit as st
import pandas as pd
from PIL import Image

st.title('연구결과')

with st.sidebar :
    gubun = st.radio("열람하고 싶은 결과를 선택하세요.", ("토지 및 인구 관련 요인", "주민 유형", "치안 관련 요인", "건물 유형"))


data = pd.read_csv('유흥주점비율.csv')
img = Image.open('graph.png')

st.dataframe(data)
st.image(img)