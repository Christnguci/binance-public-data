import zipfile

zip_file_path = '/Users/chris/Documents/Cloning/binance-public-data/python/data/spot/daily/trades/BTCUSDT/BTCUSDT-trades-2024-10-28.zip'

with zipfile.ZipFile(zip_file_path,'r')  as zip_ref:
    zip_ref.extractall('/Users/chris/Documents/Cloning/binance-public-data/python/data/spot/daily/trades/BTCUSDT')
    print(zip_ref.namelist())