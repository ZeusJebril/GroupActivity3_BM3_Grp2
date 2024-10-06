import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
# from wordcloud import WordCloud
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
laptopData = pd.read_csv("dataset/laptop_price - dataset.csv")

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


# Graph 3: Price vs. RAM
st.subheader("Graph 3: Price vs. RAM")

def scatterPlot_Price_RAM():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=laptopData['RAM (GB)'], y=laptopData['Price (Euro)'], alpha=0.7)
    plt.title('Price vs. RAM')
    plt.xlabel('RAM (GB)')
    plt.ylabel('Price (Euro)')
    st.pyplot(plt)

scatterPlot_Price_RAM()

st.markdown('`Findings and Observations`')
st.markdown("The box plot shows how laptop prices vary with different RAM capacities. Laptops with higher RAM, like 16 GB and above, generally have higher prices compared to those with lower RAM, such as 4 GB or 8 GB, indicating that RAM significantly impacts the pricing of laptops.")

# Graph 4: Price by TypeName
st.subheader("Graph 4: Price by Laptop Type")

def barChart_Price_Type():
    plt.figure(figsize=(15, 10))
    sns.barplot(x='TypeName', y='Price (Euro)', data=laptopData, palette='Set2')
    plt.title('Average Price by Laptop Type')
    plt.xlabel('Laptop Type')
    plt.ylabel('Average Price (Euro)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

barChart_Price_Type()

st.markdown('`Findings and Observations`')
st.markdown("From the plot, we can see that as the CPU frequency increases, the price of the laptops tends to rise as well. This means that laptops with faster CPUs generally cost more. However, there are some exceptions, with certain brands offering lower prices even when their specifications are high. This indicates that not all expensive laptops are from well-known brands, and some budget-friendly options provide excellent performance.")


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

#Graph 9
st.subheader("Graph 9 Average Price by CPU and GPU company")
pivot_table = laptopData.pivot_table(values='Price (Euro)', index='CPU_Company', columns='GPU_Company', aggfunc=np.mean)

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=.5)

plt.title('Average Price by CPU and GPU Company')
plt.xlabel('GPU Company')
plt.ylabel('CPU Company')

plt.tight_layout()
st.pyplot(plt)

st.markdown('`Findings and Observations`')
st.markdown("The analysis of the bar plot above depicting average prices by memory type reveals significant insights into the factors influencing laptop pricing. The bar plot demonstrates that laptops equipped with Solid State Drives (SSDs) command the highest average prices, reflecting the premium placed on their superior performance and faster data access speeds compared to traditional Hard Disk Drives (HDDs). Conversely, HDD-equipped laptops tend to have moderate pricing, which can be attributed to their larger storage capacity at lower production costs, appealing primarily to budget-conscious consumers. The category labeled Other encompasses less common memory configurations, which correlates with the lowest average prices, suggesting these options are either less popular or targeted at lower-end market segments.")

#Graph 10
st.subheader("Graph 10 Average Price by Memory Type")
def extract_memory_type(memory):
    if 'SSD' in memory:
        return 'SSD'
    elif 'HDD' in memory:
        return 'HDD'
    else:
        return 'Other'

laptopData['Memory_Type'] = laptopData['Memory'].apply(extract_memory_type)

average_price_by_memory = laptopData.groupby('Memory_Type')['Price (Euro)'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Memory_Type', y='Price (Euro)', data=average_price_by_memory, palette='YlGnBu')

plt.title('Average Price by Memory Type')
plt.xlabel('Memory Type')
plt.ylabel('Average Price (Euro)')
plt.grid(True)

plt.tight_layout()
st.pyplot(plt)

st.markdown('`Findings and Observations`')
st.markdown("In conjunction with the visualization above, the heatmap analysis reveals the significant impact of CPU and GPU combinations on pricing strategies within the laptop market. The highest average prices are associated with the pairing of Intel CPUs and Nvidia GPUs, indicative of their prevalence in high-performance laptops tailored for gaming and professional applications. In contrast, configurations utilizing AMD components often result in lower average prices, signifying their focus on the budget and mid-range sectors. This comparative analysis underscores the relationship between hardware components and laptop pricing, elucidating how memory type and processor/gpu combinations affect consumer choices and market segmentation. Collectively, these findings provide valuable insights for consumers aiming to make informed purchasing decisions and for manufacturers seeking to effectively target different market segments.")


st.header("Conclusion")
