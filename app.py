import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
Dataframe = pd.read_csv("supermarket.csv")


st.title(':red[Unit 5 Dashboard]')






st.metric(label="Average Daily Customer", value='984')
st.subheader('Daily Customer Count in top 100 stores')
st.line_chart(Dataframe["daily_customer_count"].nlargest(n=100))


st.subheader('_Stores Sales_')
chart_data = pd.DataFrame(
    
    columns=['store_id', 'store_sales'])

st.bar_chart(data=Dataframe,  x='store_id', y='store_sales', width=0, height=0, use_container_width=True)





st.subheader(':blue[Bottom 10 stores in sales]')
st.table(Dataframe["store_sales"].nsmallest(n=10))