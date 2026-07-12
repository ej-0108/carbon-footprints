import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from graph_sine import show_sine_tab
from graph_moving_average import show_moving_average_tab
from graph_digital_carbon import show_carbon_calculator_tab

# 웹페이지 기본 설정
st.set_page_config(page_title="클래스 스텝 업 / 기후 위기", layout="centered")

#웹사이트 타이틀 및 설명
st.title("🌱기후 위기, 얼마나 아시나요?")

#수정할 것 
st.write("3개의 탭으로 기후 위기를 설명하고자 합니다.")
st.write("삼각함수로 보는 한국 기후 : 한국의 기후 변화를 삼각함수 기반 그래프로 볼 수 있습니다. 삼각함수의 계수를 통해 기후 변화를 직관적으로 이해할 수 있습니다.")
st.write("이동평균선으로 보는 한국 기후 : 한국의 기후 변화를 이동평균선 기반 그래프로 볼 수 있습니다. 삼각함수에 비해 사실적입니다.")
st.write("디지털 기기 사용시간에 따른 기후 위기 : 입력한 디지털 기기 사용시간에 따라 개인의 탄소배출량이 얼마나 증가하는지 볼 수 있습니다.")
st.write("---")

#전처리된 파일 업로드
df_1940 = pd.read_csv("1940_최종.csv",encoding="cp949")
df_2025 = pd.read_csv("2025_최종.csv",encoding="cp949")

#탭
target_col = "평균기온(℃)"
tab1, tab2, tab3 =st.tabs(["삼각함수로 보는 한국 기후", "이동평균선으로 보는 한국 기후", "디지털 기기 사용시간에 따른 기후 위기"])
with tab1:
  show_sine_tab(df_1940, df_2025, "평균기온(℃)")
with tab2:
  show_moving_average_tab(df_1940, df_2025, target_col)
with tab3:
    show_carbon_calculator_tab()
