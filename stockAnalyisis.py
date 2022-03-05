from numpy import False_
from ta.momentum import *
from ta.volume import *
from ta.volatility import *
from ta.trend import *
from ta.others import *
import pandas as pd
import os
from datetime import datetime

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

def useCommonIndicators():
    directory = 'Data/StockHistory/'
    dest_directory = 'Data_Final/StockHistory/'
    dir_list = os.listdir(directory)
    fileCount = 0
    for path in dir_list:
        #check if path is a file
        fileCount += 1
    start = datetime.now()
    count = 0
    for i in dir_list:
        count = count + 1
        hist = pd.read_csv(directory+i)
        #hist = dropna(df)
        Trend_MACD = MACD(close=hist.Close)
        hist['MACD Line'] = Trend_MACD.macd()
        hist['MACD Histogram'] = Trend_MACD.macd_diff()
        hist['MACD Signal Line'] = Trend_MACD.macd_signal()

        Momentum_RSI = RSIIndicator(close=hist.Close,window=14)
        hist['RSI'] = Momentum_RSI.rsi()

        Trend_EMA = EMAIndicator(close=hist.Close)
        hist['EMA'] = Trend_EMA.ema_indicator()
        Volitility_Bollinger = BollingerBands(close=hist.Close)
        hist['Bollinger High Band'] = Volitility_Bollinger.bollinger_hband()
        hist['Bollinger High Band Indicator'] = Volitility_Bollinger.bollinger_hband_indicator()
        hist['Bollinger Low Band'] = Volitility_Bollinger.bollinger_lband()
        hist['Bollinger Low Band Indicator'] = Volitility_Bollinger.bollinger_lband_indicator()
        hist['Bollinger Middle Band'] = Volitility_Bollinger.bollinger_mavg()
        hist['Bollinger Percetage Band'] = Volitility_Bollinger.bollinger_pband()
        hist['Bollinger Band Width'] = Volitility_Bollinger.bollinger_wband()

        Momentum_StochasticOscillator = StochasticOscillator(hist.High, hist.Low, hist.Close)
        hist['Stochastic Oscillator'] = Momentum_StochasticOscillator.stoch()
        hist['Stochastic Oscillator_Signial'] = Momentum_StochasticOscillator.stoch_signal()

        hist.to_csv(dest_directory+i,index=False)
        now = datetime.now()
        durration = now - start
        p_d = str(durration)   
        print(p_d, i, count)

    df = pd.read_csv(directory+i)
    print(df)

def main():

    useCommonIndicators()
    #combineStockHistories()

if __name__ == "__main__":
    main()