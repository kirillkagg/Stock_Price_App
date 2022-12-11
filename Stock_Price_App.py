import streamlit as st
import yfinance as yf
import cufflinks as cf
from datetime import date, timedelta

# App title
st.markdown('''
# Stock Price App
''')
st.write('---')

# Retrieving tickers data
with st.form(key='form1'):
    tickerSymbol = st.text_input("Ticket", "AAPL").upper()
    submit = st.form_submit_button(label='CHECK IT')
tickerData = yf.Ticker(tickerSymbol)

# Ticker information
col1, col2, col3 = st.columns(3)

with col1:
    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)
with col2:
    st.write(' ')
with col3:
    st.write(' ')
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

with st.expander("About Company"):
    st.write(tickerData.info["longBusinessSummary"])

a = 5
b = 4
c = 3
d = 2
e = 1

col1, col2, col3 = st.columns(3)

with col1:
    option = st.selectbox(
        'Y',
        (a, b, c, d, e,))
    if option == a:
        timedelta = timedelta(days=365 * 5)
    if option == b:
        timedelta = timedelta(days=365 * 4)
    if option == c:
        timedelta = timedelta(days=365 * 3)
    if option == d:
        timedelta = timedelta(days=365 * 2)
    if option == e:
        timedelta = timedelta(days=365 * 1)
with col2:
    Start_date = st.date_input(
        "Start date",
        (date.today() - timedelta))
with col3:
    End_date = st.date_input(
        "End date",
        date.today())

# Bollinger bands
st.header('**Bollinger Bands**')
qf = cf.QuantFig(tickerData.history(period='1d', start=Start_date, end=End_date), title='First Quant Figure',
                 legend='top', name='GS')
qf.add_rsi(periods=20, color='java')
qf.add_bollinger_bands(periods=20, boll_std=2, colors=['magenta', 'grey'], fill=True)
qf.add_volume()
fig = qf.iplot(asFigure=True, dimensions=(800, 600))
st.plotly_chart(fig)

st.write('---')
# st.write(tickerData.info)
st.markdown('''
# About Company
''')
st.write('---')

# About Company
st.subheader("""Daily **closing price** for """ + tickerSymbol)
stock_data = yf.Ticker(tickerSymbol)
stock_df = stock_data.history(period='1d', start=Start_date, end=None)
st.line_chart(stock_df.Close)

Institutional_investors = st.checkbox('Institutional investors')
if Institutional_investors:
    st.subheader("""**Institutional investors** for """ + tickerSymbol)
    display_shareholders = stock_data.institutional_holders
    if display_shareholders.empty:
        st.write("No data available at the moment")
    else:
        st.write(display_shareholders)

Stock_Actions__Quarterly_Earnings = st.checkbox('Stock Actions ' ' + ' ' Quarterly Earnings')
if Stock_Actions__Quarterly_Earnings:
    coll, colll = st.columns(2)
    with coll:
        st.subheader("""Stock **actions** for """ + tickerSymbol)
        display_action = stock_data.actions
        if display_action.empty:
            st.write("No data available at the moment")
        else:
            st.write(display_action)
    with colll:
        st.subheader("""**Quarterly earnings** for """ + tickerSymbol)
        display_earnings = stock_data.quarterly_earnings
        if display_earnings.empty:
            st.write("No data available at the moment")
        else:
            st.write(display_earnings)

Quarterly_Financials = st.checkbox("Quarterly Financials")
if Quarterly_Financials:
    st.subheader("""**Quarterly financials** for """ + tickerSymbol)
    display_financials = stock_data.quarterly_financials
    if display_financials.empty:
        st.write("No data available at the moment")
    else:
        st.write(display_financials)

Quarterly_Balance_Sheet = st.checkbox("Quarterly Balance Sheet")
if Quarterly_Balance_Sheet:
    st.subheader("""**Quarterly balance sheet** for """ + tickerSymbol)
    display_balancesheet = stock_data.quarterly_balance_sheet
    if display_balancesheet.empty:
        st.write("No data available at the moment")
    else:
        st.write(display_balancesheet)

Quarterly_Cashflow = st.checkbox("Quarterly Cashflow")
if Quarterly_Cashflow:
    st.subheader("""**Quarterly cashflow** for """ + tickerSymbol)
    display_cashflow = stock_data.quarterly_cashflow
    if display_cashflow.empty:
        st.write("No data available at the moment")
    else:
        st.write(display_cashflow)

Analysts_Recommendation = st.checkbox("Analysts Recommendation")
if Analysts_Recommendation:
    st.subheader("""**Analysts recommendation** for """ + tickerSymbol)
    display_analyst_rec = stock_data.recommendations
    if display_analyst_rec.empty:
        st.write("No data available at the moment")
    else:
        st.write(display_analyst_rec)

stock = st.checkbox("FINVIZ")
if stock:
    st.subheader("""**FINVIZ for** """ + tickerSymbol)
    from finvizfinance.quote import finvizfinance

    stock = finvizfinance(tickerSymbol)
    st.image(stock.ticker_charts())
