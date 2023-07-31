from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.request import Request
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse

from stock_api.exceptions.product_exceptions import PublicProductApiFailed
from stock_api.serializers.product_serializer import ProductSerializer
from stock_api.thrid_api.product_api import ProductApi
from stock_api.db_models.product import Product

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductController(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects
    lookup_field = "bar_code"
    pagination_class = StandardResultsSetPagination
    product_api = ProductApi()

    def get(self, request: Request, bar_code: str = ""):
        try:
            user = User.objects.get(username=request.user)

            if bar_code:
                products = self.__get_list_product(user.pk)
            else:
                products = self.get_queryset()
                products = products.filter(user_id=user.pk)
                products = self.paginate_queryset(queryset=products)

            fields_serialized = self.get_serializer(products, many=True)
            return JsonResponse(fields_serialized.data, status=status.HTTP_200_OK, safe=False)
        
        except self.queryset.model.DoesNotExist as error:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, bar_code: str):
        user = User.objects.get(username=request.user)
        products = self.__get_list_product(user.pk)

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

    def delete(self, request: Request, bar_code: str):
        user = User.objects.get(username=request.user)
        product = self.__get_list_product(user.pk)
        product.delete()

        return HttpResponse(status=status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            response = self.product_api.get_product_by_barcode(
                    request.data['bar_code'])
            
            request.data.update({
                'name':response.name,
                'net_weight':response.net_weight    
            })

            user = User.objects.get(username=request.user)
            request.data.update({"user": user.pk})
            
            product_serializer = self.get_serializer(data=request.data)
            if not product_serializer.is_valid():
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            product_serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)

        except PublicProductApiFailed:
            return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def __get_list_product(self, user_id):
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

        filter_kwargs = {
            self.lookup_field: self.kwargs[lookup_url_kwarg],
            "user_id": user_id
            }
        # # May raise a permission denied
        # self.check_object_permissions(self.request, obj)
        return queryset.filter(**filter_kwargs)

    def __get_error_response(error):
        return {"MESSAGE": str(error)}