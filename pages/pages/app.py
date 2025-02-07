import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('Bike Karido Used bikes data')

# Load the data
f = pd.read_csv(r'pages/secondhandbike.csv', sep='|')
fdf = pd.DataFrame(f)
fdf = fdf.drop(columns='Unnamed: 0')

# Convert columns to numeric
fdf['Price'] = pd.to_numeric(fdf['Price'], errors='coerce')
fdf['Registration_Year'] = pd.to_numeric(fdf['Registration_Year'], errors='coerce')
fdf['KMs_Driven'] = pd.to_numeric(fdf['KMs_Driven'], errors='coerce')

# Default values for price range
default_price = 10000
default_price1 = 1000000

# User inputs
Price_range_lower = st.number_input("Enter the Lower price:", min_value=500, max_value=10000000, key='price_lower', value=default_price)
Price_range_upper = st.number_input("Enter the Upper price:", min_value=500, max_value=10000000, key='price_upper', value=default_price1)
ownership = st.selectbox("Select Ownership", ['All','First', 'Second', 'Third', 'Above'])
company = st.selectbox("Select Company (leave empty to fetch all):", ["All"] + list(fdf['Make'].unique()), key='company')
registration_year = st.selectbox("Enter Year of Registration:", ["All"] + list(map(str, range(2000, 2025))), key='registration_year')

# Fetch data based on user inputs
if st.button("Fetch data"):
    fdf_filtered = fdf[(fdf['Price'] >= Price_range_lower) & (fdf['Price'] <= Price_range_upper)]
    if ownership != 'All':
        fdf_filtered = fdf_filtered[fdf_filtered['Ownership'] == ownership]
    if registration_year != "All":
        fdf_filtered = fdf_filtered[fdf_filtered['Registration_Year'] == int(registration_year)]
    if company != "All":
        fdf_filtered = fdf_filtered[fdf_filtered['Make'] == company]
    
    st.write(fdf_filtered)

    # Create scatter plot
    fig = px.scatter(
        fdf_filtered,
        x="Price",
        y="Registration_Year",
        color="Ownership", 
        size="Price",
        hover_data=["KMs_Driven", "Model", "Make", "url"]
    )
    st.plotly_chart(fig, key="Price")

    # Display URL of selected data point
    if "selectedData" in st.session_state:
        selected_data = st.session_state.selectedData
        if selected_data:
            selected_point = selected_data['points'][0]
            selected_url = selected_point['customdata'][0] # Assuming URL is in the customdata
            if st.button("Open URL for Selected Bike"):
                st.write(f"[Link to Selected Bike]({selected_url})")

# JavaScript to get selected data point
st.markdown("""
<script type="text/javascript">
    var plotly_chart = document.querySelector("[data-testid='stPlotlyChart']");
    plotly_chart.on('plotly_click', function(data){
        var selectedData = {
            points: data.points.map(point => ({
                customdata: point.customdata
            }))
        };
        Streamlit.setComponentValue(selectedData);
    });
</script>
""", unsafe_allow_html=True)
