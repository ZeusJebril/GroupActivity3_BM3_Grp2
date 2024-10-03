import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D

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
