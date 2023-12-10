#### Create Dictionary of Cryptocurrencies ####

crypto_dict = {
    "large_cap": {
        "stable": ["USDC", "USDT"],
        "volatile": ["BTC", "ETH", "LTC"]
    },
    "small_cap": {
        "stable": ["GUSD"],
        "volatile": ["MANA", "POLY"]
    }
}

#### Create Questions ####
questions = {
    "large_cap": "Do you want to analyze a large cap coin?",
    "stable": "Do you want to analyze a stable coin?",
}