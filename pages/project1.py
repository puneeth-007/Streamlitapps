import streamlit as st
import pandas as pd


st.title('Welcome to streamlit page')

data=pd.read_csv('Cardio.csv')
df=pd.DataFrame(data)
if st.button('click me'):
    st.write(df)

