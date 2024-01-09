import streamlit as st
import yfinance as finance


def get_ticker(name):
	company = finance.Ticker(name) # google
	return company


# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")
st.sidebar.header("Financial Proyect ")

company1 = get_ticker('GOOG')
company2 = get_ticker('MSFT')

# fetches the data: Open, Close, High, Low and Volume
google = finance.download('GOOG', start="2021-10-01", end="2021-10-01")
microsoft = finance.download('MSFT', start="2021-10-01", end="2021-10-01")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="1mo")
data2 = company2.history(period="1mo")

# markdown syntax
st.write("""
### google
""")

# detailed summary on Google
st.write(company1.info)
st.write(google)

# plots the graph
st.line_chart(data1.values)

st.write("""
### microsoft
""")
st.write(company2.info, "\n", microsoft)
st.line_chart(data2.values)
