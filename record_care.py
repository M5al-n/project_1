import streamlit as st
import pandas as pd
import os
def record_plant_care():
    st.header("Record a Plant Care Activity")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Which plant?",plants_df["plant_name"].tolist())#PY LIN
            activity=st.selectbox("Activity",["Watering","Fertilizing","Repotting","Pruning"])
            activity_date=st.date_input("Date")
            if st.button("Record Activity"):
                new_activity={"plant_name":plant_name,"activity":activity,"date":activity_date}
                file_name="care_history.csv"
                if os.path.exists(file_name):
                    care_df=pd.read_csv(file_name)
                    new_activity_df=pd.DataFrame([new_activity])
                    care_df=pd.concat([care_df,new_activity_df],ignore_index=True) #SAVE 0123
                else:
                    care_df=pd.DataFrame([new_activity])
                care_df.to_csv(file_name,index=False)
                st.success("Care activity recorded successfully!")
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")