#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = "HUni4emxCgKGapEmyVUNn4dwQOvmcxT2dJhVBDB4QRfXeqZfjJArNNvJotVooq2t"
secret = "EkjSgtZbVZ3pg3h5rpKMg7WQguAkX6Qq2Vqc2nLne7yoizCUtoaNTXtK14diiYOg"

client = Client(key, secret, base_url="https://testnet.binance.vision")
logging.info(client.account(recvWindow=6000))
