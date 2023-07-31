import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'package:stock_app/widgets/nav_drawer.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Estoque',
        theme: ThemeData(
          primarySwatch: Colors.amber,
        ),
        home: Scaffold(
            drawer: NavDrawer(),
            appBar: AppBar(
              centerTitle: true,
              title: const Text(''),
            ),
            body: Center(
                child: Column(
              children: [
                Padding(
                    padding: const EdgeInsets.all(0.0),
                    child:
                        const Text('Promoções dos mercados próximos a você')),
              ],
            ))));
  }
}
