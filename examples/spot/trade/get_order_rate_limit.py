#!/usr/bin/env python

import logging
from binance.lib.utils import config_logging
from binance.spot import Spot as Client

config_logging(logging, logging.DEBUG)

key = "HUni4emxCgKGapEmyVUNn4dwQOvmcxT2dJhVBDB4QRfXeqZfjJArNNvJotVooq2t"
secret = "EkjSgtZbVZ3pg3h5rpKMg7WQguAkX6Qq2Vqc2nLne7yoizCUtoaNTXtK14diiYOg"

client = Client(key=key, secret=secret, base_url="https://testnet.binance.vision")
logger = logging.getLogger(__name__)

logger.info(client.get_order_rate_limit())
