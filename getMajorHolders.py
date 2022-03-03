import pandas as pd
import yfinance as yf
#from tqdm import tqdm
from RefreshStockAbv import getStockList
from datetime import datetime
stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getMajorHolders():
    print('')
    start = datetime.now()
    arr = stockList['Symbol'].to_numpy()
    arr_len = len(arr)
    arr_count = 0
    for i in arr.T:

        stock = yf.Ticker(i)
        stockMajorHolders = stock.major_holders

        try:
            stockMajorHolders['ABV'] = i
            stockMajorHolders.to_csv('Data/StockHolders/MajorHolders/'+ i + '_major_holders.csv',index=False)
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getMajorHolders {arr_count}/{arr_len}: {i}')

def main():
    print('starting up')
    getMajorHolders()


if __name__ == "__main__":
    main()