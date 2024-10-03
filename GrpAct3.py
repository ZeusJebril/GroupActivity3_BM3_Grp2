import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
from io import StringIO

st.title('Group Activity 2')

st.markdown("""    
Section: BM3
Group Number: 2
Group Members:
1. Boado, Julianna
2. Caluag, John
3. Kubaron, Zeus
4. Lajom, Joaquin
5. Lituanas, Kobe

Data Used: Laptop Price Dataset [(https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset/data)](https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset/data)
""")

st.header("Importing Libiries")
st.markdown("""    
1. Matplotlib [(https://matplotlib.org/)](https://matplotlib.org/)
2. Numpy [(https://numpy.org/)](https://numpy.org/)
3. Pandas [(https://pandas.pydata.org/docs/user_guide/index.html)](https://pandas.pydata.org/docs/user_guide/index.html)
4. Seaborn [(https://seaborn.pydata.org/)](https://seaborn.pydata.org/)
5. Altair [(https://altair-viz.github.io/)](https://altair-viz.github.io/)
6. Wordcloud [(https://pypi.org/project/wordcloud/)](https://pypi.org/project/wordcloud/)
7. mpl_toolkits [(https://matplotlib.org/stable/api/toolkits/mplot3d.html)](https://matplotlib.org/stable/api/toolkits/mplot3d.html)

""") 

st.header("Describing the Dataset")

st.write("Read our CSV dataset.")
laptopData = pd.read_csv("C:\\Users\\Julianna Boado\\Desktop\\GroupActivity3\\dataset\\laptop_price - dataset.csv")

laptopData

buffer = StringIO()
laptopData.info(buf=buffer)
laptopData_info_as_string = buffer.getvalue()

st.text(laptopData_info_as_string)

st.write(laptopData.isna().sum())

st.write(laptopData.describe())

st.write(laptopData['Inches'].value_counts())

st.write(laptopData['CPU_Frequency (GHz)'].value_counts())

st.write(laptopData['RAM (GB)'].value_counts())

st.write(laptopData['Weight (kg)'].value_counts())

st.write(laptopData['Price (Euro)'].value_counts())

st.write(laptopData['Company'].value_counts())

st.write(laptopData['Product'].value_counts())

st.write(laptopData['TypeName'].value_counts())

st.write(laptopData['ScreenResolution'].value_counts())

st.write(laptopData['CPU_Company'].value_counts())

st.write(laptopData['CPU_Type'].value_counts())

st.write(laptopData['Memory'].value_counts())

st.write(laptopData['GPU_Company'].value_counts())

st.write(laptopData['GPU_Type'].value_counts())

st.write(laptopData['OpSys'].value_counts())

st.header("Graphs")