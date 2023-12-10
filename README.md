# Cryptocurrency Analysis Application

## Project Description

This is a cryptocurrency analysis application that recommends a few different cryptocurrencies based on a few questions
that the user will answer from a command line prompt. Once a user selects a recommended cryptocurrency, the application
will give you options to plot historical data for price or network data for the selected cryptocurrency.

## Requirements

* Pandas
* Requests
* Plotly

## API KEY

In order to run this application, you will need to obtain an API key from [CryptoCompare](https://min-api.cryptocompare.com/). Go ahead and sign up for a free account and obtain your API key. Update the api_key variable in the api_key.py file with your API key.

## Data Description
### Data Stucture
The data for types of cryptocurrencies to recommend along with questions to ascertain what cryptocurrency to recommend are stored in dictionaries inside the cryptocurrency.py file. This data is used to create a tree structure to recommend cryptocurrencies based on user input through a command line prompt tool.

The `buildTree()` function in the Application_Function.py file is used to build the tree structure from the dictionaries in the cryptocurrency.py file. `buildTree()` is called within crypto_tree_build.py and generates a json file called 'crypto_tree.json'. This file is later loaded in the main application script ('crypto_application.py') and used for the recommendation application.

The data for historical price and network data are obtained from the CryptoCompare API and stored inside json files in the json_files folder.

### Data Summary
In total the number of cryptocurrencies in this version of the application is 8. The cryptocurrencies are:
* Bitcoin
* Ethereum
* Litecoin
* Decentraland
* USD Coin
* Tether
* Gemini Dollar
* Polymath

For each cryptocurrency there is price OHLC (Open, High, Low, Close) data and network data.

The number of records for each cryptocurrency in both the price and network data varies. The data is highly dependent on how long the cryptocurrency has been in existence and the amount of data available for each cryptocurrency.

For instance, the price data for Bitcoin goes back to 2010 whereas the price data for ethereum goes back to 2015. (The price data for all price JSONs has values that go to 2010 may be zero or null values depending on if the cryptocurrency was in existence at that time.)

The data retrieved from the CryptoCompare API contains the following:
* Historical Price Data
    * Time - Unix timestamp
    * High - Highest price of the day
    * Low - Lowest price of the day
    * Open - Opening price of the day
    * volumefrom - Total number of units of the asset specified by fsym
    * volumeto - Worth/value of the total number of units of the asset specified by tsym
    * close - Closing price of the day
* Network Data
    * symbol - Symbol of the cryptocurrency
    * time - Unix timestamp
    * zero_balance_addresses_all_time - Total number of unique addresses with a balance of zero
    * unique_addresses_all_time - Total number of unique addresses
    * new_addresses - Total number of new addresses
    * active_addresses - Total number of active addresses
    * transaction_count - Total number of transactions
    * transaction_count_all_time - Total number of transactions all time
    * large_transaction_count - Total number of large transactions
    * average_transaction_value - Average transaction value
    * block_height - Block height
    * hashrate - Hashrate
    * difficulty - Difficulty
    * block_time - Block time
    * block_size - Block size
    * current_supply - Current supply



## Usage

To run this application please follow the steps below:
1. Clone the repository to your local machine.
2. Obtain an API key from [CryptoCompare](https://min-api.cryptocompare.com/).
3. Update the api_key variable in the api_key.py file with your API key.
4. Run the crypto_application.py
5. Within the command line prompt, answer the questions to get a recommended cryptocurrency.
6. Once a cryptocurrency is selected, you will be given options to plot historical price or network data for the selected cryptocurrency. (Note - More specific instructions will be given in the command line prompt.)
