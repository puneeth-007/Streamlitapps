
import pandas as pd
import numpy as np
import streamlit as st

def dffun(response):
	df=pd.json_normalize(response.json(),record_path=['data'])
	return df[['name','full_address']]

st.title('Maps data with address')
place=st.text_input('Please enter the place you want to search')
if st.button('search'):
	import requests
	url = "https://maps-data.p.rapidapi.com/nearby.php"
	querystring = {"query":place,"lat":"17.40","lng":"78.47","limit":"100","country":"ind","lang":"en","offset":"0","zoom":"12"}
	headers = {
		"x-rapidapi-key": "603806efdcmsh7077e2d3ea167a7p1e2264jsnc4ff6dcdf758",
		"x-rapidapi-host": "maps-data.p.rapidapi.com"
		}
	response = requests.get(url, headers=headers, params=querystring)

	#print(response.json())
	df=pd.json_normalize(response.json(),record_path=['data'])
	st.write(df[['name','full_address']])