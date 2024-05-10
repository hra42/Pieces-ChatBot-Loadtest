import streamlit as st
from internal.intro import get_intro
from internal.setup_pieces_connection.setup import check_setup
from internal.chatbot.chat import chat
from internal.environment.read_env import read_env_file

# MARK: - Page Config
st.set_page_config(page_title="Pieces ChatBot Load Test", page_icon="", layout="wide")

#MARK: - Pages List
page_names_to_funcs = {
    "-": get_intro,
    "Check Pieces Connection": check_setup,
    "Chatbot": chat,
}

app = st.sidebar.selectbox("Choose a function", list(page_names_to_funcs.keys()))
page_names_to_funcs[app]()