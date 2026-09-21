import streamlit as st
import pandas as pd
import os
import base64
from add_plant import add_new_plant
from record_care import record_plant_care
from due_for_care import view_plants_due_for_care
from search_plants import search_plants
from view_all_plants import view_all_plants
from growth import track_growth
from seasonal_reminders import seasonal_care_reminders
from photos import add_plant_photo
from seasonal_schedule import adjust_seasonal_schedule
from plant_diagnosis import diagnose_plant
from plant_chat import plant_care_chat
st.set_page_config(page_title="Plant Care Tracker",page_icon="🌿",layout="wide")
st.markdown("""
<style>
[data-testid="stSidebar"] {
background-color: #E8F5E9;
}
.stButton > button {
background-color: #2E7D32;
color: white;
border: none;
border-radius: 8px;
}
.stButton > button:hover {
background-color: #1B5E20;
color: white;
}
div[role="radiogroup"] label:has(input:checked) {
background-color: #C8E6C9;
border-radius: 8px;
padding: 5px;
}
h1, h2, h3 {
color: #1B5E20;
}
[data-baseweb="input"] {
background-color: #DDEEDD;
border-radius: 8px;
}
[data-baseweb="input"] input {
background-color: #DDEEDD;
}
[data-testid="stNumberInput"] input {
background-color: #DDEEDD;
}
textarea {
background-color: #DDEEDD !important;
}
[data-baseweb="select"] > div {
background-color: #DDEEDD;
}
[data-testid="stDateInput"] input {
background-color: #DDEEDD;
}
[data-testid="stMetric"] {
background-color: #DDEEDD;
border: 1px solid #81A784;
border-radius: 10px;
padding: 15px;
}
[data-testid="stDataFrame"] {
background-color: #E8F5E9;
border: 2px solid #81A784;
border-radius: 10px;
padding: 5px;
}
[data-testid="stAlert"] {
background-color: #DDEEDD;
border: 1px solid #81A784;
border-radius: 10px;
}
[data-testid="stForm"] {
background-color: rgba(221,238,221,0.90);
border: 1px solid #81A784;
border-radius: 10px;
padding: 20px;
}
[data-testid="stExpander"] {
background-color: #E8F5E9;
border-radius: 10px;
}
[data-testid="stFileUploader"] {
background-color: #E8F5E9;
border-radius: 10px;
padding: 10px;
}
</style>
""",unsafe_allow_html=True)
def set_background(image):
    if os.path.exists(image):
        file=open(image,"rb")# READ
        image_data=base64.b64encode(file.read()).decode()
        file.close() #NO RESOURCE
        st.markdown(f"""
        <style>
        .stApp {{
        background-image: linear-gradient(rgba(255,255,255,0.55),rgba(255,255,255,0.55)),url("data:image/png;base64,{image_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        }}
        </style>
        """,unsafe_allow_html=True)
st.sidebar.title("🌿 Plant Care")
st.sidebar.write("Keep your plants happy and healthy.")
option=st.sidebar.radio("Menu",["🏠 Dashboard","➕ Add New Plant","💧 Record Care","⏰ Due for Care","🔍 Search Plants","📋 View All Plants","🌱 Track Growth","☀️ Seasonal Care","📷 Plant Photos","📅 Adjust Schedule","🩺 Plant Doctor","💬 Plant Care Assistant"])
if option=="🏠 Dashboard":
    set_background("dashboard.png")
    st.title("🌿 Plant Care Tracker")
    st.write("A simple place to manage your plants and keep track of their care.")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        total_plants=len(plants_df)
    else:
        total_plants=0
    if os.path.exists("care_history.csv"):
        care_df=pd.read_csv("care_history.csv")
        total_activities=len(care_df)
    else:
        total_activities=0
    if os.path.exists("growth_history.csv"):
        growth_df=pd.read_csv("growth_history.csv")
        total_growth=len(growth_df)
    else:
        total_growth=0
    col1,col2,col3=st.columns(3)
    col1.metric("🌱 Total Plants",total_plants)
    col2.metric("💧 Care Activities",total_activities)
    col3.metric("📏 Growth Records",total_growth)
    st.subheader("My Plants")
    if total_plants>0:
        st.dataframe(plants_df,use_container_width=True)
    else:
        st.info("No plants have been added yet.")
elif option=="➕ Add New Plant":
    set_background("add_plant.png")
    add_new_plant()
elif option=="💧 Record Care":
    set_background("record_care.png")
    record_plant_care()
elif option=="⏰ Due for Care":
    set_background("due_care.png")
    view_plants_due_for_care()
elif option=="🔍 Search Plants":
    set_background("search.png")
    search_plants()
elif option=="📋 View All Plants":
    set_background("all_plants.png")
    view_all_plants()
elif option=="🌱 Track Growth":
    set_background("growth.png")
    track_growth()
elif option=="☀️ Seasonal Care":
    set_background("seasonal.png")
    seasonal_care_reminders()
elif option=="📷 Plant Photos":
    set_background("photos.png")
    add_plant_photo()
elif option=="📅 Adjust Schedule":
    set_background("schedule.png")
    adjust_seasonal_schedule()
elif option=="🩺 Plant Doctor":
    set_background("doctor.png")
    diagnose_plant()
elif option=="💬 Plant Care Assistant":
    set_background("assistant.png")
    plant_care_chat()