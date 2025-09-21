Economic Indicator Dashboard

Create multiple containers to give headline of selected stocks. 

```ruby
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
```



<img width="1897" height="495" alt="image" src="https://github.com/user-attachments/assets/968d4a9e-2cb3-4297-90c1-e729b01f5172" />


Add sidebar info: 

```ruby
    st.sidebar.title('Parameters')
    stocks_list = ['META', 'AAPL','AMZN', 'NFLX', 'GOOG', 'TSLA', 'NVDA', 'BTC-USD']
    ticker = st.sidebar.selectbox('Select Stock Ticker:', stocks_list, index=0) #Index defaults value to first option
    tickerdata = yf.Ticker(ticker)
    time_period = st.sidebar.selectbox('Time Period', ['1mo', '6mo', '1y', '5y', 'max'], index=2)
    chart_type = st.sidebar.selectbox('Chart Type', ['Candlestick', 'Line'])        
    st.sidebar.info('Created by Darren Ofoe, view code on [Github](https://github.com/dofoe17/Economic-Dashboard/blob/main/Dashboard.py)') 
```


Add visualisation with analyst recommendations

```ruby
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
```


<img width="1896" height="602" alt="image" src="https://github.com/user-attachments/assets/90e66aba-f8ea-49a4-94c8-596f2dec4571" />

Finally, create the two tabs with data table and stock information. 

```ruby
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
```

<img width="1683" height="490" alt="image" src="https://github.com/user-attachments/assets/28816175-ade6-4b13-832b-67262f80fe6b" />

<img width="1625" height="275" alt="image" src="https://github.com/user-attachments/assets/6963402a-74da-4b4f-8728-21a23afe32e1" />
