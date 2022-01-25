import pandas as pd
import yfinance as yf
from tqdm import tqdm


stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockFinancials():
    '''

    Runs through a csv file with stock abreviations 
    to download the basic financial information of every stock 
    abreviation in a csv file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.

    '''
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.financials
            df_transposed = hist.transpose()
            df_transposed['ABV'] = i
            df_transposed.to_csv('Data/StockFinancials/'+i+'.csv')
        except:
            pass

def main():
    getStockFinancials()

if __name__ == "__main__":
    main()
