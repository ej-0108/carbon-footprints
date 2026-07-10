import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# 웹페이지 기본 설정
st.set_page_config(page_title="클래스 스텝 업 / 기후 데이터 분석", layout="centered")
#웹사이트 타이틀 및 설명
st.title("🌱")
st.write("기후 위기, 얼마나 아시나요?\n산업화 이전 대비 지구 온도가 1.5도 상승하는 지점이 지구 온난화를 돌이킬 수 없는 임계점이라는 것은 널리 알려져 있습니다.\n이미 전 지구 평균 기온이 약 1.6도 상승하여 위험한 상황이라는 점도요.\n그렇다면 이러한 상황에서, 한국의 기후는 얼마나 변했을까요?")
st.write("---")
st.header("📊삼각함수 기반 1940년과 2025년 한국 기후 비교")
def sine_moel(X,a,b,c,d):
  return a*np.sin(b*(X+c)*(np.pi/720))+d
#전처리된 파일 업로드
try:
  df
