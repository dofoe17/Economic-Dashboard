import streamlit as st
import yfinance as yf 
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from fredapi import Fred

st.set_page_config(page_title='My Economic Dashboard', page_icon='💹', layout='wide')

st.title('Economic Indicators Dashboard')


#Date range 
end_date = pd.to_datetime('today')#.strftime('%Y-%m-%d')
start_date = end_date - pd.DateOffset(years=1) #1 year ago

sp_col, ftse_col, nasdaq_col, cable_col, btc_col = st.columns([1, 1, 1, 1, 1])

#Set the headliners for indices on dashboard
with sp_col: 
    with st.container(border=True): 
        sp_data = yf.download(tickers='^GSPC', start=start_date, end=end_date)['Close']
        dod_sp = sp_data.tail(2).pct_change() 
        sp_latest_price = sp_data.tail(1)     

        sp_latest_price_val = sp_latest_price.iloc[0]['^GSPC']
        dod_sp_val = dod_sp.iloc[1]['^GSPC']
        st.subheader('S&P 500', divider='gray')
        st.markdown(f'**{sp_latest_price_val:,.2f}**') 
        if dod_sp_val > 0:
            st.markdown(f'+{dod_sp_val:.2%}')
        else: 
            st.markdown(f'{dod_sp_val:.2%}')


with ftse_col: 
    with st.container(border=True): 
        ftse_data = yf.download(tickers='^FTSE', start=start_date, end=end_date)['Close']
        dod_ftse = ftse_data.tail(2).pct_change() 
        ftse_latest_price = ftse_data.tail(1)     

        ftse_latest_price_val = ftse_latest_price.iloc[0]['^FTSE']
        dod_ftse_val = dod_ftse.iloc[1]['^FTSE']
        st.subheader('FTSE 100', divider='gray')
        st.markdown(f'**{ftse_latest_price_val:,.2f}**') 
        if dod_ftse_val > 0:
            st.markdown(f'+{dod_ftse_val:.2%}')
        else: 
            st.markdown(f'{dod_ftse_val:.2%}')


with nasdaq_col: 
    with st.container(border=True): 
        nasdaq_data = yf.download(tickers='NQ=F', start=start_date, end=end_date)['Close']
        dod_nasdaq = nasdaq_data.tail(2).pct_change() 
        nasdaq_latest_price = nasdaq_data.tail(1)     

        nasdaq_latest_price_val = nasdaq_latest_price.iloc[0]['NQ=F']
        dod_nasdaq_val = dod_nasdaq.iloc[1]['NQ=F']
        st.subheader('Nasdaq', divider='gray')
        st.markdown(f'**{nasdaq_latest_price_val:,.2f}**') 
        if dod_nasdaq_val > 0:
            st.markdown(f'+{dod_nasdaq_val:.2%}')
        else: 
            st.markdown(f'{dod_nasdaq_val:.2%}')


with btc_col: 
    with st.container(border=True): 
        btc_data = yf.download(tickers='BTC-USD', start=start_date, end=end_date)['Close']
        dod_btc = btc_data.tail(2).pct_change() 
        btc_latest_price = btc_data.tail(1)     

        btc_latest_price_val = btc_latest_price.iloc[0]['BTC-USD']
        dod_btc_val = dod_btc.iloc[1]['BTC-USD']
        st.subheader('BTC/USD', divider='gray')
        st.markdown(f'**{btc_latest_price_val:,.2f}**') 
        if dod_btc_val > 0:
            st.markdown(f'+{dod_btc_val:.2%}')
        else: 
            st.markdown(f'{dod_btc_val:.2%}')


with cable_col: 
    with st.container(border=True): 
        cable_data = yf.download(tickers='GBP=X', start=start_date, end=end_date)['Close']
        dod_cable = cable_data.tail(2).pct_change() 
        cable_latest_price = cable_data.tail(1)     

        cable_latest_price_val = cable_latest_price.iloc[0]['GBP=X']
        dod_cable_val = dod_cable.iloc[1]['GBP=X']
        st.subheader('USD/GBP', divider='gray')
        st.markdown(f'**{cable_latest_price_val:,.2f}**') 
        if dod_cable_val > 0:
            st.markdown(f'+{dod_cable_val:.2%}')
        else: 
            st.markdown(f'{dod_cable_val:.2%}')


#Get data based on ticker and time period
def get_stock_data(ticker, period): 
    stock_df = yf.download(ticker, period=period, multi_level_index=False)
    stock_df = stock_df[['Close', 'High', 'Low', 'Open', 'Volume']]
    return stock_df


def main(): 

    tab1, tab2 = st.tabs(['Stock Dashboard', 'Economic Indicators'])
    with tab1:
        #Set sidebar user parameters     
        stocks_list = ['META', 'AAPL','AMZN', 'NFLX', 'GOOG', 'TSLA', 'NVDA', 'BTC-USD']
        ticker = st.sidebar.selectbox('Select Stock Symbol:', stocks_list, index=2)
        time_period = st.sidebar.selectbox('Time Period', ['1mo', '6mo', '1y', '5y', 'max'])
        chart_type = st.sidebar.selectbox('Chart Type', ['Candlestick', 'Line'])
        st.sidebar.info('Created by Darren Ofoe, view code on [Github](https://github.com/dofoe17.....)')


        st.header(f'Stock Data for {ticker}')


        #if symbol: 
        stock_df = get_stock_data(ticker, time_period)

        #Stock Visualisation
        st.subheader('Candlestick Chart')
        fig = go.Figure()
        if chart_type == 'Candlestick': 
                fig.add_trace(go.Candlestick(
                    x=stock_df.index, 
                    open=stock_df['Open'], 
                    high=stock_df['High'], 
                    low=stock_df['Low'], 
                    close=stock_df['Close']
                )
        )
        else: 
            fig = px.line(stock_df, x=stock_df.index, y=stock_df['Close'])

        fig.update_layout(title=f'{ticker} Candlestick Chart', xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)


        #Summary of data 
        with st.expander('Data Preview'):
            st.dataframe(
                stock_df,
                column_config={'Date':st.column_config.DateColumn('Date', format='YYYY-MM-DD')},
                #format the numbers in the table
                #maybe have the table on the side of the dashboard
                use_container_width=True, 
                hide_index=False
                )  
            
    with tab2: 
        fred_api = st.secrets['API_KEY'] ### DO NOT SHARE ####
        fred = Fred(api_key=fred_api)
        unrate = fred.get_series('UNRATE')
        cpi = fred.get_series('CORESTICKM159SFRBATL')
        
        #visualisation for fred data 
        #Unemployment Rate vs Inflation Rate Visualisation
        fig, ax1 = plt.subplots(figsize=(10, 5))
        ax2 = ax1.twinx() 

        #Add title 
        plt.title('Key Economic Indicators', color='white')

        #Add plots
        l1 = ax1.plot(unrate, color='b', label="Unemployment Rate")
        l2 = ax1.plot(cpi, color='g', label="Inflation Rate")

        #Add labels 
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Percentage (%)', fontsize=12)

        ax1.xaxis.label.set_color('white')
        ax1.yaxis.label.set_color('white')

        #Add legend
        ax1.legend(handles=l1+l2, labelcolor='linecolor')
        st.plotly_chart(fig, use_container_width=True)

main()
