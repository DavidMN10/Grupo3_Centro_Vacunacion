
IA PUCP - Diplomatura de Desarrollo de Aplicaciones de Inteligencia Artificial
Python para Ciencia de Datos
============
TRABAJO DE FIN DE CURSO PYTHON PARA CIENCIA DE DATOS

PROFESOR: Pablo Fonseca


----------------------------------
Integrantes:
David Arroyo Leon

Vidal Cupe Quispe

Julio Díaz Villanueva

David Milla Noa

Erika Tello Rivera

----------------------------------
Se preparo un dataset a partir de la información de los centros de vacunacion de Covid 19 en Peru de la web de datos abiertos ( https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion) y el dataset con los datos geográficos de los departamentos del peru
Este nuevo dataset contiene nombre del departamento , latitud, longitud, cantidad de centro de vacunacion por departamento y volumen de diferentes tipos de centros de vacunación. 

El procesamiento de los datos lo podemos encontrar en el archivo nombrado "Trabajo_Final_Streamlit.ipynb" en el cual se encuentra en notebook desarrollado.

En el archivo "PROYECTOFINAL.py" se encuentra la app la cual tiene el siguiente link de deploy:

----------------------------------

La app muestra un mapa interactivo del Perú dividido en departamentos en los cuales podemos visualizar en forma de heatmap las cantidades de centros de vacunación por entidades las cuales fueron extraidas del scraping de datos de la base de datos original. 

En la parte inferior podemos hacer comparaciones de barras de los diferentes tipos de centros de vacunación y hacer la comparación por departamento.


----------------------------------
Referencias:
1) https://discuss.streamlit.io/t/creating-points-and-heatmap-from-csv/20047
2) https://github.com/juaneladio/peru-geojson/blob/master/peru_departamental_simple.geojson
3) https://sakizo-blog.com/en/607/
4) https://medium.datadriveninvestor.com/recreating-my-project-using-folium-and-streamlit-part-2-8e7668e8924d
