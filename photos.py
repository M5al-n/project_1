import streamlit as st
import pandas as pd
import os
def add_plant_photo():
    st.header("Plant Photos")
    if os.path.exists("plants.csv"):
        plants_df=pd.read_csv("plants.csv")
        if len(plants_df)>0:
            plant_name=st.selectbox("Select plant",plants_df["plant_name"].tolist())
            uploaded_file=st.file_uploader("Upload plant image",type=["jpg","jpeg","png"])
            if uploaded_file is not None:
                st.image(uploaded_file)
                if st.button("Save Photo"):
                    if not os.path.exists("plant_photos"):
                        os.mkdir("plant_photos")
                    file_type=uploaded_file.name.split(".")[-1]
                    file_name="plant_photos/"+plant_name+"."+file_type
                    file=open(file_name,"wb")
                    file.write(uploaded_file.getvalue())
                    file.close()
                    st.success(f"{plant_name}'s photo saved successfully!")
        else:
            st.write("Please add a plant first.")
    else:
        st.write("Please add a plant first.")