import streamlit as st
import pandas as pd

st.title('상관관계 : 유흥주점과 강력범죄율')

data = pd.read_csv('유흥주점비율.csv')

st.dataframe(data)