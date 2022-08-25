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
agree4 = st.checkbox('인후염')

if agree1 & agree2:
     st.markdown('발열과 기침이 있군요!')

line_break()
