import pandas as pd
import numpy as np
import streamlit as st
import random
import re
import os
from pathlib import Path

#operations to conduct if file is of csv type
def csv_op(file):
        df = pd.read_csv(file)
        rand_from_csv_pick = df.at(random.randint(0, len(df)))
        df = df.pop(rand_from_csv_pick)
        return rand_from_csv_pick
    
def text_path(file):
    save_folder = "Upload"
    save_path = Path(save_folder , file)
    with open(save_path,mode="wb") as w:
        w.write(file.getvalue())
        
        if save_path.exists():
            st.success(f'File {file} was successfully uploaded!')
    return save_path
#operations to conduct if file is of txt type , file_path passed for i/o , specific iteration: through new line/lines split at new line
def txt_op(file_path):
        f = open(file_path , "r")
        txt_f = f.read()
        f.close()
        txt_f.splitlines()
        length = txt_f.count("\n")
        r = random.randint(0, length)
        choice = txt_f[r]
        txt_f[r].pop()
        return choice
#User input of data to be random picked
def input_op():
        i=0
        st.write('Enter Values Below: (seperate values by space or comma)')
        u_input = st.text_input("Value: ", "dogs , cats , reptiles , rodents , goats")
        u_input = re.split('\s|,', u_input)#regex split of comma and space
        
        if st.button("Random Pick!", key=3):
                st.write(u_input[random.randint(0, len(u_input))]) 
