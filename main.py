
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
import streamlit as st

st.title('Maps data with address')
import requests
url = "https://maps-data.p.rapidapi.com/nearby.php"

querystring = {"query":"bike repair shop","lat":"17.40","lng":"78.47","limit":"100","country":"ind","lang":"en","offset":"0","zoom":"12"}

headers = {
	"x-rapidapi-key": "603806efdcmsh7077e2d3ea167a7p1e2264jsnc4ff6dcdf758",
	"x-rapidapi-host": "maps-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

df=pd.json_normalize(response.json(),record_path=['data'])
df[['name','full_address']].head