import streamlit as st
import pandas as pd
import os
def search_plants():
    st.header("Search Plants")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        search_term=st.text_input("Search by plant name or location")
        if search_term!="":
            name_match=plants_df["plant_name"].str.contains(search_term,case=False,na=False)# R=  r   NA = NUM FALSE
            location_match=plants_df["location"].str.contains(search_term,case=False,na=False)
            search_results=plants_df[name_match|location_match]#OR
            if len(search_results)>0:
                st.dataframe(search_results)
            else:
                st.write("No matching plants found.")
    else:
        st.write("Please add a plant first.")