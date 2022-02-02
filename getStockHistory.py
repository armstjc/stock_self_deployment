import pandas as pd
import yfinance as yf
from tqdm import tqdm
from datetime import datetime

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockHistory():
    '''

    Runs through a csv file with stock abreviations 
    to download the daily history of every stock in the file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.
   
    '''
    print('Getting the full history of the stock market.')
    arr = stockList['Symbol'].to_numpy()
    start = datetime.now()
    arr_len = len(arr)
    arr_count = 0
    for i in arr.T:
        try:
            stock = yf.Ticker(i)
            hist = stock.history(period="max")
            hist.to_csv('Data/StockHistory/'+i+'.csv')
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getStockHistory {arr_count}/{arr_len}: {i}')

def main():
    getStockHistory()

if __name__ == "__main__":
    main()
