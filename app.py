import requests as rq
from noti import send

COIN_TICKERS = ['KRW-BTC', 'KRW-ETH']
msg = ''

for coin in COIN_TICKERS:
  BASE_URL = "https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.%s&count=0"%(coin)

  res = rq.get(BASE_URL)
  data = res.json()[0]

  exchange='업비트'
  code = coin
  openingPrice = "{:,}".format(data['openingPrice'])
  highPrice = "{:,}".format(data['highPrice'])
  lowPrice = "{:,}".format(data['lowPrice'])
  tradePrice = "{:,}".format(data['tradePrice'])
  candleAccTradeVolume = "{:,}".format(data['candleAccTradeVolume'])
  candleAccTradePrice = "{:,}".format(data['candleAccTradePrice'])

  msg += '''
거래소: %s,
코드: %s,
시작가: %s,
고가: %s,
저가: %s,
채결가: %s,
채결량(1Day): %s, 
채결금액(1Day): %s

  '''%(exchange, code, openingPrice, highPrice, lowPrice, tradePrice, candleAccTradeVolume, candleAccTradePrice)

send(msg)
# print(msg)