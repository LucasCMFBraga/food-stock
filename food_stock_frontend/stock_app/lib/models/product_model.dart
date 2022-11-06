import 'dart:convert';

List<Product>  fromJson(String product){
  List<Product> prod =  List<Product>.empty(growable: true);
  final jsonData = json.decode(product);
  if(jsonData is Map){
    return [];
  }
  
  for(Map<String, dynamic> product in jsonData){
      prod.add(Product.fromJson(product));
  }
  return prod;
}

String toJson(Product product){
  print(product.toJson());
  return json.encode(product.toJson());
}

class Product{
  String? bar_code;
  DateTime? expiration_date;
  String? name;
  String? net_weight;

  Product({
    required this.bar_code,
    required this.expiration_date,
    this.name,
    this.net_weight});

  factory Product.fromJson(Map<String, dynamic> product){
    return Product(
      name: product['name'],
      bar_code: product['bar_code'],
      net_weight: product['net_weight'],
      expiration_date: DateTime.parse(product['expiration_date'])
      );
  }

  Map<String, dynamic> toJson(){
    return {
      "bar_code": this.bar_code,
      "expiration_date": '${this.expiration_date!.year}-${this.expiration_date!.month}-${this.expiration_date!.day}'
    };
  }
  
} 