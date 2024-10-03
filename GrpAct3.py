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

st.subheader("Graph 1: Price by Company")
#u can edit the graph name part

def boxChart_Price_Company(laptopData=laptopData, x_col='Company', y_col='Price (Euro)'):
    plt.figure(figsize=(16, 14))
    sns.boxplot(x=laptopData[x_col], y=laptopData[y_col], palette="Set3", hue=None)
    plt.title('Price Distribution of Laptops by Company')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    st.pyplot(plt)  

boxChart_Price_Company()

st.markdown('`Findings and Observations`')
st.markdown("Based on the Box chart, the laptop brand that has the highest price range is Razer while the lowest is Vero. Some companies, like Razer and Microsoft, have a few laptops that fall outside their usual price range, which you can see from the whiskers or lines extending beyond the box. This indicates a wide spread of prices, both higher and lower than the average price of the brand. Companies like HP and Dell have outliers, or small dots, indicating significantly higher prices for certain laptops that are far from their average price range. On the other hand, companies like Mediacom and Fujitsu have small whiskers and no outliers, suggesting a more consistent and budget-friendly price range. The line inside each box represents the median price. Apple’s median line is closer to the bottom, indicating that they offer many budget-friendly options. With a median line in the middle, Huawei seem to have a very balanced average price for their laptops. Given that Samsung's median line is closer to the top, the majority of their laptops are often more expensive.")


st.subheader("Graph 2: Price by Operating System")
#u can edit the graph name part

def barChart_Price_OS():
    plt.figure(figsize=(15, 10))
    os = laptopData['OpSys']
    price = laptopData['Price (Euro)']
    plt.bar(os, price)
    plt.title('Laptop Prices by Operating System')
    plt.ylabel('Price (Euro)')
    plt.xlabel('Operating System')

    plt.xticks(rotation=45)
    st.pyplot(plt) 

barChart_Price_OS()

st.markdown('`Findings and Observations`')
st.markdown("The bar graph shows that laptops with the Windows 10 operating system have the highest average price, followed by those with Windows 7, while laptops with Android have the lowest average price. A surprising discovery is that a laptop with no operating system does not have the lowest price among the laptops with an operating system. The price difference between Windows 10 and Windows 7 laptops is about 1,000 euros, while the gap between Windows 10 and Android laptops is roughly 5,000 euros. This suggests that laptops with any Windows operating system tend to be more expensive than those with Android or no operating system.")


st.subheader("Graph 3")
#u can edit the graph name part

# put the graph here

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 4")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 5")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 6")
#u can edit the graph name part 

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 7")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 8")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 9")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here

st.subheader("Graph 10")
#u can edit the graph name part

st.markdown('`Findings and Observations`')
st.markdown("...")
# put the findings and observations here


st.header("Conclusion")