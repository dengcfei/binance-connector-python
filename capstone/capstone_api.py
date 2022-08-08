import unittest
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError


class MyTestCase(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given module."""
        config_logging(logging, logging.DEBUG)

        key = "HUni4emxCgKGapEmyVUNn4dwQOvmcxT2dJhVBDB4QRfXeqZfjJArNNvJotVooq2t"
        secret = "EkjSgtZbVZ3pg3h5rpKMg7WQguAkX6Qq2Vqc2nLne7yoizCUtoaNTXtK14diiYOg"
        binance_url = "https://testnet.binance.vision"
        local_url  = "http://127.0.0.1"
        cls.client = Client(key, secret, base_url=local_url)

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a setup_module
        method.
        """
        pass

    def test_new_order(self):
        symbol = "BTCUSDT"
        price = 9500
        quantity = 0.002
        status = "FILLED"

        params = {
            "symbol": symbol,
            "side": "SELL",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price,
        }

        response = self.client.new_order(**params)
        self.assertEqual(response['symbol'], symbol)  # add assertion here
        self.assertEqual('{:.8f}'.format(price), response['price'])  # add assertion here
        self.assertEqual('{:.8f}'.format(quantity), response['origQty'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
