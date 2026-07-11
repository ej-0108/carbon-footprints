import streamlit as st
import pandas as pd
fromgraph_sine import show_sine_tab

# 웹페이지 기본 설정
st.set_page_config(page_title="클래스 스텝 업 / 기후 위기", layout="centered")

#웹사이트 타이틀 및 설명
st.title("🌱")

#수정할 것 
st.write("한국의 기후 변화를 2가지 그래프로 볼 수 있습니다.")
st..write("입력한 디지털 기기 사용시간에 따라 개인의 탄소배출량이 얼마나 증가하는지 볼 수 있습니다.")
st.write("---")

#전처리된 파일 업로드
df_1940 = pd.read_csv("1940_최종.csv",encoding="cp949")
df_2025 = pd.read_csv("2025_최종.csv",encoding="cp949")

#탭
tab1, tab2=st.tabs("삼각함수로 보는 한국 기후", "이동평균선으로 보는 한국 기후")
