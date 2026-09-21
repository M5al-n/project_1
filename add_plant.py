import streamlit as st
import pandas as pd
import os
import re# NUM API
from plant_api import get_plant_data
def add_new_plant():
    st.header("Add a New Plant")
    plant_name=st.text_input("Plant name/species")
    plant_type=st.selectbox("Plant type",["Tropical","Succulent","Flowering","Herb","Other"])
    season=st.selectbox("Season",["Spring","Summer","Autumn","Winter"])
    location=st.text_input("Location in home")
    date_acquired=st.date_input("Date acquired")
    if st.button("Get Plant Care Information"):
        if plant_name=="":
            st.error("Please enter the plant name.")
        else:
            plant_data=get_plant_data(plant_name)#API
            if plant_data is not None:
                st.session_state["plant_data"]=plant_data
                st.success("Plant information found!")
            else:
                st.error("Plant not found in the API.")
    if "plant_data" in st.session_state:
        plant_data=st.session_state["plant_data"]
        common_name=plant_data.get("common_name",plant_name) #KeyError
        watering=plant_data.get("watering","Not available")
        sunlight_data=plant_data.get("sunlight",[])
        if isinstance(sunlight_data,list):
            sunlight=", ".join(sunlight_data)
        else:
            sunlight=str(sunlight_data)
        watering_info=plant_data.get("watering_general_benchmark",{})
        watering_frequency=str(watering_info.get("value",""))
        watering_unit=watering_info.get("unit","days")
        numbers=re.findall(r"\d+",watering_frequency)
        watering_days=None
        if len(numbers)==1:
            watering_days=int(numbers[0])
        elif len(numbers)>=2:
            first_day=int(numbers[0])
            second_day=int(numbers[1])
            watering_days=round((first_day+second_day)/2)
        care_tip=f"Watering level: {watering}. Water approximately every {watering_frequency} {watering_unit}. Recommended sunlight: {sunlight}."
        st.subheader("Plant Care Information")
        st.write("Plant:",common_name)
        st.write("Watering:",watering)
        st.write("Watering interval from API:",watering_frequency,watering_unit)
        st.write("Sunlight:",sunlight)
        st.write("Care Tip:",care_tip)
        if watering_days is not None:
            st.write("Watering days used for schedule:",watering_days,"days")
        if st.button("Add Plant"):
            if watering_days is None:
                st.error("The API did not provide a watering interval for this plant.")
            else:
                new_plant={"plant_name":common_name,"plant_type":plant_type,"season":season,"location":location,"date_acquired":date_acquired,"watering_frequency":watering_days,"watering_interval":watering_frequency+" "+watering_unit,"sunlight_needs":sunlight,"care_tip":care_tip}
                file_name="plants.csv"
                if os.path.exists(file_name):
                    plants_df=pd.read_csv(file_name)
                    new_plant_df=pd.DataFrame([new_plant])
                    plants_df=pd.concat([plants_df,new_plant_df],ignore_index=True)
                else:
                    plants_df=pd.DataFrame([new_plant])
                plants_df.to_csv(file_name,index=False)
                st.success("Plant added successfully!")
                del st.session_state["plant_data"]