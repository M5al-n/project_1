import streamlit as st
import pandas as pd
import os
def diagnose_plant():
    st.header("Plant Doctor")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Select plant",plants_df["plant_name"].tolist())
            symptom=st.selectbox("Select the main symptom",["Yellow leaves","Brown leaves","Wilting","Root problems","Slow growth"])
            if st.button("Diagnose Plant"):
                diagnosis=""
                solution=""
                if symptom=="Yellow leaves":
                    diagnosis="Possible overwatering or poor drainage."
                    solution="Check the soil moisture and make sure excess water can drain."
                elif symptom=="Brown leaves":
                    diagnosis="Possible underwatering or low humidity."
                    solution="Check the soil moisture and provide suitable humidity."
                elif symptom=="Wilting":
                    diagnosis="Possible underwatering or root stress."
                    solution="Check the soil and roots and provide appropriate watering."
                elif symptom=="Root problems":
                    diagnosis="Possible root rot or poor drainage."
                    solution="Check the roots and improve soil drainage."
                elif symptom=="Slow growth":
                    diagnosis="Possible insufficient light or nutrients."
                    solution="Check the plant's light conditions and nutrient needs."
                st.subheader("Plant")
                st.write(plant_name)
                st.subheader("Possible Problem")
                st.write(diagnosis)
                st.subheader("Suggested Recovery Steps")
                st.write(solution)
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")