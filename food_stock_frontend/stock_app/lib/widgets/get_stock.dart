import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:stock_app/widgets/nav_drawer.dart';

import 'package:stock_app/models/product_model.dart';
import 'package:stock_app/service/product_service.dart';


// FutureBuilder<List<Product>>(
//                         future: product_service.getProducts(),
//                         builder: ((context, snapshot){
//                           return Text('${snapshot.data?.name}');
//                         }),)

class ShowStock extends StatefulWidget {
  @override
  _MyHomeState createState() => _MyHomeState();
}

class _MyHomeState extends State<ShowStock> {
  late ScrollController controller;
  int current_page = 1;
  List<Product> products = List<Product>.empty();

  List<SizedBox> items = List.generate(1, (index) =>  
  SizedBox(
    width: 200.0,
    height: 100.0,
    child: Card(child: Text('$index'))));

  @override
  void initState() {
    super.initState();
    controller = ScrollController()..addListener(_scrollListener);

    getProducts(current_page).then((value){
      this.products = value;
      for(Product p in products){
          print(p.name);
      }
      setState((){});
      });    
  }

  @override
  void dispose() {
    controller.removeListener(_scrollListener);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // getProducts().then(
    //   (value) => null)

    return Scaffold(
      body: Scrollbar(
        child: ListView.builder(
          controller: controller,
          itemBuilder: (context, index) {
            return SizedBox(
                    width: 200.0,
                    height: 100.0,
                    child: Card(
                      child:Center(
                        child: Text(products[index].name.toString())
                    )));
          },
          itemCount: products.length,
        ),
      ),
    );
  }

  void _scrollListener() {
    print(controller.position.extentAfter);
    if (controller.position.extentAfter < 500) {
        current_page++;
        getProducts(current_page).then((value){
          products.addAll(value);
          setState((){});
      });  

      // setState(() {
      //   items.addAll(List.generate(42, (index) =>   
      //   SizedBox(
      //     width: 200.0,
      //     height: 100.0,
      //     child: Card(child: Text('$index')))));
      // });
    }
  }
}


class Stock extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: ShowStock()
    );
  }
}