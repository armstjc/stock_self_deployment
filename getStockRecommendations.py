import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList
from datetime import datetime

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockRecommendations():
    print('')
    arr = stockList['Symbol'].to_numpy()
    start = datetime.now()
    arr_len = len(arr)
    arr_count = 0

    for i in arr.T:
        
        stock = yf.Ticker(i)
        stockRecommendations = stock.recommendations

        try:
            stockRecommendations['ABV'] = i
            stockRecommendations.to_csv('Data/StockRecommendations/'+ i + '_recommendations.csv')
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getStockRecommendations {arr_count}/{arr_len}: {i}')

def main():
    print('starting up')
    getStockRecommendations()


if __name__ == "__main__":
    main()