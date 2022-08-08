
#import logging
from binance.spot import Spot as Client
#from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient
import queue

#config_logging(logging, logging.DEBUG)

clent_test = Client(base_url="https://testnet.binance.vision")
clent_prod = Client()

client_ws = WebsocketClient()
client_ws.start()

#queue book update
book_updates = queue.Queue()
def message_handler(message):
    if 'result' in message.keys():
        pass
    else:
        book_updates.put(message)
    #print(message)

client_ws.diff_book_depth(
    symbol="btcusdt",
    speed=1000,
    id=1,
    callback=message_handler,
)
import time
time.sleep(1)

book_snapshot = clent_prod.depth("BTCUSDT", limit=10)
last_update_id = book_snapshot['lastUpdateId']

while True:
    book_update = book_updates.get()
    if book_update['u'] <= last_update_id:
        print("skip ", book_update['U'])
    elif book_update['U'] <= last_update_id + 1 <= book_update['u']:
        bid_update = book_update['b']
        ask_update = book_update['a']
        book_snapshot['bids'] = list(map(lambda level:  bid_update if level[0] == bid_update[0] else level, book_snapshot['bids']))
        book_snapshot['asks'] = list(map(lambda level:  ask_update if level[0] == ask_update[0] else level, book_snapshot['asks']))
        last_update_id = book_update['u']
        print(last_update_id)
    else:
        print("error " , book_update['U'], book_update['u'], last_update_id)
        book_snapshot = clent_prod.depth("BTCUSDT", limit=10)
        last_update_id = book_snapshot['lastUpdateId']


#pass


