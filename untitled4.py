# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:58:20 2022

@author: Hubble
"""
import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
st.set_page_config(layout ="wide")

json1 = f"peru_departamental_simple.geojson"


m = folium.Map(location=[-12.029789, -77.129030], tiles='CartoDB positron', name="Light Map",
               zoom_start=5, attr="My Data attribution")


df=pd.read_csv('BASE_DATOS.csv')
df=df.drop('Unnamed: 0',axis=1)

choice = ['MINSA', 'DIRESA','ESSALUD', 'LAB', 'CS', 'PS', 'IE', 'PRIV','CANT']
choice_selected = st.selectbox("Select choice", choice)

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=df,
    columns=['nombdep',choice_selected],
    key_on="feature.properties.NOMBDEP",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name=choice_selected
).add_to(m)
folium.features.GeoJson('peru_departamental_simple.geojson',
                        name="States", popup=folium.features.GeoJsonPopup(fields=["NOMBDEP"])).add_to(m)

folium_static(m, width=1600, height=950)