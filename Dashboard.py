import streamlit as st
import yfinance as yf 
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


st.set_page_config(page_title='My Economic Dashboard', page_icon='💹', layout='wide')

st.title('Stock App Dashboard')

#Date range 
end_date = pd.to_datetime('today')#.strftime('%Y-%m-%d')
start_date = end_date - pd.DateOffset(years=1) #1 year ago

sp_col, ftse_col, nasdaq_col, cable_col, btc_col = st.columns(5)

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
            st.markdown(f':green[+{dod_sp_val:.2%}]')
        else: 
            st.markdown(f':red[{dod_sp_val:.2%}]')
        
        sp_fig = px.line(sp_data, x=sp_data.index, y=sp_data['^GSPC'])
        sp_fig.update_layout(
            yaxis_showticklabels=False,
            yaxis_title=None,
            xaxis_visible=False,
            autosize=False, 
            height=225
            )
        sp_fig.update_traces(line_color='purple')
        st.plotly_chart(sp_fig, use_container_width=True)


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
            st.markdown(f':green[+{dod_ftse_val:.2%}]')
        else: 
            st.markdown(f':red[{dod_ftse_val:.2%}]')

        ftse_fig = px.line(ftse_data, x=ftse_data.index, y=ftse_data['^FTSE'])
        ftse_fig.update_layout(
            yaxis_showticklabels=False,
            yaxis_title=None,
            xaxis_visible=False,
            autosize=False, 
            height=225
            )
        ftse_fig.update_traces(line_color='orange')
        st.plotly_chart(ftse_fig, use_container_width=True)


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
            st.markdown(f':green[+{dod_nasdaq_val:.2%}]')
        else: 
            st.markdown(f':red[{dod_nasdaq_val:.2%}]')

        nasdaq_fig = px.line(nasdaq_data, x=nasdaq_data.index, y=nasdaq_data['NQ=F'])
        nasdaq_fig.update_layout(
            yaxis_showticklabels=False,
            yaxis_title=None,
            xaxis_visible=False,
            autosize=False, 
            height=225
            )
        nasdaq_fig.update_traces(line_color='darkblue')
        st.plotly_chart(nasdaq_fig, use_container_width=True)


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
            st.markdown(f':green[+{dod_btc_val:.2%}]')
        else: 
            st.markdown(f':red[{dod_btc_val:.2%}]')

        btc_fig = px.line(btc_data, x=btc_data.index, y=btc_data['BTC-USD'])
        btc_fig.update_layout(
            yaxis_showticklabels=False,
            yaxis_title=None,
            xaxis_visible=False,
            autosize=False, 
            height=225
            )
        btc_fig.update_traces(line_color='yellow')
        st.plotly_chart(btc_fig, use_container_width=True)



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
            st.markdown(f':green[+{dod_cable_val:.2%}]')
        else: 
            st.markdown(f':red[{dod_cable_val:.2%}]')

        cable_fig = px.line(cable_data, x=cable_data.index, y=cable_data['GBP=X'])
        cable_fig.update_layout(
            yaxis_showticklabels=False,
            yaxis_title=None,
            xaxis_visible=False,
            autosize=False, 
            height=225
            )
        cable_fig.update_traces(line_color='white')
        st.plotly_chart(cable_fig, use_container_width=True)


#Get data based on ticker and time period
def get_stock_data(ticker, period): 
    stock_df = yf.download(ticker, period=period, multi_level_index=False)
    stock_df = stock_df[['Close', 'High', 'Low', 'Open', 'Volume']]
    return stock_df


#Calculate metric data
def calculate_metric_data(stock_df): 
    last_price = stock_df.iloc[-1]['Close']
    previous_day_close = stock_df.iloc[-2]['Close']
    percentage_change = ((last_price - previous_day_close) / previous_day_close) * 100 
    return percentage_change, last_price


def main(): 

    #Set sidebar user parameters     
    st.sidebar.title('Parameters')
    stocks_list = ['META', 'AAPL','AMZN', 'NFLX', 'GOOG', 'TSLA', 'NVDA', 'BTC-USD']
    ticker = st.sidebar.selectbox('Select Stock Ticker:', stocks_list, index=0) #Index defaults value to first option
    tickerdata = yf.Ticker(ticker)
    time_period = st.sidebar.selectbox('Time Period', ['1mo', '6mo', '1y', '5y', 'max'], index=2)
    chart_type = st.sidebar.selectbox('Chart Type', ['Candlestick', 'Line'])        
    st.sidebar.info('Created by Darren Ofoe, view code on [Github](https://github.com/dofoe17/Economic-Dashboard/blob/main/Dashboard.py)') 
            
    st.header(f'Stock Data for {ticker}')
    
    stock_df = get_stock_data(ticker, time_period)

    percentage_change, last_price = calculate_metric_data(stock_df)

    #Add metrics to provide at glance summary
    st.metric('Close Price', f'${last_price:,.2f}', delta=f'{percentage_change:+.2f}%')


    #Stock Visualisation
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

    fig.update_layout(title=f'{ticker} Chart', xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)


    #Pull recommendation from yfinance data
    try:
        string_rec = tickerdata.info['recommendationKey']
        st.info(f'Analyst recommendation: {string_rec}')
    except KeyError:
        st.error(f'Yahoo finance cannot find recommendation for: {ticker}') 

 

    tab1, tab2 = st.tabs(['Data Summary', 'Stock Info'])
    with tab1:    #Summary of data 
        with st.expander('Data Preview - Click to expand'):
            st.dataframe(
                stock_df,
                column_config={
                    'Date':st.column_config.DateColumn(
                    'Date',
                    format='YYYY-MM-DD'
                    ), 
                    'Volume':st.column_config.NumberColumn(
                        'Volume', format='localized'
                    )
                    },
                use_container_width=True, 
                hide_index=False
                ) 
    with tab2: 
        stock_summary = tickerdata.info['longBusinessSummary']
        stock_name = tickerdata.info['longName']
        st.subheader(stock_name)
        st.info(stock_summary)
main()
