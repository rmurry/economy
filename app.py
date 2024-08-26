import streamlit as st
from datetime import date
from datetime import timedelta
import yfinance as yf
import pandas as pd
import altair as alt

st.set_page_config(page_title="Stonks",layout="wide",initial_sidebar_state="expanded")

with st.sidebar:
    st.title("Stock Puller")

    st.markdown("Enter a Stock Symbol and Date Range to Pull Data For")

    symbol = st.text_input(label = "Stock Symbol",value="AAPL")

    start_date = st.date_input(label = "Starting Date",value = date.today()-timedelta(weeks = 12))
    end_date = st.date_input(label = "Ending Date",value = date.today())

def get_data(symbol,start_date,end_date):
    results = pd.DataFrame(yf.download(symbol,start=start_date,end=end_date)).reset_index()
    return results

dat = get_data(symbol,start_date,end_date)

trend = alt.Chart(dat).mark_line().encode(
    x = 'Date',
    y = 'Close',
    tooltip = ['Date','Close']
).properties(title="Stock Trend").interactive()


### Dashboard Layout
col = st.columns((1,4),gap='medium')

with col[0]:
    st.metric(symbol,"100","4")

with col[1]:
    st.altair_chart(trend,use_container_width=True)



