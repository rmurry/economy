import streamlit as st
from streamlit_date_picker import date_range_picker
from datetime import date
from datetime import timedelta
import yfinance as yf
import easychart
import pandas as pd
import altair as alt

st.set_page_config(page_title="Stonks")


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

#dat = get_data("AAPL","2024-01-01","2024-05-01")
#dat.head()

trend = alt.Chart(dat).mark_line().encode(
    x = 'Date',
    y = 'Close'
)
st.altair_chart(trend,use_container_width=True)



