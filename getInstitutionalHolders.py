import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList

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
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockMajorHolders = stock.institutional_holders

        try:
            stockMajorHolders['ABV'] = i
            stockMajorHolders.to_csv('Data/StockHolders/InstitutionalHolders/'+ i + '_institutional_holders.csv',index=False)
        except:
            pass

def main():
    print('starting up')
    getInstitutionalHolders()


if __name__ == "__main__":
    main()