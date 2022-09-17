import config, sys, time, ccxt




exchange = ccxt.ftx({
  'apiKey': config.API_KEY,
  'secret': config.SECRET_KEY,
  'headers': {
        'FTX-SUBACCOUNT': 'spot-perpetual',
    },
})

ticker = exchange.fetch_ticker(config.SYMBOL)
print(ticker)
buy_orders = []
sell_orders = []

# initial_buy_order = exchange.create_limit_buy_order(config.SYMBOL, config.POSITION_SIZE , 1500)
start = time.time()

for i in range(config.NUM_BUY_GRID_LINE):
  price = ticker['bid'] - (config.GRID_SIZE * (i+1))
  print("sumitted market limit buy order at {}".format(price))
  order = exchange.create_limit_buy_order(config.SYMBOL, config.POSITION_SIZE, price)
#   buy_orders.append(order)


# for i in range(config.NUM_SELL_GRID_LINE):
#   price = ticker['ask'] + (config.GRID_SIZE * (i+1))
#   print("sumitted market limit sell order at {}".format(price))
#   order = exchange.create_limit_sell_order(config.SYMBOL, config.POSITION_SIZE, price)
#   sell_orders.append(order)

setted_up_orders = time.time()

print("set_orders time is {}".format(setted_up_orders - start))


# while True:
#   while_loop_start = time.time()

#   close_order_ids = []

#   print("checking for buy orders")
#   for buy_order in buy_orders:
#     try:
#       order = exchange.fetch_order(buy_order['id'])
#     except Exception as e:
#       print("request failed, retrying/")
#       continue

#     order_info = order['info']

#     if order_info['status'] == config.CLOSED_ORDER_STATUS:
#       close_order_ids.append(order_info["id"])
#       print("buy order excuted at price {}".format(order_info['price']))
#       new_sell_price = float(order_info["price"]) + config.GRID_SIZE
#       new_sell_order = exchange.create_limit_sell_order(config.SYMBOL, config.POSITION_SIZE, new_sell_price)
#       print("creating new limit sell order at price {}".format(new_sell_price))
#       sell_orders.append(new_sell_order)

#   time.sleep(config.CHECK_ORDERS_FREQEUNCY)

#   for sell_order in sell_orders:
#     try:
#       order = exchange.fetch_order(sell_order['id'])
#     except Exception as e:
#       print("request failed, retrying/")
#       continue

#     order_info = order['info']

#     if order_info['status'] == config.CLOSED_ORDER_STATUS:
#       close_order_ids.append(order_info["id"])
#       print("sell order excuted at price {}".format(order_info['price']))
#       new_buy_price = float(order_info["price"]) - config.GRID_SIZE
#       new_buy_order = exchange.create_limit_buy_order(config.SYMBOL, config.POSITION_SIZE, new_buy_price)
#       print("creating new limit sell order at price {}".format(new_sell_price))
#       sell_orders.append(new_sell_order)

#     time.sleep(config.CHECK_ORDERS_FREQEUNCY)
    
#   for order_id in close_order_ids:
#     buy_orders = [ buy_order for buy_order in buy_orders if order_id != buy_order['id']]
#     sell_orders = [ sell_order for sell_order in sell_orders if order_id != sell_order['id']]
  
#   end_of_while_loop = time.time()
#   print("each loop time is {}".format(end_of_while_loop - while_loop_start))

