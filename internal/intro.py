import streamlit as st

def get_intro():
    st.title("Pieces ChatBot Load Test")
    st.markdown(
    """
    This is a chatbot designed to use an instance of PiecesOS as a backend for LLM queries.
    It will be used to test how many concurrent users can be supported by the backend.
    
    Setup Pieces Connection:
    - Define the IP and port of the Pieces OS you want to use
    - It allows you to check if Pieces OS is running and accessible
    """)