import streamlit as st
import pandas as pd
import os
def adjust_seasonal_schedule():
    st.header("Adjust Care Schedule")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Select plant",plants_df["plant_name"].tolist())
            season=st.selectbox("Current season",["Spring","Summer","Autumn","Winter"])
            plant=plants_df[plants_df["plant_name"]==plant_name].iloc[0]# == PLANT NAME خذ أول Row .
            watering_frequency=pd.to_numeric(plant["watering_frequency"],errors="coerce") # NUMB  ERR=NAN
            if pd.isna(watering_frequency):
                st.error("Watering frequency is not available for this plant.")
            else:
                watering_frequency=int(watering_frequency)
                st.write("Watering frequency from API:",watering_frequency,"days")
                if st.button("Adjust Schedule"):
                    if season=="Summer":
                        new_frequency=max(1,watering_frequency-1)#0=1
                    elif season=="Winter":
                        new_frequency=watering_frequency+2
                    else:
                        new_frequency=watering_frequency
                    st.subheader("Adjusted Care Schedule")
                    st.write("Plant:",plant_name)
                    st.write("Original watering frequency:",watering_frequency,"days")
                    st.write("Season:",season)
                    st.write("Adjusted watering frequency:",new_frequency,"days")
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")