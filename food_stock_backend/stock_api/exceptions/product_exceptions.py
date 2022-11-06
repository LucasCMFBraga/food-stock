from typing import Final

class ProductException(Exception):
    pass

class ExceptionMessage:
    public_api_product_failed: Final = "Public product API failed"

class PublicProductApiFailed(ProductException):
    def __init__(self) -> None:
        super().__init__(ExceptionMessage.public_api_product_failed)