import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt


st.title('Cardio data')

data=pd.read_csv('Cardio.csv')
df=pd.DataFrame(data)
gender=st.selectbox('Gender',options=list(df.Gender.unique()))
marital=st.selectbox('Marital Status',options=list(df.MaritalStatus.unique()))
plot=sns.barplot(x=df[(df['Gender']==gender) &( df['MaritalStatus']==marital)].Education,y=df[(df['Gender']==gender) &( df['MaritalStatus']==marital)].Miles)

if st.button('click me'):
    st.write(df)
    st.pyplot(plot.get_figure())
    st.write(marital)
import seaborn as sns


