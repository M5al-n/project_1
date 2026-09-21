import streamlit as st
import pandas as pd
import os
def view_all_plants():
    st.header("All Plants")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            st.dataframe(plants_df)
        else:
            st.write("No plants have been added yet.")
    else:
        st.write("No plants have been added yet.")