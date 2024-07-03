import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('candidates_with_phase.csv')

st.title("2024 Loksabha Elections")

nav = st.sidebar.radio("Navigation",['Male Female Participation','Age Wise Representation','Result','Maharashtra'])

if nav == "Male Female Participation" :
    gender = ['male', 'female', 'third' ]
    candidates = [7634,801,6]

    fig, ax = plt.subplots()
    ax.pie(candidates, labels = gender, autopct = '%1.1f%%')
    ax.set_title('Total Candidates')
    st.pyplot(fig)
