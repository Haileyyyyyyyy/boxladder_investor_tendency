import json
import requests
import streamlit as st
import time
import elasticsearch
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title = "BOX LADDER",
    page_icon = "🌏"
    
)

st.title("BOX LADDER")

st.subheader("SERVICE 1: FIND INVEST TENDENCY ")
st.info("Decode your investment preferences into 4-letter codes derived from the latest investment data and visualize them. Discover your investment personality effortlessly through our service and tailor your investment strategies accordingly.\n\n 최신 투자 데이터를 기반으로한 투자 선호도를 4자의 문자로 해석하고 시각화합니다. 저희 서비스를 통해 투자 성향을 손쉽게 발견하고 이에 맞게 투자 전략을 설계하세요.", icon ="🌐")

# 이미지 파일 경로
image_path = './img/dashboard.png' 
# 이미지를 화면에 표시
st.write("ElasticSearch의 dashboard로 데이터를 시각화하여 실시간으로 변화하는 데이터를 반영합니다")
st.image(image_path, caption='INVEST TENDENCY dashboard', use_column_width=True)

st.subheader("SERVICE 2: INVESTOR SEARCH ENGINE")
st.info("The 'Investment Firm Search Engine' service is an online tool that leverages the latest investment firm information to help investors quickly and efficiently find the investment firms they are looking for. \n \n 이 서비스는 최신 투자 회사 정보를 활용하여 투자자가 빠르고 효율적으로 원하는 투자 회사를 찾을 수 있도록 도와주는 검색엔진입니다.", icon="🌐")
# 이미지 파일 경로
image_path = './img/stack2.png' 
# 이미지를 화면에 표시
st.image(image_path, caption='our technology stack', use_column_width=True)
