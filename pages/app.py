import pandas as pd
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px

st.title('Bike Karido Used bikes data')

f = pd.read_csv(r'pages/secondhandbike.csv', sep='|')
fdf = pd.DataFrame(f)
fdf = fdf.drop(columns='Unnamed: 0')

fdf['Price'] = pd.to_numeric(fdf['Price'], errors='coerce')
fdf['Registration_Year'] = pd.to_numeric(fdf['Registration_Year'], errors='coerce')
fdf['KMs_Driven'] = pd.to_numeric(fdf['KMs_Driven'], errors='coerce')

default_price = 10000
default_price1 = 1000000

Price_range_lower = st.number_input("Enter the Lower price:", min_value=500, max_value=10000000, key='price_lower', value=default_price)
Price_range_upper = st.number_input("Enter the Upper price:", min_value=500, max_value=10000000, key='price_upper', value=default_price1)
ownership = st.selectbox("Select Ownership", ['All','First', 'Second', 'Third', 'Above'])
company = st.selectbox("Select Company (leave empty to fetch all):", ["All"] + list(fdf['Make'].unique()), key='company')
registration_year = st.selectbox("Enter Year of Registration:", ["All"] + list(map(str, range(2000, 2025))), key='registration_year')

if st.button("Fetch data"):
    if Price_range_lower:
        if Price_range_upper:
            fdf1 = fdf[(fdf['Price'] >= Price_range_lower) & (fdf['Price'] <= Price_range_upper)]
        else:
            fdf1 = fdf[fdf['Price'] >= Price_range_lower]
    else:
        if Price_range_upper:
            fdf1 = fdf[fdf['Price'] <= Price_range_upper]
        else:
            fdf1 = fdf
    if ownership != 'All':
        if ownership:
            fdf2 = fdf1[fdf1['Ownership'] == ownership]
        else:
            fdf2 = fdf1
    else:
        fdf2 = fdf1

    if registration_year != "All":
        if registration_year:
            fdf3 = fdf2[fdf2['Registration_Year'] == int(registration_year)]
        else:
            fdf3 = fdf2
    else:
        fdf3 = fdf2

    if company != "All":
        fdf4 = fdf3[fdf3['Make'] == company]
    else:
        fdf4 = fdf3
    st.write(fdf4)
   
    data = {'Price': [100, 200, 150, 300, 250], 'Make': ['A', 'B', 'A', 'B', 'A']}

  
    fig = px.histogram(fdf, x='Price', title='Histogram of Price')
    fig.show()
    plotly_chart(fig)
    '''st.write(fdf4)
    fig = ff.create_distplot( fdf4['Price'])
    st.plotly_chart(fig)'''
