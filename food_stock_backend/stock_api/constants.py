from os import path

# Paths
CURRENT_PATH = path.dirname(path.dirname(path.abspath(__file__)))
ROOT_PATH = path.join(CURRENT_PATH, '..')
FOOD_STOCK = path.join(ROOT_PATH, 'food_stock')

#URLs
API_URL = "http://brasilapi.simplescontrole.com.br/mercadoria/consulta/?ean={barcode}&access-token={token}&_format=json"
