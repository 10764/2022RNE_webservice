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
    with t1 :
        st.subheader('평균 공시지가')
        data = pd.read_csv('평균공시지가.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('평균공시지가사진.png')
        st.image(image, caption = '평균 공시지가')
    with t2 :
        st.subheader('전체 인구')
        data = pd.read_csv('전체인구.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('전체인구사진.png')
        st.image(image, caption = '전체 인구')
        st.subheader('인구 밀도')
        data = pd.read_csv('인구밀도.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('인구밀도사진.png')
        st.image(image, caption = '인구 밀도')
        st.subheader('도시 인구')
        data = pd.read_csv('도시인구.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('도시인구사진.png')
        st.image(image, caption = '도시 인구')
        st.subheader('비도시 인구')
        data = pd.read_csv('비도시인구.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('비도시인구사진.png')
        st.image(image, caption = '비도시 인구')
        st.subheader('도시지역 인구 비율')
        data = pd.read_csv('도시지역 인구비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('도시지역 인구비율사진.png')
        st.image(image, caption = '도시지역 인구 비율')
    with t3 :
        st.subheader('행정구역 면적')
        data = pd.read_csv('행정구역 면적.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('행정구역면적사진.png')
        st.image(image, caption = '행정구역 면적')

elif gubun == "주민 유형" :
    st.title("주민 유형")
    t1, t2, t3 = st.tabs(["연령구간별 인구수", "세대당 인구", "기초생활수급자 수"])
    with t1 : 
        st.subheader('0~9세')
        data = pd.read_csv('0~9세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('0~9세사진.png')
        st.image(image, caption = '0~9세')
        st.subheader('0~9세 비율')
        data = pd.read_csv('0~9세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('0~9세비율사진.png')
        st.image(image, caption = '0~9세 비율')
        st.subheader('10~19세')
        data = pd.read_csv('10~19세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('10~19세사진.png')
        st.image(image, caption = '10~19세')
        st.subheader('10~19세 비율')
        data = pd.read_csv('10~19세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('10~19세비율사진.png')
        st.image(image, caption = '10~19세 비율')
        st.subheader('20~29세')
        data = pd.read_csv('20~29세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('20~29세사진.png')
        st.image(image, caption = '20~29세')
        st.subheader('20~29세 비율')
        data = pd.read_csv('20~29세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('20~29세비율사진.png')
        st.image(image, caption = '20~29세 비율')
        st.subheader('30~39세')
        data = pd.read_csv('30~39세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('30~39세사진.png')
        st.image(image, caption = '30~39세')
        st.subheader('30~39세 비율')
        data = pd.read_csv('30~39세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('30~39세비율사진.png')
        st.image(image, caption = '30~39세 비율')
        st.subheader('40~49세')
        data = pd.read_csv('40~49세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('40~49세사진.png')
        st.image(image, caption = '40~49세')
        st.subheader('40~49세 비율')
        data = pd.read_csv('40~49세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('40~49세비율사진.png')
        st.image(image, caption = '40~49세 비율')
        st.subheader('50~59세')
        data = pd.read_csv('50~59세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('50~59세사진.png')
        st.image(image, caption = '50~59세')
        st.subheader('50~59세 비율')
        data = pd.read_csv('50~59세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('50~59세비율사진.png')
        st.image(image, caption = '50~59세 비율')
        st.subheader('60~69세')
        data = pd.read_csv('60~69세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('60~69세사진.png')
        st.image(image, caption = '60~69세')
        st.subheader('60~69세 비율')
        data = pd.read_csv('60~69세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('60~69세비율사진.png')
        st.image(image, caption = '60~69세 비율')
        st.subheader('70~79세')
        data = pd.read_csv('70~79세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('70~79세사진.png')
        st.image(image, caption = '70~79세')
        st.subheader('70~79세 비율')
        data = pd.read_csv('70~79세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('70~79세비율사진.png')
        st.image(image, caption = '70~79세 비율')
        st.subheader('80~89세')
        data = pd.read_csv('80~89세.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('80~89세사진.png')
        st.image(image, caption = '80~89세')
        st.subheader('80~89세 비율')
        data = pd.read_csv('80~89세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('80~89세비율사진.png')
        st.image(image, caption = '80~89세 비율')
        st.subheader('90~99세')
        data = pd.read_csv('행정구역 면적.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('행정구역면적사진.png')
        st.image(image, caption = '90~99세')
        st.subheader('90~99세 비율')
        data = pd.read_csv('90~99세비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('90~99세비율사진.png')
        st.image(image, caption = '90~99세 비율')
        st.subheader('100세 이상')
        data = pd.read_csv('100세 이상.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('100세이상사진.png')
        st.image(image, caption = '100세 이상')
        st.subheader('100세 이상 비율')
        data = pd.read_csv('100세이상비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('100세이상비율사진.png')
        st.image(image, caption = '100세 이상 비율')
    with t2 :
        st.subheader('세대당 인구')
        data = pd.read_csv('세대당인구.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('세대당인구사진.png')
        st.image(image, caption = '세대당 인구')
    with t3 :
        st.subheader('기초생활수급자 수')
        data = pd.read_csv('기초생활수급자수.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('기초생활수급자수사진.png')
        st.image(image, caption = '기초생활수급자 수')
        st.subheader('기초생활수급자 비율')
        data = pd.read_csv('기초생활수급자수비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('기초생활수급자수비율사진.png')
        st.image(image, caption = '기초생활수급자 비율')

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
    with t1 :
        st.subheader('유치원 수')
        data = pd.read_csv('유치원.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('유치원사진.png')
        st.image(image, caption = '유치원 수')
        st.subheader('유치원 비율')
        data = pd.read_csv('유치원비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('유치원비율사진.png')
        st.image(image, caption = '유치원 비율')
    with t2 :
        st.subheader('초·중·고등학교 수')
        data = pd.read_csv('초중고.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('초중고사진.png')
        st.image(image, caption = '초·중·고등학교 수')
        st.subheader('초·중·고등학교 비율')
        data = pd.read_csv('초중고비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('초중고비율사진.png')
        st.image(image, caption = '초·중·고등학교 비율')
        st.subheader('대학교 수')
        data = pd.read_csv('대학교.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('대학교사진.png')
        st.image(image, caption = '대학교 수')
        st.subheader('대학교 비율')
        data = pd.read_csv('대학교비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('대학교비율사진.png')
        st.image(image, caption = '대학교 비율')
    with t3 :
        st.subheader('학원 수')
        data = pd.read_csv('학원.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('학원사진.png')
        st.image(image, caption = '학원 수')
        st.subheader('단위면적당 학원 비율')
        data = pd.read_csv('학원비율(면적).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('학원비율(면적)사진.png')
        st.image(image, caption = '단위면적당 학원 비율')
        st.subheader('단위인구당 학원 비율')
        data = pd.read_csv('학원비율(인구).csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('학원비율(인구)사진.png')
        st.image(image, caption = '단위인구당 학원 비율')
    with t4 :
        st.subheader('유흥주점 수')
        data = pd.read_csv('유흥주점.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('유흥주점사진.png')
        st.image(image, caption = '유흥주점 수')
        st.subheader('유흥주점 비율')
        data = pd.read_csv('유흥주점비율.csv', encoding = 'cp949')
        st.dataframe(data, use_container_width = True)
        image = Image.open('유흥주점비율사진.png')
        st.image(image, caption = '유흥주점 비율')

