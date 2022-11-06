from abc import abstractclassmethod, ABC

from stock_api.entities.product_entity_api import ProductEntityApi

class ProductApiInterface(ABC):
    @abstractclassmethod
    def get_product_by_barcode(bar_code: str) -> ProductEntityApi:
        pass