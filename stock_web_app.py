# Description : this is a stock market dashboard to show some charts and data on some stock

#import the libraries
import streamlit as st
import pandas as pd 
from PIL import Image

#Add title and image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock! Date range from  Jan 4, 2010 - Aug 21, 2020""")

image= Image.open("stock-market-round.png")
st.image(image, use_column_width=True)

#Create a sidebar header
st.sidebar.header('User Input')

#Create a function to get the users input
def get_input():
    start= st.sidebar.text_input('Start Date', "2020-01-01")
    end= st.sidebar.text_input('End Date', "2020-01-01")
    symbol= st.sidebar.text_input('Stock Symbol', "ACA.PA")
    return start, end, symbol


#Create a function to get the company name
def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'ACA.PA':
        return 'Crédit Agricole'
    elif symbol == 'GOOG':
        return 'Alphabet'
    elif symbol == 'TSLA':
        return 'Tesla'
    else: 
        'None'


#Create a function to get the proper company data and the proper timeframe
def get_data(symbol, start, end):

    #Load the data
    if symbol.upper() == 'AMZN':
        df= pd.read_csv('amazon.csv')
    elif symbol.upper() == 'ACA.PA':
        df= pd.read_csv('cagricole.csv')
    elif symbol.upper() == 'GOOG':
        df= pd.read_csv('google.csv')
    elif symbol.upper() == 'TSLA':
        df= pd.read_csv('tesla.csv')
    else:
        df= pd.DataFrame(columns= ['Date', 'High','Low', 'Open', 'Close', 'Volume', 'Adj Close'])


    #Get the date range
    start= pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row= 0 
    end_row = 0

    #Start the date from the top of the data set and go down to see if the users start date is less than or equal to
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i 
            break 

    #Start from the bottom of the dataser and go up to see if the users end date is greater or equal to
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 -j
            break 

    #Set the index to be the date
    df= df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1, :]

#Get the users inputs
start, end, symbol = get_input()
#Get the data
df= get_data(symbol, start, end)
#Get company name
company_name= get_company_name(symbol.upper())

#Display the close price
st.header(company_name + " Close Price \n")
st.line_chart(df['Close'])

#Display the volume
st.header(company_name + " Volume \n")
st.line_chart(df['Volume'])

#Stats
st.header('Data Stats')
st.write(df.describe())