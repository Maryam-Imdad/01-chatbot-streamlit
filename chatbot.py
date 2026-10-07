# Student: Maryam
# Project: AI-ML Chatbot - 3 Months Course Assignment
import streamlit as st

# Page setting
st.set_page_config(page_title="Student Assistant")

# Title - yehi change ho gaya hai
st.title("🎓 Student Assistant Chatbot")
st.write("Name: Maryam | Course: AI-ML Chatbot Project")

# Chat history save karne ke liye
if "chat" not in st.session_state:
    st.session_state.chat = []

# Purane messages dikhana
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# Neeche wala input box
user_input = st.chat_input("Apna sawal likhain...")

if user_input:
    # User ka message
    st.session_state.chat.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Bot ka jawab - simple logic jo teacher ko samajh aaye
    if "salam" in user_input.lower():
        ans = "Walaikum Salam! Bataiye main apki kya madad kar sakti hun?"
    elif "name" in user_input.lower():
        ans = "Mera naam Student Assistant hai, maine Python aur Streamlit se banaya hai."
    elif "course" in user_input.lower():
        ans = "Ye mera 3 months AI-ML course ka pehla project hai."
    else:
        ans = f"Aap ne kaha: '{user_input}'. Ye acha sawal hai, main is par kaam kar rahi hun."

    # Bot ka reply
    with st.chat_message("assistant"):
        st.write(ans)
    st.session_state.chat.append({"role": "assistant", "text": ans})