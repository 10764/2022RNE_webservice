import streamlit as st
import pandas as pd
from PIL import Image

st.title('연구결과')

with st.sidebar :
    gubun1 = st.radio("토지 및 인구 관련 요인", ("평균 공시지가", "전체 인구", "도시 인구", "비도시 인구", "도시지역 인구비율", "행정구역 면적", "인구밀도"))
    gubun2 = st.radio("주민 유형", ("세대당 인구", "연령구간별 인구(10세 단위)", "기초생활수급자"))
    gubun3 = st.radio("치안 관련 요인", ("CCTV", "치안센터"))
    gubun4 = st.radio("건물 유형", ("유치원", "초·중·고등학교", "대학교", "학원", "유흥주점"))


data = pd.read_csv('유흥주점비율.csv')
img = Image.open('graph.png')

st.dataframe(data)
st.image(img)