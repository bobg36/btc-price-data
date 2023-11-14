1. run "convert_minute_candles.py"
    - enter timeframe when prompted, in minutes
    - higher timeframes will take a long time, only 60 min or under works well

2. run "candles_to_png.py" once the converted file has been generated
    - CSV file name is argument
    - '2544x1142.png' is an empty png file for the script to write to, must exist in order for script to run.

brute_download_whale_data
101-1000_scrape_address.ipynb - jupyter notebook to scrape top BTC whale addresses
brute_download_whale_data.py - downloads transaction data for scraped BTC addresses

converted_btc_data
converted minutely data is stored in this folder

btc_chart
generated .pngs are stored in this folder

