import streamlit as st
import pandas as pd
import os
def track_growth():
    st.header("Track Plant Growth")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Which plant?",plants_df["plant_name"].tolist())# -----
            height=st.number_input("Plant height (cm)",min_value=0.0,step=0.1)
            measurement_date=st.date_input("Measurement date")
            if st.button("Save Growth Measurement"):
                new_measurement={"plant_name":plant_name,"height_cm":height,"date":measurement_date}
                file_name="growth_history.csv"
                if os.path.exists(file_name):
                    growth_df=pd.read_csv(file_name)
                    new_measurement_df=pd.DataFrame([new_measurement])
                    growth_df=pd.concat([growth_df,new_measurement_df],ignore_index=True)
                else:
                    growth_df=pd.DataFrame([new_measurement])
                growth_df.to_csv(file_name,index=False)
                st.success("Growth measurement saved successfully!")
                st.dataframe(growth_df)
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")