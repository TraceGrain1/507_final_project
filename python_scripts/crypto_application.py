#### Load Libraries ####
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# change pandas display settings
pd.set_option('display.max_columns', None)


#### Create Main Function ####
def main():
    print("Welcome to the Crypto Recomenndation App")
    print("Let's Find a Cryptocurrency for you to analyze!")
    play(cryptoTree)

#### Create Functions ####
def play(tree):
    """
    """
    if isAnswer(tree):
        return playAnswer(tree)
    else:
        while True:
            answer = input(tree[0] + " (Yes or No) ")
            if answer.lower() == "yes":
                return (tree[0], play(tree[1]), tree[2])
            elif answer.lower() == "no":
                return (tree[0], tree[1], play(tree[2]))
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")


def isAnswer(tree):
    """
    Helper function to determine if the tree is a leaf or not

    parameters: tree

    returns: True if the tree is a leaf, False otherwise
    """
    if tree[1] == None and tree[2] == None:
        return True
    else:
        return False


def playAnswer(tree):
    """
    parameters: tree

    returns: the new tree
    """
    while True:
        answer = input("Please Select a ticker symbol: " + ', '.join(tree[0]) + " (input ticker) ")
        if answer.upper() in tree[0]:
            print("Great choice! Let's analyze " + answer.upper() + ".")
            financialAnalysis(answer.upper())
            break
        else:
            print("Invalid input. Please enter a valid ticker symbol.")


def financialAnalysis(ticker):
    """
    """
    while True:
        # print a new line
        print("\n")
        print("----------------------------------------------------------")
        print("Type \"Exit\" to leave the financial analysis application.")
        plotType = input("For ticker symbol " + ticker +", what would you like to analyze? (Price or Network)")
        if plotType.lower() == "price":
            print("Analyzing price data for " + ticker)
            prices = loadData(ticker, plotType)
            period = input("What type of price data would you like to analyze? (Daily, Weekly, Monthly)")
            if period.lower() == "daily":
                print("Analyzing daily price data for " + ticker)
                newPrices = changePeriod(period, prices)
                priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                if priceOrReturn.lower() == "price":
                    print("Analyzing price data for " + ticker)
                    plotPriceSeries(newPrices, ticker)
                    print("Back To Main Menu")
                elif priceOrReturn.lower() == "return":
                    print("Analyzing return data for " + ticker)
                    newPrices["return"] = newPrices["close"].pct_change()
                    newPrices = newPrices.dropna()
                    plotReturnSeries(newPrices, ticker)
                    print("Back To Main Menu")
                else:
                    print("Invalid input. Please enter 'Price' or 'Return'.")
            elif period.lower() == "weekly":
                newPrices = changePeriod(period, prices)
                priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                if priceOrReturn.lower() == "price":
                    print("Analyzing price data for " + ticker)
                    plotPriceSeries(newPrices, ticker)
                    print("Back To Main Menu")
                elif priceOrReturn.lower() == "return":
                    print("Analyzing return data for " + ticker)
                    newPrices["return"] = newPrices["close"].pct_change()
                    newPrices = newPrices.dropna()
                    plotReturnSeries(newPrices, ticker)
                    print("Back To Main Menu")
                else:
                    print("Invalid input. Please enter 'Price' or 'Return'.")
            elif period.lower() == "monthly":
                newPrices = changePeriod(period, prices)
                priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                if priceOrReturn.lower() == "price":
                    print("Analyzing price data for " + ticker)
                    plotPriceSeries(newPrices, ticker)
                    print("Back To Main Menu")
                elif priceOrReturn.lower() == "return":
                    print("Analyzing return data for " + ticker)
                    newPrices["return"] = newPrices["close"].pct_change()
                    newPrices = newPrices.dropna()
                    plotReturnSeries(newPrices, ticker)
                    print("Back To Main Menu")
                else:
                    print("Invalid input. Please enter 'Price' or 'Return'.")
            else:
                print("Invalid input. Please enter 'Daily', 'Weekly', or 'Monthly'.")
        elif plotType.lower() == "network":
            print("Analyzing network data for " + ticker)
            network = loadData(ticker, plotType)
            period = input("What type of network data would you like to analyze? (Daily, Weekly, Monthly)")
            if period.lower() == "daily":
                print("Analyzing daily network data for " + ticker)
                newNetwork = changePeriod(period, network)
                validInputs = newNetwork.columns.tolist()
                print("\n")
                print("select a number corresponding to the statistic you would like to analyze:")
                print("----------------------------------------------------------")
                for i in range(len(validInputs)):
                    print(validInputs[i] + " : " + str(i))
                print("----------------------------------------------------------")
                numberSelected = input("Select Number: ")
                plotNetworkStatSeries(newNetwork, ticker, validInputs[int(numberSelected)])
                print("Back To Main Menu")
            elif period.lower() == "weekly":
                print("Analyzing weekly network data for " + ticker)
                newNetwork = changePeriod(period, network)
                print(newNetwork.head())
                print("Back To Main Menu")
            elif period.lower() == "monthly":
                print("Analyzing monthly network data for " + ticker)
                newNetwork = changePeriod(period, network)
                print(newNetwork.head())
                print("Back To Main Menu")
            else:
                print("Invalid input. Please enter 'Daily', 'Weekly', or 'Monthly'.")
        elif plotType.lower() == "exit":
            print("Exiting application.")
            tryAgain = input("Would you like to analyze another cryptocurrency? (Yes or No) ")
            if(tryAgain.lower() == "yes"):
                print("\n")
                print("----------------------------------------------------------")
                play(cryptoTree)
            elif(tryAgain.lower() == "no"):
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
        else:
            print("Invalid input. Please enter 'Price' or 'Network'.")

