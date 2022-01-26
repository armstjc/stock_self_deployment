## Script created by Joseph Armstrong (armstjc@mail.uc.edu
## Latest Script edit: 10/05/2021
##
## Script name: RefreshStockAbv.py
## Script use case: Downloads a list of US stocks for these scripts to use

from urllib.request import urlopen
import pandas as pd

def getStockAbv():
    
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/all/all_tickers.txt"
    file = urlopen(url)
    stockDF = pd.read_csv(file, sep=" ", header=None, names=["Symbol"])
    stockDF.to_csv('Stock_List.csv',index=False)
    print(stockDF)

def getNyseStockABV():
    
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_tickers.txt"
    file = urlopen(url)
    stockDF = pd.read_csv(file, sep=" ", header=None, names=["Symbol"])
    stockDF.to_csv('Stock_List.csv',index=False)
    print(stockDF)

def getNasdaqStockABV():

    
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_tickers.txt"
    file = urlopen(url)
    stockDF = pd.read_csv(file, sep=" ", header=None, names=["Symbol"])
    stockDF.to_csv('Stock_List.csv',index=False)
    print(stockDF)

def getAmexStockABV():

    
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/amex/amex_tickers.txt"
    file = urlopen(url)
    stockDF = pd.read_csv(file, sep=" ", header=None, names=["Symbol"])
    stockDF.to_csv('Stock_List.csv',index=False)
    print(stockDF)

def getStockList(inputNum=0):
    if(inputNum=0):
        getStockAbv()
    else:
        print('fail')

def main():
    getStockList()

if __name__ == "__main__":
    main()
