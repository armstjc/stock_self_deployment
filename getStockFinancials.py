import pandas as pd
import yfinance as yf
#from tqdm import tqdm
from zipfile import ZipFile
from RefreshStockAbv import getStockList
import os
from datetime import datetime
#getStockList(3)

stockList = pd.read_csv('Stock_List.csv')
stockListLen = len(stockList)

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths   

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
    
    start = datetime.now()
    arr = stockList['Symbol'].to_numpy()
    arr_len = len(arr)
    arr_count = 0
    workDir = 'Data/StockFinancials/'
    arr = stockList['Symbol'].to_numpy()
    for i in arr.T:
        

        try:
            stock = yf.Ticker(i)
            hist = stock.financials
            df_transposed = hist.transpose()
            df_transposed['ABV'] = i
            df_transposed.to_csv(workDir+i+'.csv')
        except:
            pass
        now = datetime.now()
        durration = now - start
        p_d = str(durration)     
        #print(p_d)   
        arr_count = arr_count +1
        print(f'{p_d} getStockFinancials {arr_count}/{arr_len}: {i}')
    #allDir = get_all_file_paths(workDir)
    #with ZipFile('Data_Final/StockHistory.zip','w') as zip:
    #    # writing each file one by one
    #    for file in allDir:
    #        zip.write(file)


def main():
    getStockFinancials()

if __name__ == "__main__":
    main()
