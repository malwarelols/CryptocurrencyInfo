#!/usr/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Cryptocurrencies</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>MalwareLol</bitbar.author>
# <bitbar.author.github>malwarelols</bitbar.author.github>
# <bitbar.desc>A macOS plugin to track stats relating to your own personal cryptocurrency investments!</bitbar.desc>
# <bitbar.image>http://gis.ee/files/pihole-bitbar.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

import requests
import json

# insert information about each currency here -- the number of tokens/coins you hodl and the total cost in your currency 
# a) XLM information
number_of_xlm = 2461.00
total_cost_xlm = 199.00
# b) XVG information
number_of_xvg = 1148.00
total_cost_xvg = 78.00

# API request to coinmarketcap for the current information about XLM
xlm_api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/stellar/")
stellar = json.loads(xlm_api_request.content)
for s in stellar:
    stellar_price = float(s['price_usd']) * 0.75 # Takes the current from coinmarketcap in USD and converts to GBP. To get prices in USD, remove the * 0.75
    stellar_total_value = (stellar_price * number_of_xlm) # The total value is the number of tokens/coins multipled by the current cost as per coinmarketcap
    stellar_percentage = (((stellar_total_value - total_cost_xlm)/total_cost_xlm) * 100) # Calculation for working out the profit/loss percentage
    stellar_profit = (stellar_total_value - total_cost_xlm) # Calculation for the total profit in money

# API request to coinmarketcap for the current infomation on XVG -- see the code comments above for explanation of what each line is doing.
xvg_api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/verge/")
verge = json.loads(xvg_api_request.content)
for v in verge:
    verge_price = float(v['price_usd']) * 0.75
    verge_total_value = (verge_price * number_of_xvg)
    verge_percentage = (((verge_total_value - total_cost_xvg)/total_cost_xvg) * 100)
    verge_profit = (verge_total_value - total_cost_xvg)

try:
    print("💰")
    print("---")
    print("{sym} = £{price}".format(sym=s['symbol'],price=stellar_price))
    print("Total value: £{0:.2f}".format(stellar_total_value))
    print("{0:.2f}%".format(stellar_percentage))
    print("XLM Profit: £{0:.2f}".format(stellar_profit))
    print("---")
    print("{sym} = £{price}".format(sym=v['symbol'],price=verge_price))
    print("Total value: £{0:.2f}".format(verge_total_value))
    print("{0:.2f}%".format(verge_percentage))
    print("XVG Profit: £{0:.2f}".format(verge_profit))
    print("---")
    print("Overall Profit: £{0:.2f}".format(stellar_profit + verge_profit))

except:
    print("❌")
    print("---")
    print("Error.")
    print("---")