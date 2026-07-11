import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def show_moving_average_tab(df_1940, df_2025, target_col):
    st.header("이동평균선 기반 1940년과 2025년 한국 기후 비교")
    st.markdown("""
    하루하루 들쭉날쭉한 기온 변동(노이즈)을 제거하기 위해 15일 이동평균선을 적용한 그래프입니다. 
    """)
    
    # 1. 15일 이동평균 데이터 계산 (rolling 함수 사용)
    # center=True를 주면 앞뒤 일주일을 평균 내어 날짜 타이밍이 밀리지 않습니다.
    df_1940['MA'] = df_1940[target_col].rolling(window=15, min_periods=1, center=True).mean()
    df_2025['MA'] = df_2025[target_col].rolling(window=15, min_periods=1, center=True).mean()
    
    # 2. 그래프 시각화
    fig, ax = plt.subplots(figsize=(11, 4.5))
    
    ax.plot(df_1940['julian_date'], df_1940['MA'], color='blue', linewidth=2, label='1940 (15-day MA)')
    ax.plot(df_2025['julian_date'], df_2025['MA'], color='red', linewidth=2, label='2025 (15-day MA)')
    
    ax.set_xlabel("Julian Date (Day of the Year)")
    ax.set_ylabel("Temperature (℃)")
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    
    st.pyplot(fig)
    
    st.write("---")
    
    # 이동평균선의 장점 분석
    st.subheader("이동평균선 그래프 장점")
    st.markdown("""
    삼각함수 기반 그래프 대비 이동평균선 그래프는 어떤 장점이 있을까요?
    > ① 실제 기후의 불규칙성을 반영해 과소적합 문제를 해결
    > 삼각함수 기반 그래프는 전반적인 기후 추세를 한 눈에 파악하고자 일정한 대칭성을 갖도록 데이터를 맞춥니다.
    > 이동평균선 그래프는 데이터를 있는 그대로 반영합니다.
    
    > ② 특이 기후 현상 포착
    > 삼각함수 기반 그래프는 데이터를 삼각함수 형태에 맞춥니다.
    > 이동평균선 기반 그래프는 15일 단위로 그려집니다. 따라서 각 해의 구체적인 기후 위기 징후를 알 수 있습니다.
    """)
    
    
