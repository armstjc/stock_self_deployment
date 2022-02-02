import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList
from datetime import datetime
#getStockList(3)

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockOptions():
    arr = stockList['Symbol'].to_numpy()
    start = datetime.now()
    arr_len = len(arr)
    arr_count = 0
    for i in arr.T:
        try:
            stockABV = i
            stock = yf.Ticker(stockABV)
            options = stock.options
            datalist = list(options)
            listOptions = pd.DataFrame(datalist, columns=['Dates'])
            for s in listOptions.index:
                opt = stock.option_chain(listOptions['Dates'][s])
                optCallsTable = opt.calls
                optCallsTable['ABV'] = i
                optCallsTable.to_csv('Data/StockOptions/Calls/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
                optPutsTable = opt.puts
                optPutsTable['ABV'] = i
                optPutsTable.to_csv('Data/StockOptions/Puts/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getStockOptions {arr_count}/{arr_len}: {i}')

def main():
    print('starting up')
    getStockOptions()


if __name__ == "__main__":
    main()