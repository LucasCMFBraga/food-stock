import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:stock_app/models/product_model.dart';
import 'package:stock_app/utils/constants.dart';

Future<List<Product>> getProducts(int page) async {        
  http.Response returnedResult =  await http.get(
    Uri.parse('${API}${PRODUCT}?page=${page}'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset-UTF-8',
      'Authorization': TOKEN
      });

  return fromJson(returnedResult.body);
}

Future<bool> postProduct(Product product) async{
  http.Response returnedResult = await http.post(
    Uri.parse('${API}${PRODUCT}'),
    headers: <String, String>{
      'Content-Type': 'application/json',
      'Authorization': TOKEN
      },
    body: toJson(product));
    
    return  returnedResult.statusCode == 201;
}