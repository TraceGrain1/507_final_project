#### Application Functions ####
import pandas as pd
import plotly.express as px
from cryptocurrency import crypto_dict, questions

#### PLAY FUNCTION ####
def play(tree):
    """
    Function to be able to enter the recommendation system

    play function will take in a tree and ask the user questions to determine the best cryptocurrency to analyze

    parameters: tree

    returns: the new tree
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

#### IS ANSWER FUNCTION ####
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

#### PLAY ANSWER FUNCTION ####
def playAnswer(tree):
    """
    Helper function to return the answer of the tree

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

#### FINANCIAL ANALYSIS FUNCTION ####
def financialAnalysis(ticker):
    """
    Function to analyze the financial data of a cryptocurrency

    financialAnalysis function will take in a ticker symbol and ask the user what type of analysis they would like to perform

    There is one main menu and two submenus for price and network analysis

    The main menu will ask the user if they would like to analyze price or network data

    The price submenu will ask the user if they would like to analyze daily, weekly, or monthly price data

    Within the daily, weekly, and monthly price submenus, the user will be asked if they would like to analyze price or return data

    when the user selects price or return data, the function will plot the price or return series for the selected period

    The network submenu will ask the user if they would like to analyze daily, weekly, or monthly network data

    Within the daily, weekly, and monthly network submenus, the user will be asked to select a statistic to analyze

    when the user selects a statistic, the function will plot the network statistic series for the selected period

    parameters: ticker

    returns: None
    """
    on = True
    on2 = True
    while on == True:
        print("----------------------------------------------------------")
        print("MAIN MENU")
        print("Type \"Quit\" to leave the financial analysis application.")
        plotType = input("For ticker symbol " + ticker +", what would you like to analyze? (Price or Network)")
        if plotType.lower() == "price":
            while True:
                print("----------------------------------------------------------")
                print("PRICE PERIOD MENU")
                print("Type \"E\" to go back to the MAIN MENU.")
                print("Analyzing price data for " + ticker + "...")
                prices = loadData(ticker, plotType)
                period = input("What type of price data would you like to analyze? (Daily, Weekly, Monthly)")
                if period.lower() == "daily":
                    while True:
                        print("----------------------------------------------------------")
                        print("PRICE OR RETURN MENU")
                        print("Type \"E\" to go back to the PRICE PERIOD MENU.")
                        print("Analyzing daily price data for " + ticker)
                        newPrices = changePeriod(period, prices)
                        priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                        if priceOrReturn.lower() == "price":
                            print("----------------------------------------------------------")
                            print("Analyzing price data for " + ticker)
                            plotPriceSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "return":
                            print("----------------------------------------------------------")
                            print("Analyzing return data for " + ticker)
                            newPrices["return"] = newPrices["close"].pct_change()
                            newPrices = newPrices.dropna()
                            plotReturnSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "e":
                            break
                        else:
                            print("Invalid input. Please enter 'Price' or 'Return'.")
                elif period.lower() == "weekly":
                    while True:
                        print("----------------------------------------------------------")
                        print("PRICE OR RETURN MENU")
                        print("Type \"E\" to go back to the PERIOD MENU.")
                        print("Analyzing daily price data for " + ticker)
                        newPrices = changePeriod(period, prices)
                        priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                        if priceOrReturn.lower() == "price":
                            print("----------------------------------------------------------")
                            print("Analyzing price data for " + ticker)
                            plotPriceSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "return":
                            print("----------------------------------------------------------")
                            print("Analyzing return data for " + ticker)
                            newPrices["return"] = newPrices["close"].pct_change()
                            newPrices = newPrices.dropna()
                            plotReturnSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "e":
                            break
                        else:
                            print("Invalid input. Please enter 'Price' or 'Return'.")
                elif period.lower() == "monthly":
                    while True:
                        print("----------------------------------------------------------")
                        print("PRICE OR RETURN MENU")
                        print("Type \"E\" to go back to the PERIOD MENU.")
                        print("Analyzing daily price data for " + ticker)
                        newPrices = changePeriod(period, prices)
                        priceOrReturn = input("Would you like to analyze price or return data? (Price or Return) ")
                        if priceOrReturn.lower() == "price":
                            print("----------------------------------------------------------")
                            print("Analyzing price data for " + ticker)
                            plotPriceSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "return":
                            print("----------------------------------------------------------")
                            print("Analyzing return data for " + ticker)
                            newPrices["return"] = newPrices["close"].pct_change()
                            newPrices = newPrices.dropna()
                            plotReturnSeries(newPrices, ticker)
                        elif priceOrReturn.lower() == "e":
                            break
                        else:
                            print("Invalid input. Please enter 'Price' or 'Return'.")
                elif period.lower() == "e":
                    break
                else:
                    print("Invalid input. Please enter 'Daily', 'Weekly', 'Monthly' or 'E'.")
        elif plotType.lower() == "network":
            while True:
                print("----------------------------------------------------------")
                print("NETWORK PERIOD MENU")
                print("Type \"E\" to go back to the MAIN MENU.")
                network = loadData(ticker, plotType)
                period = input("What type of network data would you like to analyze? (Daily, Weekly, Monthly)")
                if period.lower() == "daily":
                    while True:
                        newNetwork = changePeriod(period, network)
                        validInputs = newNetwork.columns.tolist()
                        print("----------------------------------------------------------")
                        print("NETWORK PLOTS MENU")
                        print("Type \"E\" to go back to the NETWORK PERIOD MENU.")
                        print("Analyzing daily network data for " + ticker)
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print("Select a number corresponding to the statistic you would like to analyze:")
                        print("----------------------------------------------------------")
                        for i in range(len(validInputs)):
                            print(validInputs[i] + " : " + str(i))
                        print("----------------------------------------------------------")
                        numberSelected = input("Select Number: ")
                        try:
                            if int(numberSelected) < len(validInputs) and int(numberSelected) >= 0:
                                plotNetworkStatSeries(newNetwork, ticker, validInputs[int(numberSelected)])
                        except ValueError:
                            pass
                        try:
                            if numberSelected.lower() == "e":
                                break
                        except ValueError:
                            pass
                elif period.lower() == "weekly":
                    while True:
                        newNetwork = changePeriod(period, network)
                        validInputs = newNetwork.columns.tolist()
                        print("----------------------------------------------------------")
                        print("NETWORK PLOTS MENU")
                        print("Type \"E\" to go back to the NETWORK PERIOD MENU.")
                        print("Analyzing daily network data for " + ticker)
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print("Select a number corresponding to the statistic you would like to analyze:")
                        print("----------------------------------------------------------")
                        for i in range(len(validInputs)):
                            print(validInputs[i] + " : " + str(i))
                        print("----------------------------------------------------------")
                        numberSelected = input("Select Number: ")
                        try:
                            if int(numberSelected) < len(validInputs) and int(numberSelected) >= 0:
                                plotNetworkStatSeries(newNetwork, ticker, validInputs[int(numberSelected)])
                        except ValueError:
                            pass
                        try:
                            if numberSelected.lower() == "e":
                                break
                        except ValueError:
                            pass
                elif period.lower() == "monthly":
                    while True:
                        newNetwork = changePeriod(period, network)
                        validInputs = newNetwork.columns.tolist()
                        print("----------------------------------------------------------")
                        print("NETWORK PLOTS MENU")
                        print("Type \"E\" to go back to the NETWORK PERIOD MENU.")
                        print("Analyzing daily network data for " + ticker)
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print("Select a number corresponding to the statistic you would like to analyze:")
                        print("----------------------------------------------------------")
                        for i in range(len(validInputs)):
                            print(validInputs[i] + " : " + str(i))
                        print("----------------------------------------------------------")
                        numberSelected = input("Select Number: ")
                        try:
                            if int(numberSelected) < len(validInputs) and int(numberSelected) >= 0:
                                plotNetworkStatSeries(newNetwork, ticker, validInputs[int(numberSelected)])
                        except ValueError:
                            pass
                        try:
                            if numberSelected.lower() == "e":
                                break
                        except ValueError:
                            pass
                elif period.lower() == "e":
                    break
                else:
                    print("Invalid input. Please enter 'Daily', 'Weekly', 'Monthly' or 'E'.")
        elif plotType.lower() == "quit":
            while on2 == True:
                tryAgain = input("Would you like to analyze another cryptocurrency? (Yes or No) ")
                if(tryAgain.lower() == "yes"):
                    print("\n")
                    print("----------------------------------------------------------")
                    play(buildTree(crypto_dict, questions))
                elif(tryAgain.lower() == "no"):
                    print("Exiting application.")
                    on = False
                    on2 = False
                    break
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
        else:
            print("Invalid input. Please enter 'Price' or 'Network'.")

