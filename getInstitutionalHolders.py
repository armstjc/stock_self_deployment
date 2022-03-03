import pandas as pd
import yfinance as yf
#from tqdm import tqdm
from RefreshStockAbv import getStockList
from datetime import datetime
stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

##def getInstitutionalHolders():
##    print('show major holders')
##    stock = yf.Ticker("MSFT")
##    stockInstitutionalHolders = stock.institutional_holders
##    #df_transposed = stockMajorHolders.transpose()
##    stockInstitutionalHolders['ABV'] = "MSFT" #stockList['Symbol'][i]
##    stockInstitutionalHolders.to_csv('Data/StockHolders/MajorHolders/'+'MSFT'+'.csv')
##    #print(stockMajorHolders)

def getInstitutionalHolders():
    start = datetime.now()
    print('')
    arr = stockList['Symbol'].to_numpy()
    arr_len = len(arr)
    arr_count = 0
    for i in arr.T:
        stock = yf.Ticker(i)
        stockMajorHolders = stock.institutional_holders

        try:
            stockMajorHolders['ABV'] = i
            stockMajorHolders.to_csv('Data/StockHolders/InstitutionalHolders/'+ i + '_institutional_holders.csv',index=False)
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getInstitutionalHolders {arr_count}/{arr_len}: {i}')

def main():
    print('starting up')
    getInstitutionalHolders()


if __name__ == "__main__":
    main()