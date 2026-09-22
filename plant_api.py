import requests
import streamlit as st
API_KEY=st.secrets['API_KeY']
def get_plant_data(plant_name):
    url="https://perenual.com/api/v2/species-list"
    params={"key":API_KEY,"q":plant_name}
    response=requests.get(url,params=params)
    if response.status_code==200:
        data=response.json()
        if len(data.get("data",[]))>0:
            plant_id=data["data"][0]["id"]
            details_url="https://perenual.com/api/v2/species/details/"+str(plant_id)
            details_params={"key":API_KEY}
            details_response=requests.get(details_url,params=details_params)
            if details_response.status_code==200:
                return details_response.json()
    return None
