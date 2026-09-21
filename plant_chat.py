import streamlit as st
def plant_care_chat():
    st.title("Plant Care Assistant")
    st.write("Ask me about watering, sunlight, leaves, roots, fertilizer, or other plant problems.")
    if "messages" not in st.session_state:
        st.session_state.messages=[{"role":"assistant","content":"Hello! How can I help you with your plant?"}]
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])
    prompt=st.chat_input("Ask about your plant...")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        st.chat_message("user").write(prompt)
        question=prompt.lower()
        if "yellow" in question:
            response="Yellow leaves may be caused by overwatering, poor drainage, or insufficient light."
        elif "brown" in question:
            response="Brown leaves may be caused by underwatering, dry air, or too much direct sunlight."
        elif "water" in question:
            response="Check the soil before watering. Water the plant when the soil is becoming dry."
        elif "sunlight" in question or "light" in question:
            response="Make sure the plant receives the correct amount of light for its type."
        elif "wilting" in question or "wilt" in question:
            response="Wilting may be caused by underwatering, overwatering, heat, or root problems."
        elif "fertilizer" in question or "fertilizing" in question:
            response="Use fertilizer according to the plant type and avoid using too much."
        elif "root" in question:
            response="Check the roots for dark, soft, or damaged areas and make sure the pot has good drainage."
        else:
            response="Please tell me the plant name and describe the problem or symptoms."
        st.chat_message("assistant").write(response)
        st.session_state.messages.append({"role":"assistant","content":response})