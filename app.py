import streamlit as st
from streamlit_date_picker import date_range_picker
from datetime import date
from datetime import timedelta
import yfinance as yf
import easychart
import pandas as pd

easychart.config.rendering.responsive = True
st.title("Stock Puller")

st.sidebar.markdown("Enter a Stock Symbol and Date Range to Pull Data For")

symbol = st.sidebar.text_input(label = "Stock Symbol",value="AAPL")

start_date = st.sidebar.date_input(label = "Starting Date",value = date.today()-timedelta(weeks = 12))
end_date = st.sidebar.date_input(label = "Ending Date")

dat = yf.download(symbol,start=start_date,end=end_date)
#dat = yf.download("AAPL",start="2024-01-01",end="2024-03-01")
#dat.head()

trend = easychart.new("line")
trend.plot(dat)

st.components.v1.html(easychart.rendering.render(trend), height=400)

