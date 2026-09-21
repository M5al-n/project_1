import streamlit as st
import pandas as pd
import os
def view_plants_due_for_care():
    st.header("Plants Due for Care")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if os.path.exists("care_history.csv"):
            care_df=pd.read_csv("care_history.csv")
            care_df["date"]=pd.to_datetime(care_df["date"])# TEXT
            watering_df=care_df[care_df["activity"]=="Watering"]# TRUE SAVE
            last_watering=watering_df.groupby("plant_name")["date"].max().reset_index()#MAX DATE
            last_watering=last_watering.rename(columns={"date":"last_watered"})
            due_df=plants_df.merge(last_watering,on="plant_name",how="left") # يدمج 
            today=pd.Timestamp.today().normalize()# TODAY
            due_df["watering_frequency"]=pd.to_numeric(due_df["watering_frequency"],errors="coerce").fillna(7)
            due_df["due_date"]=due_df["last_watered"]+pd.to_timedelta(due_df["watering_frequency"],unit="D")
            due_df["due_date"]=due_df["due_date"].fillna(today) # NO = TODAY
            due_df["days_until_due"]=(due_df["due_date"]-today).dt.days #REMANE DAY
            due_df["status"]="Not due yet"
            due_df.loc[due_df["days_until_due"]<=0,"status"]="Needs watering"
            plants_due=due_df[due_df["days_until_due"]<=0]#-1
            if len(plants_due)>0:
                st.dataframe(plants_due[["plant_name","location","last_watered","watering_frequency","due_date","status"]])
            else:
                st.success("No plants are due for care.")
        else:
            st.write("No care activities have been recorded yet.")
    else:
        st.write("Please add a plant first.")