def loadData(ticker, type):
    """
    """
    if type.lower() == "price":
        price = pd.read_json("../json_files/" + ticker + "_price.json", convert_dates=False)
        price["time"] = pd.to_datetime(price["time"], unit="s")
        price = price.drop(columns=["conversionType", "conversionSymbol"])
        price = price.set_index("time")
        return price
    elif type.lower() == "network":
        network = pd.read_json("../json_files/" + ticker + "_blockchain.json", convert_dates=False)
        network = network.drop(columns=["id", "symbol"])
        network["time"] = pd.to_datetime(network["time"], unit="s")
        network = network.set_index("time")
        return network
    else:
        print("Invalid input. Please enter 'Price' or 'Network'.")



def changePeriod(period, data):
    """
    """
    if period.lower() == "daily":
        return data.resample("D").last()
    elif period.lower() == "weekly":
        return data.resample("W").last()
    elif period.lower() == "monthly":
        return data.resample("M").last()
    else:
        print("Invalid input. Please enter 'Daily', 'Weekly', or 'Monthly'.")


def plotPriceSeries(data, ticker):
    """
    """
    fig = px.line(data, x=data.index, y="close")
    fig.update_layout(title="Price Series: " + ticker, xaxis_title="Date", yaxis_title="Price (USD)")
    fig.show()

def plotReturnSeries(data, ticker):
    """
    """
    fig = px.line(data, x=data.index, y="return")
    fig.update_layout(
        title="Return Series: " + ticker,
        xaxis_title="Date",
        yaxis_title="Return",
        yaxis_tickformat=".2%"
    )
    fig.show()

def plotNetworkStatSeries(data, ticker, statistic):
    """
    """
    fig = px.line(data, x=data.index, y=statistic)
    fig.update_layout(title=statistic + " : " + ticker, xaxis_title="Date", yaxis_title=statistic)
    fig.show()

#### Create Tree Data Structure ####
cryptoTree = \
    ("Do you want to analyze a large cap coin?",
        ("Do you want to analyze a stable coin?",
            (["USDC", "USDT"], None, None),
            (["BTC", "ETH", "LTC"], None, None)),
        ("Do you want to analyze a stable coin?",
            (["GUSD"], None, None),
            (["MANA", "POLY"], None, None)))



if __name__ == '__main__':
    main()