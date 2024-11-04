#!/usr/bin/env python

"""
  script to download trades.
  set the absoluate path destination folder for STORE_DIRECTORY, and run

  e.g. STORE_DIRECTORY=/data/ ./download-trade.py

"""

import sys
from datetime import *
import pandas as pd
from enums import *
from utility import download_file, get_all_symbols, get_parser, get_start_end_date_objects, convert_to_date_object, \
  get_path


def download_monthly_trades(trading_type, symbols, num_symbols, years, months, start_date, end_date, folder, checksum):
  current = 0
  date_range = None

  if start_date and end_date:
    date_range = start_date + " " + end_date

  if not start_date:
    start_date = START_DATE
  else:
    start_date = convert_to_date_object(start_date)

  if not end_date:
    end_date = END_DATE
  else:
    end_date = convert_to_date_object(end_date)

  print("Found {} symbols".format(num_symbols))

  for symbol in symbols:
    print("[{}/{}] - start download monthly {} trades ".format(current+1, num_symbols, symbol))
    for year in years:
      for month in months:
        current_date = convert_to_date_object('{}-{}-01'.format(year, month))
        if current_date >= start_date and current_date <= end_date:
          path = get_path(trading_type, "trades", "monthly", symbol)
          file_name = "{}-trades-{}-{}.zip".format(symbol.upper(), year, '{:02d}'.format(month))
          download_file(path, file_name, date_range, folder)

          if checksum == 1:
            checksum_path = get_path(trading_type, "trades", "monthly", symbol)
            checksum_file_name = "{}-trades-{}-{}.zip.CHECKSUM".format(symbol.upper(), year, '{:02d}'.format(month))
            download_file(checksum_path, checksum_file_name, date_range, folder)
    
    current += 1

def download_daily_trades(trading_type, symbols, num_symbols, dates, start_date, end_date, folder, checksum):
  current = 0
  date_range = None

  if start_date and end_date:
    date_range = start_date + " " + end_date

  if not start_date:
    start_date = START_DATE
  else:
    start_date = convert_to_date_object(start_date)

  if not end_date:
    end_date = END_DATE
  else:
    end_date = convert_to_date_object(end_date)
    
  print("Found {} symbols".format(num_symbols))

  for symbol in symbols:
    print("[{}/{}] - start download daily {} trades ".format(current+1, num_symbols, symbol))
    for date in dates:
      current_date = convert_to_date_object(date)
      if current_date >= start_date and current_date <= end_date:
        path = get_path(trading_type, "trades", "daily", symbol)
        file_name = "{}-trades-{}.zip".format(symbol.upper(), date)
        download_file(path, file_name, date_range, folder)

        if checksum == 1:
          checksum_path = get_path(trading_type, "trades", "daily", symbol)
          checksum_file_name = "{}-trades-{}.zip.CHECKSUM".format(symbol.upper(), date)
          download_file(checksum_path, checksum_file_name, date_range, folder)

    current += 1

# if __name__ == "__main__":
#     parser = get_parser('trades')
#     args = parser.parse_args(sys.argv[1:])
#     print(args)

#     if not args.symbols:
#       print("fetching all symbols from exchange")
#       symbols = get_all_symbols(args.type)
#       num_symbols = len(symbols)
#     else:
#       symbols = args.symbols
#       num_symbols = len(symbols)
#       print("fetching {} symbols from exchange".format(num_symbols))

#     if args.dates:
#       dates = args.dates
#     else:
#       period = convert_to_date_object(datetime.today().strftime('%Y-%m-%d')) - convert_to_date_object(
#         PERIOD_START_DATE)
#       dates = pd.date_range(end=datetime.today(), periods=period.days + 1).to_pydatetime().tolist()
#       dates = [date.strftime("%Y-%m-%d") for date in dates]
#       if args.skip_monthly == 0:
#         download_monthly_trades(args.type, symbols, num_symbols, args.years, args.months, args.startDate, args.endDate, args.folder, args.checksum)
#     if args.skip_daily == 0:
#       #download_daily_trades("spot",['BTCUSDT'],1,'2024-10-27'],None,None,None, None,0)
#       download_daily_trades(args.type, symbols, num_symbols, dates, args.startDate, args.endDate, args.folder, args.checksum)


# New code  
def main():
    trading_type = "spot"
    symbols = [input("Symbols: ")]
    dates = [input("Dates: ")]
    startDate=None
    endDate = None
    folder = None
    checksum = 0
    skip_daily = 0  



    if not symbols:
      print("fetching all symbols from exchange")
      symbols = get_all_symbols(trading_type)
      num_symbols = len(symbols)
    else:
      num_symbols = len(symbols)
      print("fetching {} symbols from exchange".format(num_symbols))

    if not date:
      period = convert_to_date_object(datetime.today().strftime('%Y-%m-%d')) - convert_to_date_object(
        PERIOD_START_DATE)
      dates = pd.date_range(end=datetime.today(), periods=period.days + 1).to_pydatetime().tolist()
      dates = [date.strftime("%Y-%m-%d") for date in dates]
      if skip_monthly == 0:
        download_monthly_trades(trading_type, symbols, num_symbols, years, months, startDate, endDate, folder, checksum)
    if skip_daily == 0:
      #download_daily_trades("spot",['BTCUSDT'],1,'2024-10-27'],None,None,None, None,0)
      try:
        download_daily_trades(trading_type, symbols, num_symbols, dates, startDate, endDate, folder, checksum)
        import zipfile

        zip_file_path = '/Users/chris/Documents/Cloning/binance-public-data/python/data/spot/daily/trades/BTCUSDT/BTCUSDT-trades-2024-10-28.zip'

        with zipfile.ZipFile(zip_file_path,'r')  as zip_ref:
            zip_ref.extractall('/Users/chris/Documents/Cloning/binance-public-data/python/data/spot/daily/trades/BTCUSDT')
            print(zip_ref.namelist())
      except Exception as e:
        raise(e)

main()