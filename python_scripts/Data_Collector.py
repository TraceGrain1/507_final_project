#### Data Collector Code ####

#### import libraries ####
import json
import requests
from api_key import api_key
import os


# Define base URL
base_url = "https://min-api.cryptocompare.com/data/"

# Define API Version
version  = "v2"

# Define Endpoints
daily_endpoint = "histoday"
blockchain_endpoint = "blockchain/histo/day"

# Cryptocurrencies to query
crypto = ["BTC", "ETH", "LTC"]

# Conversion currency
fiat = "USD"

############################ Get the price data ############################
crypto_count = 0
for i in crypto:
    params = {
        "fsym": crypto[crypto_count],
        "tsym": fiat,
        "allData": "true"
    }

    # Construct URL
    url = base_url + version + "/" + daily_endpoint

    # Get the price data response
    response = requests.get(url, params=params)

    # Unpack response to json
    data = response.json()
    data = data["Data"]["Data"]

    # Create File name
    file_name = i + "_price.json"

    # Change directory
    os.chdir("../json_files")

    # Write data to file
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

    crypto_count += 1

############################ Get Blockchain Data ############################
blockchain_count = 0
for i in crypto:
    params = {
        "fsym": crypto[blockchain_count],
        "limit": 2000,
        "api_key": api_key
    }

    # Construct URL
    url = base_url + blockchain_endpoint

    # Get the price data response
    response = requests.get(url, params=params)

    # Unpack response to json
    data = response.json()
    data = data["Data"]["Data"]

    # Create File name
    file_name = i + "_blockchain.json"

    # Change directory
    os.chdir("../json_files")

    # Write data to file
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

    blockchain_count += 1
