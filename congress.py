
import pandas as pd



def getHouseTransactions():
    '''

    Grabs a list of stock transactions made by various members of the 
    United States House of Representatives. 

    Data has been croud sourced from the House Stock Watcher website.
    Link: https://housestockwatcher.com/

    '''
    URL = 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'
    houseDF = pd.read_json(URL)
    houseDF.to_csv('Data/Congress/houseTransactions.csv' )
    print(houseDF)

def getSenateTransactions():
    '''

    Grabs a list of stock transactions made by various members of the 
    United States Senate. 

    Data has been croud sourced from the Senate Stock Watcher website.
    Link: https://housestockwatcher.com/

    '''
    URL = 'https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json'
    senateDF = pd.read_json(URL)
    senateDF.to_csv('Data/Congress/senateTransactions.csv' )
    print(senateDF)

def congress():
    getHouseTransactions()
    getSenateTransactions()

def main():
    print('')
    getHouseTransactions()
    getSenateTransactions()

if __name__ == "__main__":
    main()