import pandas as pd
import yfinance as yf
from tqdm import tqdm


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
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.history(period="max")
            hist.to_csv('Data/StockHistory/'+i+'.csv')
        except:
            pass

def main():
    getStockHistory()

if __name__ == "__main__":
    main()