#### LOAD DATA FUNCTION ####
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
        print("Invalid input. Please enter 'Price', 'Network' or 'Quit'.")

#### CHANGE PERIOD FUNCTION ####
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

#### PLOT PRICE SERIES FUNCTION ####
def plotPriceSeries(data, ticker):
    """
    """
    fig = px.line(data, x=data.index, y="close")
    fig.update_layout(title="Price Series: " + ticker, xaxis_title="Date", yaxis_title="Price (USD)")
    fig.show()

#### PLOT RETURNS SERIES FUNCTION ####
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

#### PLOT NETWORK STATS SERIES FUNCTION ####
def plotNetworkStatSeries(data, ticker, statistic):
    """
    This function will plot the network statistic series for the selected period

    parameters: data, ticker, statistic

    returns: None
    """
    fig = px.line(data, x=data.index, y=statistic)
    fig.update_layout(title=statistic + " : " + ticker, xaxis_title="Date", yaxis_title=statistic)
    fig.show()

#### TREE DATA STRUCTOR CONTRUCTOR ####
def buildTree(crypto_dict, questions):
    """
    Function to build the tree data structure

    buildTree function will take in a dictionary of cryptocurrencies and a dictionary of questions to build the tree data structure

    parameters: crypto_dict, questions

    returns: the tree data structure
    """
    # create the first node of the tree with the first question
    mainNode = (questions["large_cap"])

    # create the second node of the tree with the second question
    secondNode = (questions["stable"])

    # create the third node of the tree with the third question
    thirdNode = (questions["stable"])

    # create the large cap leaf nodes
    largeCapLeaf1 = (crypto_dict["large_cap"]["stable"])
    largeCapLeaf2 = (crypto_dict["large_cap"]["volatile"])

    # create the Small cap leaf nodes
    smallCapLeaf1 = (crypto_dict["small_cap"]["stable"])
    smallCapLeaf2 = (crypto_dict["small_cap"]["volatile"])

    # construct the tree
    tree = (mainNode, (secondNode, (largeCapLeaf1, None, None), (largeCapLeaf2, None, None)), (thirdNode, (smallCapLeaf1, None, None), (smallCapLeaf2, None, None)))
    return tree