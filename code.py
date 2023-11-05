import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import easyocr
import mysql.connector as sql
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
import re

# SETTING PAGE CONFIGURATIONS
icon = Image.open("icon.png")
st.set_page_config(page_title= "BizCardX: Extracting Business Card Data with OCR | By Nikita Y P",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This OCR app is created by *Nikita Y P*!"""})
st.markdown("<h1 style='text-align: center; color: white;'>BizCardX: Extracting Business Card Data with OCR</h1>", unsafe_allow_html=True)

# SETTING-UP BACKGROUND IMAGE
def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background: url("https://cutewallpaper.org/22/plane-colour-background-wallpapers/189265759.jpg");
                        background-size: cover}}
                     </style>""",unsafe_allow_html=True) 
setting_bg()

# CREATING OPTION MENU
selected = option_menu(None, ["Home","Upload & Extract","Modify"], 
                       icons=["house","cloud-upload","pencil-square"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "0px", "--hover-color": "#6495ED"},
                               "icon": {"font-size": "35px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#6495ED"}})

# INITIALIZING THE EasyOCR READER
reader = easyocr.Reader(['en'])

# CONNECTING WITH MYSQL DATABASE
mydb = sql.connect(host="localhost",
                   user="root",
                   password="your password",
                   database= "bizcardx_db"
                  )
mycursor = mydb.cursor(buffered=True)
