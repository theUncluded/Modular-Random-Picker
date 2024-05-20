from functions import *
import streamlit as st
#Modular Rand Picker
"""
Allow users to set params for random picking from a list. List must be txt file attached to mrp's list folder. 
"""
st.title("Random Item Picker")
options = st.selectbox(
    "Select A Method to Choose At Random!",
    ("CSV", "TXT", "Input Manually")
)

if options == "CSV":
    u_file = st.file_uploader("Upload CSV Here!",'csv')
    if u_file is not None:
        pick = csv_op(u_file)
        st.write(pick)
elif options == "TXT":
    u_file = st.file_uploader("Upload TXT Here!",'txt')
    if u_file is not None:
        text_path(u_file)
        pick = txt_op(u_file)
        st.write(pick)
else:
    input_op()