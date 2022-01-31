import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getMajorHolders():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockMajorHolders = stock.major_holders

        try:
            stockMajorHolders['ABV'] = i
            stockMajorHolders.to_csv('Data/StockHolders/MajorHolders/'+ i + '_major_holders.csv',index=False)
        except:
            pass

def main():
    print('starting up')
    getMajorHolders()


if __name__ == "__main__":
    main()