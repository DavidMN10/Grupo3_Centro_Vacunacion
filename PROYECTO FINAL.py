# -*- coding: utf-8 -*-
"""
IA PUCP - Diplomatura de Desarrollo de Aplicaciones de Inteligencia Artificial
Python para Ciencia de Datos

TRABAJO DE FIN DE CURSO PYTHON PARA CIENCIA DE DATOS

PROFESOR: Pablo Fonseca

Created on Mon Dec 19 09:58:20 2022

@auth: 
David Arroyo Leon

Vidal Cupe Quispe

Julio Díaz Villanueva

David Milla Noa

Erika Tello Rivera

"""
import streamlit as st
from streamlit_folium import folium_static
import geopandas as gpd
import pandas as pd
import numpy as np
import folium
from folium.features import GeoJsonTooltip
import altair as alt

st.set_page_config(layout ="wide")
st.title("Vacunatorios COVID en el Perú")
json1 = f"peru_departamental_simple.geojson"


m = folium.Map(location=[-12.029789, -77.129030], tiles='CartoDB positron', name="Light Map",
               zoom_start=5, attr="My Data attribution")


df=pd.read_csv('BASE_DATOS.csv')
df=df.drop('Unnamed: 0',axis=1)

geojson=gpd.read_file("peru_departamental_simple.geojson")
geojson=geojson[['NOMBDEP','geometry']]

df=geojson.merge(df, left_on="NOMBDEP", right_on="nombdep", how="outer")

choice = [ 'CANTIDAD TOTAL DE CENTROS', 'MINSA', 'DIRESA', 'ESSALUD',
 'LABORATORIOS', 'CENTRO DE SALUD', 'POSTA DE SALUD',
 'INSTITUCIONES EDUCATIVAS', 'INSTITUCIONES PRIVADAS.']
choice_selected = st.selectbox("Select choice", choice)

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=df,
    columns=['nombdep',choice_selected],
    key_on="feature.properties.NOMBDEP",
    fill_color="YlOrRd",
    nan_fill_color="White",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name=choice_selected
).add_to(m)

folium.features.GeoJson(
                    data=df,
                    name='VACUNATORIOS COVID',
                    smooth_factor=2,
                    style_function=lambda x: {'color':'black','fillColor':'transparent','weight':0.5},
                    tooltip=folium.features.GeoJsonTooltip(
                        fields=[ 'CANTIDAD TOTAL DE CENTROS', 'MINSA', 'DIRESA', 'ESSALUD',
                         'LABORATORIOS', 'CENTRO DE SALUD', 'POSTA DE SALUD',
                         'INSTITUCIONES EDUCATIVAS', 'INSTITUCIONES PRIVADAS.'],
                        aliases=["Cantidad de Vacunatorios Totales:",
                                 'Vacunados por :MINSA', 
                                 'Vacunados por :DIRESA',
                                 'Vacunados por :ESSALUD',
                                 'Vacunados por :LABORATORIOS',
                                 'Vacunados por :CENTROS DE SALUD',
                                 'Vacunados por :POSTA MÉDICA',
                                 'Vacunados por :INSTITUCIÓN EDUCATIVA',
                                 'Vacunados por :INSTITUCIÓN PRIVADA'
                                ], 
                        localize=True,
                        sticky=False,
                        labels=True,
                        style="""
                            background-color: #F0EFEF;
                            border: 2px solid black;
                            border-radius: 3px;
                            box-shadow: 3px;
                        """,
                        max_width=800,),
                            highlight_function=lambda x: {'weight':3,'fillColor':'grey'},
                        ).add_to(m) 

folium_static(m, width=1600, height=950)

st.title("Exploración de Vacunatorios COVID en el Perú con Gráficos de Barras")
data = df
column = st.selectbox('Select column',['MINSA', 'DIRESA', 'ESSALUD',
 'LABORATORIOS', 'CENTRO DE SALUD', 'POSTA DE SALUD',
 'INSTITUCIONES EDUCATIVAS', 'INSTITUCIONES PRIVADAS.'])
countries = st.multiselect('Select countries',list(data["NOMBDEP"].unique()))

if countries:
    country_max_cases = []
    country_cases = pd.DataFrame()
    for country in countries:
        country_cases = country_cases.append(data[data["NOMBDEP"] == country],ignore_index=True)
        country_max_cases.append(np.max(data[data["NOMBDEP"] == country][column]))

    df_max = pd.DataFrame({
    'DEPARTAMENTO': countries,
    column: country_max_cases
    })

    df_max = df_max.set_index('DEPARTAMENTO',drop=True)

    col1, col2 =  st.columns(2)

    with col1:
        st.bar_chart(df_max)

    chart = alt.Chart(country_cases).mark_line().encode(
        x=alt.X('date:T', axis=alt.Axis(tickCount=10, grid=False)),
        y=alt.Y(f'{column}:Q'),
        color='location:N',
        #strokeDash='location',
    )






