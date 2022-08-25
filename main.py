import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# config
st.set_page_config(
    page_title="COVID-19 Coughing Detector",
    page_icon="🤒",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# title
title('COVID-19 Coughing Detector')

# 코로나 증상
section('코로나19 주요 증상 안내')

line_break()

image = Image.open('images/코로나증상.png')
st.image(image,)

line_break()

st.markdown('여러분이 앓고 있는 증상은 무엇인가요?')
agree1 = st.checkbox('발열')
agree2 = st.checkbox('기침')
agree3 = st.checkbox('몸살')
agree4 = st.checkbox('인후통')

if agree1 or agree2 or agree3 or agree4:
     st.markdown('코로나19 증상이 있군요! 코로나 검사가 필요할 것 같아요.')

line_break()
line_break()

callout(['현재 집에 진단키트가 없으신가요?',
         '',
        'COVID-19의 두드러진 증상은 기침과 호흡 곤란을 포함합니다.',
        'AI 기술을 활용하여 기침 소리로부터 COVID-19에 대한 유용한 통찰력을 얻을 수 있습니다.',
        '기침 소리로부터 COVID-19를 검출하는 새로운 진단 도구를 사용해보세요!'])

line_break()
line_break()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        #### Step1
        """
    )
    st.image("images/step1.jpg")

with col2:
    st.markdown(
        """
        #### Step2
        """
    )
    st.image("images/step2.jpg")

with col3:
    st.markdown(
        """
        #### Step3
        """
    )
    st.image("images/step2.jpg")
