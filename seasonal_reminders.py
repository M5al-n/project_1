import streamlit as st
import pandas as pd
import os
def seasonal_care_reminders():
    st.header("Seasonal Care Reminders")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Select plant",plants_df["plant_name"].tolist())
            season=st.selectbox("Current season",["Spring","Summer","Autumn","Winter"])
            if st.button("Generate Reminder"):
                if season=="Summer":
                    reminder=f"Check {plant_name}'s soil more often because plants may dry faster during summer."
                elif season=="Winter":
                    reminder=f"Check {plant_name} before watering because plants may need less water during winter."
                elif season=="Spring":
                    reminder=f"Check {plant_name}'s growth and consider fertilizing during the growing season."
                else:
                    reminder=f"Monitor {plant_name}'s watering and light as the weather becomes cooler."
                st.success("Care Reminder")
                st.write(reminder)
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")