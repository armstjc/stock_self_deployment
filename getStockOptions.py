import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList
#getStockList(3)

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockOptions():
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
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

def main():
    print('starting up')
    getStockOptions()


if __name__ == "__main__":
    main()