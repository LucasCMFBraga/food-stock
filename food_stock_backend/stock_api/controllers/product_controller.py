from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.http import JsonResponse, HttpResponse

from stock_api.serializers.product_serializer import ProductSerializer
from stock_api.db_models.product import Product


class ProductController(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects
    lookup_field = "bar_code"

    def get(self, request, bar_code: str = ""):
        try:
            if bar_code:
                products = self.__get_list_product()
            else:
                products = self.get_queryset()
                products = products.all()

            fields_serialized = self.get_serializer(products, many=True)

            return JsonResponse(fields_serialized.data, status=status.HTTP_200_OK, safe=False)

        except queryset.model.DoesNotExist as error:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, bar_code: str):
        products = self.__get_list_product()

        if products:
            fields_serialized = self.get_serializer(data=request.data, partial=True)
            if fields_serialized.is_valid():
                fields_serialized.update(products[0], fields_serialized.validated_data)

                products = self.__get_list_product()
                fields_serialized = self.get_serializer(products, many=True)

                return JsonResponse(fields_serialized.data, status=status.HTTP_200_OK, safe=False)

            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, bar_code: str):
        product = self.__get_list_product()
        product.delete()

        return HttpResponse(status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = self.get_serializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)

        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def __get_list_product(self):
        """
        Returns the object list the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.get_queryset()

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        # # May raise a permission denied
        # self.check_object_permissions(self.request, obj)
        return queryset.filter(**filter_kwargs)

    def __get_error_response(error):
        return {"MESSAGE": str(error)}