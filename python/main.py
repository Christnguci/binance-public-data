import download_trade as dt 

dt.download_daily_trades("spot","BTCUSDT",1,"2024-10-18")

python3 download-trade.py -t spot -s ETHUSDT BTCUSDT BNBBUSD -y 2020 -m 02 12 -c 1
python3 download-trade.py -t spot -s BTCUSDT -skip-monthly 1 -startDate 2021-01-01 -endDate 2021-02-02