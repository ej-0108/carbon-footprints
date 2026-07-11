import streamlit as st
import matplotlib.pyplot as plt

def show_carbon_calculator_tab():
    st.header("UN 제시 기후 예산 대비 디지털 기기 이용 시간에 따른 탄소 배출량")
    st.markdown("""
    매일 반복하는 우리의 디지털 기기 이용 습관이 1년 동안 지속된다면 지구에 어떤 영향을 미칠까요?
    UN 파리기후협정에 따른 1인당 연간 총 탄소 배출 제한량(2,000kg) 중 
    나의 디지털 습관이 차지하는 비중을 도넛 그래프로 확인해 봅니다.
    """)
    
    user_hours = st.slider("하루 평균 디지털 기기(스마트폰, PC 등) 사용 시간:", 0.0, 24.0, 6.0, 0.5)
    
    #탄소 데이터 기준 (1시간 = 50g = 0.05kg 배출)
    CO2_PER_HOUR_KG = 0.05
    UN_ANNUAL_BUDGET_KG = 2000.0  # UN 제한량
    
    # 사용자의 1년 누적 디지털 탄소 배출량 및 남은 예산 계산
    user_annual_co2 = user_hours * CO2_PER_HOUR_KG * 365
    remaining_budget = max(0.0, UN_ANNUAL_BUDGET_KG - user_annual_co2)
    
    # 차지하는 비율(%)
    percentage = (user_annual_co2 / UN_ANNUAL_BUDGET_KG) * 100
    
    # 3. 분석 결과 안내 문구
    st.write("---")
    st.subheader("1년 누적 시뮬레이션 결과")
    
    st.markdown(f"""
    > 하루 평균 {user_hours}시간 사용 습관이 1년간 지속될 경우:
    > * 나의 연간 디지털 탄소 배출량: :red[{user_annual_co2:.1f} kg]
    > * 이는 UN이 제시한 1인당 연간 총 탄소 예산({UN_ANNUAL_BUDGET_KG:,.0f} kg)의 **:orange[{percentage:.1f}%]**를 차지합니다.
    """)
    
    st.write("---")
    st.markdown("##### UN 연간 탄소 예산 중 디지털 배출량의 비중")
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # 도넛 차트 데이터 설정
    labels = ['My Digital CO2', 'Remaining Budget\n(Food, Transport, etc.)']
    sizes = [user_annual_co2, remaining_budget]
    colors = ['#e74c3c', '#2ecc71'] # 내 배출량은 경고의 빨간색, 남은 예산은 안전한 초록색
    
    # 도넛 모양을 만들기 위해 wedgeprops(두께 비율 지정) 사용
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors,
        textprops=dict(color="w", weight="bold", fontsize=11), # 글자 색상 및 크기
        pctdistance=0.75, # 퍼센트 글자 위치
        wedgeprops=dict(width=0.3, edgecolor='none') # 도넛 두께 (0.3만큼만 채우기)
    )
    
    # 그래프 텍스트 가독성을 위해 배경 테마에 맞춰 라벨 색상 조정
    for text in texts:
        text.set_color('#f5f5f5')
    for autotext in autotexts:
        autotext.set_color('#ffffff')
        autotext.set_fontsize(12)
        
    # 도넛 한가운데 구멍에 차지하는 총 퍼센트 텍스트 넣기
    ax.text(0, 0, f'{percentage:.1f}%\nOccupied', ha='center', va='center', 
            fontsize=16, weight='bold', color='#ffdd57')
    
    # 그래프 배경을 투명하게 하거나 웹 테마에 맞추기
    fig.patch.set_facecolor('#0a0a0a')
    ax.set_facecolor('#0a0a0a')
    
    st.pyplot(fig)

    # 4. [핵심 기능] 세계은행·ITU 통계 기반 조건문 판정 및 텍스트 출력
    # 기준: 세계 ICT 탄소 점유율(1.5%~4.0%)을 기반으로 개인 예산 할당량 최적화 판정
    if percentage < 2.0:
        st.success(f"""
        ### **[안전]**(점유율: {percentage:.1f}%)
        * 세계은행(World Bank) 및 ITU가 발표한 글로벌 디지털 부문 탄소 배출 비중(1.5%~4%)의 최하단에 위치
        """)
    elif percentage < 5.0:
        st.warning(f"""
        ### **[주의]** 디지털 예산 과소비 경계 등급 (점유율: {percentage:.1f}%)
        * 현재 글로벌 전체 산업 중 디지털 섹터가 차지하는 평균적인 탄소 점유율 수준
        * UN이 규정한 1인당 총 탄소 예산의 핵심 생존 영역을 서서히 압박하기 시작하는 단계입니다. 불필요한 스크린 타임을 줄이는 노력이 필요합니다.
        """)
    else:
        st.error(f"""
        ### **[위험]** 기후 배출 마지노선 초과 등급 (점유율: {percentage:.1f}%)
        * 디지털 기기로 인한 탄소 배출량이 총 탄소 예산의 5% 이상을 차지
        * 이 패턴이 1년간 유지된다면, 다른 모든 생활(먹거리, 대중교통 이용 등)에서 탄소 배출을 극단적으로 차단해야 합니다.
        """)
  
    
