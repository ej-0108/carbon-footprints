import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
# 웹페이지 기본 설정
st.set_page_config(page_title="클래스 스텝 업 / 기후 데이터 분석", layout="centered")
#웹사이트 타이틀 및 설명
st.title("🌱")
st.markdown("**기후 위기, 얼마나 아시나요?**")
st.markdown("산업화 이전 대비 지구 온도가 **1.5도** 상승하는 지점이 지구 온난화를 돌이킬 수 없는 임계점이라는 것은 널리 알려져 있습니다.")
st.write("이미 전 지구 평균 기온이 약 1.6도 상승하여 위험한 상황이라는 점도요.")
st.write("그렇다면 이러한 상황에서, 한국의 기후는 얼마나 변했을까요?")
st.write("---")
st.header("삼각함수 기반 1940년과 2025년 한국 기후 비교")
def sine_model(X,a,b,c,d):
  return a*np.sin(b*(X+c)*(np.pi/720))+d
#전처리된 파일 업로드
try:
    df_1940 = pd.read_csv("1940_최종.csv",encoding="cp949")
    df_2025 = pd.read_csv("2025_최종.csv",encoding="cp949")
   # 데이터 행 순서대로 1일부터 365일까지의 X축(julian_date)을 자동으로 생성
    df_1940['julian_date'] = df_1940.index + 1
    df_2025['julian_date'] = df_2025.index + 1
except FileNotFoundError:
    st.error("⚠️ '1940_최종.csv' 또는 '2025_최종.csv' 파일을 찾을 수 없습니다. 두 파일이 app.py와 같은 폴더에 업로드되어 있는지 확인해 주세요.")
    st.stop()
except UnicodeDecodeError:
# cp949 실패 시 utf-8-sig로 재시도하는 안전장치
    try:
        df_1940 = pd.read_csv("1940_최종.csv", encoding="utf-8-sig")
        df_2025 = pd.read_csv("2025_최종.csv", encoding="utf-8-sig")
        df_1940['julian_date'] = df_1940.index + 1
        df_2025['julian_date'] = df_2025.index + 1
    except Exception as e:
        st.error(f"⚠️ 파일 인코딩 에러가 지속됩니다: {e}")
        st.stop()
target_col="평균기온(℃)"
y_label="기온(℃)"
graph_title= "1940년과 2025년 서울 평균기온 삼각함수 모형 비교"
initial_guess=[18,4,246.0,12.0]
# =========================================================================
# 3. 평균기온 전용 설정값 고정 (사이드바 및 선택 기능 제거)
# =========================================================================
target_col = "평균기온(℃)"
y_label = "Temperature (Celsius)"
initial_guess = [18.0, 3.95, -119.0, 12.0]  # 실제 데이터 기반 검증된 초기 추정값 [a, b, c, d]

# =========================================================================
# 4. SciPy 연산 및 그래프 즉시 출력
# =========================================================================
try:
    # SciPy curve_fit을 이용해 오차가 가장 적은 최적의 a, b, c, d 상수 도출
    popt_1940, _ = curve_fit(sine_model, df_1940['julian_date'], df_1940[target_col], p0=initial_guess, maxfev=10000)
    popt_2025, _ = curve_fit(sine_model, df_2025['julian_date'], df_2025[target_col], p0=initial_guess, maxfev=10000)
    
    # 1일부터 365일까지 끊어지지 않는 매끄러운 곡선용 가상 X축 데이터 생성
    x_curve = np.linspace(1, 365, 500)
    y_curve_1940 = sine_model(x_curve, *popt_1940)
    y_curve_2025 = sine_model(x_curve, *popt_2025)
    
    # 메인 그래프 생성
    fig, ax = plt.subplots(figsize=(11, 5))
    
    # 1) 실제 날짜별 평균기온 데이터 점 (산점도 - 흐리게 처리)
    ax.scatter(df_1940['julian_date'], df_1940[target_col], color='blue', alpha=0.12, label='1940 Raw Data')
    ax.scatter(df_2025['julian_date'], df_2025[target_col], color='red', alpha=0.12, label='2025 Raw Data')
    
    # 2) 수학적으로 추정된 매끄러운 사인 함수 곡선 추가
    ax.plot(x_curve, y_curve_1940, color='blue', linewidth=2.5, label='1940 Sine Model')
    ax.plot(x_curve, y_curve_2025, color='red', linewidth=2.5, label='2025 Sine Model')
    
    # 그래프 스타일 세팅
    ax.set_xlabel("Day of the Year (Julian Date)")
    ax.set_ylabel(y_label)
    ax.legend(loc="upper right")
    ax.grid(True, linestyle=':', alpha=0.5)
    
    # 스트림릿 웹 화면에 그래프 출력
    st.pyplot(fig)
    
    # 분석
    st.subheader("연도별 삼각함수식")
    col1, col2 = st.columns(2)
    with col1:
            st.markdown("##### :blue[1940년 서울 기온 추세식]")
            st.latex(r"y = %.2f \sin\left(\frac{2\pi}{365}(X %+.1f)\right) %+.2f" % (a_40, c_40, d_40))
            
    with col2:
            st.markdown("##### :red[2025년 서울 기온 추세식]")
            st.latex(r"y = %.2f \sin\left(\frac{2\pi}{365}(X %+.1f)\right) %+.2f" % (a_25, c_25, d_25))
            
            st.write("---")
            st.subheader("계수별 의미")

            # d값 변화 계산 (연평균 기온)
            diff_d = d_225 = d_25 - d_40
        
            st.markdown(f"""
            > **y축 평행이동 상수 >> 한반도 평균기온의 전반적 증가**
            > 사인 곡선 전체의 중심축이 1940년 **{d_40:.2f}℃**에서 2025년 **{d_25:.2f}℃**로 약 **{diff_d:.2f}℃** 상승했습니다.
        
            > **진폭의 변화 >> 이상 기후와 기온 극단화**
            > 중심선에서 최고점까지의 높이를 나타내는 진폭이 1940년 **{a_40:.2f}**에서 2025년 **{a_25:.2f}**로 변화했습니다. 이는 봄과 가을도 여름과 겨울처럼 극단적인 기온으로 변화하고 있음을 뜻합니다.
        
            > **x축 평행이동 >> 생태 시계 교란**
            > 그래프를 좌우로 밀어내는 평행이동 값이 1940년 **{c_40:.1f}**에서 2025년 **{c_25:.1f}**로 이동했습니다. 일년 중 가장 더운 날과 추운 날의 타이밍이 물리적으로 변했음을 의미합니다. 
            > 실제로 한반도의 봄은 일찍 시작되어 벌과 나비가 활동하기 전에 꽃이 지게 됩니다.
            """)
            
except Exception as e:
    st.error(f"수식 연산 및 그래프를 생성하는 중에 오류가 발생했습니다: {e}")
