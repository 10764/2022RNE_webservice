import streamlit as st
import pandas as pd
from PIL import Image

with st.sidebar :
    gubun = st.selectbox("열람하고 싶은 결과를 선택하세요.", ("강력범죄간 상관관계", "토지 및 인구 관련 요인", "주민 유형", "치안 관련 요인", "건물 유형"))

if gubun == "강력범죄간 상관관계" :
    st.title("강력범죄간 상관관계")
    t1, t2 = st.tabs(["범죄 수", "범죄율"])
    with t1 :
        st.subheader('범죄 수')
        data = pd.read_csv('범죄간상관관계.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('범죄간상관관계사진.png')
        st.image(image, caption = '강력범죄간 상관관계')
    with t2 :
        st.subheader('범죄율')
        data = pd.read_csv('범죄율간상관관계.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('범죄율간상관관계사진.png')
        st.image(image, caption = '강력범죄의 범죄율간 상관관계')

elif gubun == "토지 및 인구 관련 요인" :
    st.title("토지 및 인구 관련 요인")
    t1, t2, t3 = st.tabs(["공시지가", "인구", "행정구역 면적"])

elif gubun == "주민 유형" :
    st.title("주민 유형")
    t1, t2, t3 = st.tabs(["연령구간별 인구수", "세대당 인구", "기초생활수급자 수"])

elif gubun == "치안 관련 요인" :
    st.title("치안 관련 요인")
    t1, t2 = st.tabs(["CCTV 개수", "치안센터 수"])
    with t1 :
        st.subheader('CCTV 개수')
        data = pd.read_csv('CCTV개수.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('CCTV개수.png')
        st.image(image, caption = 'CCTV 개수')
        st.subheader('단위면적당 CCTV 개수 비율')
        data = pd.read_csv('CCTV개수비율(면적).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('CCTV개수비율(면적)사진.png')
        st.image(image, caption = '단위면적당 CCTV 개수 비율')
        st.subheader('단위인구당 CCTV 개수 비율')
        data = pd.read_csv('CCTV개수비율(인구).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('CCTV개수비율(인구)사진.png')
        st.image(image, caption = '단위인구당 CCTV 개수 비율')
    with t2 :
        st.subheader('치안센터 수')
        data = pd.read_csv('치안센터수.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('치안센터수사진.png')
        st.image(image, caption = '치안센터 수')
        st.subheader('단위면적당 치안센터 비율')
        data = pd.read_csv('치안센터수비율(면적).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('치안센터비율(면적)사진.png')
        st.image(image, caption = '단위면적당 치안센터 비율')
        st.subheader('단위인구당 치안센터 비율')
        data = pd.read_csv('치안센터수비율(인구).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('치안센터수비율(인구)사진.png')
        st.image(image, caption = '단위인구당 치안센터 비율')

else :
    st.title("건물 유형")
    t1, t2, t3, t4 = st.tabs(["유치원", "학교", "학원", "유흥주점"])