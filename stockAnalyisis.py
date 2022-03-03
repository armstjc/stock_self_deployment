#import pandas_ta as ta
import pandas as pd
import os

def combineStockHistories():
    directory = 'Data/StockHistory/'
    dir_list = os.listdir(directory)
    main_df = pd.DataFrame()
    count = 0

    for i in dir_list:
        count = count + 1
        print(i, count)
        df = pd.read_csv(directory+i)
        id = str(i)
        id = id.replace(".csv","")
        df['Stock'] = id
        main_df = pd.concat([main_df,df],ignore_index=True)
    main_df.to_csv('combinedStockHistories.csv')

def analyzeStockHistory():
    directory = 'Data/StockHistory/'
    dir_list = os.listdir(directory)

    for i in dir_list:
        count = count + 1
        print(i, count)

    df = pd.read_csv(directory+i)
    print(df)

def main():
    combineStockHistories()
    analyzeStockHistory()

if __name__ == "__main__":
    main()