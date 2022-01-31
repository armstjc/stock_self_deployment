import pandas as pd
import yfinance as yf
from tqdm import tqdm
from RefreshStockAbv import getStockList

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def getStockRecommendations():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockRecommendations = stock.recommendations

        try:
            stockRecommendations['ABV'] = i
            stockRecommendations.to_csv('Data/StockRecommendations/'+ i + '_recommendations.csv')
        except:
            pass


def main():
    print('starting up')
    getStockRecommendations()


if __name__ == "__main__":
    main()