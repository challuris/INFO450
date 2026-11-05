import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv("Advertising_F.csv")

st.title("Advertising Dashboard - Sri")

st.sidebar.header("Filters")
x_var = st.selectbox("X axis", ['TV','radio',"newspaper"])

#show scatterplot
fig = px.scatter(df, x=x_var, y='sales',
           labels={'TV': 'TV ad spend', 'radio': 'Radio ad spend'})
st.plotly_chart(fig)

#show bar plot
sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig = px.bar(sales_per_city, x='City', y='sales', title='sales per city')
st.plotly_chart(fig)

#Show the dataframe
st.dataframe(df)
