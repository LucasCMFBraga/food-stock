import requests
import environ
from os import path

from stock_api.thrid_api.produts_api_interface import ProductApiInterface, ProductEntityApi
from stock_api.exceptions.product_exceptions import PublicProductApiFailed
from stock_api.constants import API_URL
from stock_api.constants import FOOD_STOCK

# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(path.join(FOOD_STOCK,'.env'))

RETURN_DATA = 'return'
NAME = 'nome'
BAR_CODE = 'ean'
NET_WEIGHT = 'peso_liquido'

class ProductApi(ProductApiInterface):
    def get_product_by_barcode(self, bar_code: str) -> ProductEntityApi:
        try:
            response = requests.get(API_URL.format(barcode=bar_code, token=env('TOKEN')))
            response = response.json()
            data = response[RETURN_DATA]
            
            product = ProductEntityApi(
                data[NAME],
                data[BAR_CODE],
                data[NET_WEIGHT])
            return product

        except:
            raise PublicProductApiFailed()
