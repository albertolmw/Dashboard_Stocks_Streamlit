import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

today = date.today()

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#SIDEBAR
st.sidebar.header("Dashboard Portfolio 📈")
st.sidebar.markdown('''
---
Created by albertolmw.
''')
# Select your stocks
STOCKS=st.sidebar.multiselect("Select your stocks", options=["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA", "META", "NVDA", "PYPL", "NFLX", "INTC"])
#Select the start date
start_date = st.sidebar.date_input("Start date",value="2025-01-01" ,max_value=today)

#Download the data
PORT=pd.DataFrame()
for stock in STOCKS:
    PORT[stock]=yf.Ticker(stock).history(start=start_date, end=today).Close

#Number of days
days = (today - start_date).days
#Calculate the returns
RET = pd.DataFrame()
for stock in STOCKS:
    RET[stock] = PORT[stock].pct_change()
returns = {}
for stock in STOCKS:
    returns[stock] =RET[stock].sum()
#Calculate the risk
risk = {}
for stock in STOCKS:
    risk[stock] =RET[stock].std()
#Calculate the return per risk
return_risk = {}
for stock in STOCKS:
    return_risk[stock] = returns[stock]/risk[stock]
#Calculate correlation
corr_return = RET.corr()

#Create the dashboard
col = st.columns((.15, .45, .4), gap='medium',border=True)

with col[0]:
    st.metric("Days elapsed:", days)
    
    ## Returns
    st.write("## Returns")
    returns = pd.DataFrame(returns, index=["Returns"]).T
    # Title of stocks
    returns.index.name = "Stocks"
    # Sort returns
    returns = returns.sort_values(by="Returns", ascending=False)
    returns = returns.style.format("{:.2%}")
    st.dataframe(returns, column_order=["Returns"])
    
    ## Risks
    st.write("## Risk")
    risk = pd.DataFrame(risk, index=["Risk"]).T
    # Title of stocks
    risk.index.name = "Stocks"
    # Sort risk
    risk = risk.sort_values(by="Risk", ascending=False)
    risk = risk.style.format("{:.2%}")
    st.dataframe(risk, column_order=["Risk"])

with col[1]:
    st.write("## STOCKS")
    st.line_chart(PORT[STOCKS])

    #Correlation heatmap
    st.write("## Correlation")
    fig, ax=plt.subplots()
    fig.patch.set_facecolor((0,0,0,0))
    sns.heatmap(corr_return, annot=True, cmap='coolwarm',center=0)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.write(fig)
    
with col[2]:
    #Return per risk bar plot
    st.write("## Return per unit of Risk")
    return_risk = pd.DataFrame(return_risk, index=["Return by Risk"]).T
    st.bar_chart(return_risk, y_label="% / σ")

    #Boxplot
    st.write("## Boxplot")
    fig, ax = plt.subplots()
    fig.patch.set_facecolor((0,0,0,0))
    sns.boxplot(data=RET)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.write(fig)


    
