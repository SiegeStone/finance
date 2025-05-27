# https://github.com/financedata-org/FinanceDataReader
# pip install finance-datareader

import FinanceDataReader as fdr
import streamlit as st
import datetime

# date_input : UI제목, 초기값
# text_input : UI제목, 초기값, placeholder(표시 내용)

with st.sidebar : # 사이드바
    date = st.date_input("조회 시작일을 선택해 주세요.", datetime.datetime(2024, 1, 1)) # 날짜 선택 UI
    code = st.text_input('종목코드', value = '', placeholder = '종목코드를 입력해 주세요.') # 종목코드 입력 UI

if code and date : 
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending = True).loc[:,'Close'] # df, 종가(Close)열로 정렬
    # st.line_chart(data)
    tab1, tab2 = st.tabs(['차트', '데이터']) # 탭 UI

    with tab1 : # 그래프 탭
        st.line_chart(data)
    with tab2 : # 표 탭
        st.dataframe(df.sort_index(ascending = False)) # 정렬
    with st.expander('컬럼 설명') : # 확장 UI(각 컬럼의 의미 표시 목적)
        st.markdown('''
         - Open : 시가
         - High : 고가
         - Low : 저가
         - Close : 종가
         - Adj Close : 수정 종가
         - Volume : 거래량
        ''') # 표시 내용(이건 표의 컬럼명이 아니다. 처음에 혼동했다.) 