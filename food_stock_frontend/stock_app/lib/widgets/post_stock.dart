import 'package:flutter/material.dart';

import 'package:stock_app/service/product_service.dart';
import 'package:stock_app/models/product_model.dart';

// Create a Form widget.
class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  MyCustomFormState createState() {
    return MyCustomFormState();
  }
}

// Create a corresponding State class.
// This class holds data related to the form.
class MyCustomFormState extends State<MyCustomForm> {
  // Create a global key that uniquely identifies the Form widget
  // and allows validation of the form.
  //
  // Note: This is a GlobalKey<FormState>,
  // not a GlobalKey<MyCustomFormState>.
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    // Build a Form widget using the _formKey created above.
    String? bar_code;
    DateTime expiration_data = DateTime.now(); 

    return Form(
      key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextFormField(
            onSaved: (value){bar_code=value.toString();},
            // The validator receives the text that the user has entered.
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter some text';
              }
              return null;
            },
          ),
          TextFormField(
            // onSaved: (value){expiration_data=DateTime.parse(value.toString());},
            // The validator receives the text that the user has entered.
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 16.0),
            child: ElevatedButton(
              onPressed: () {
                // Validate returns true if the form is valid, or false otherwise.
                if (_formKey.currentState!.validate()) {
                  // If the form is valid, display a snackbar. In the real world,
                  // you'd often call a server or save the information in a database.
                  _formKey.currentState?.save();
                  DateTime now = new DateTime.now();
                  DateTime date = new DateTime(now.year, now.month, now.day);
                  Product current_product = Product(
                    bar_code: bar_code,
                    expiration_date: date);
                    postProduct(current_product).then((value){
                      Text message = value==true ? Text('Salvo com sucesso'): Text('Código de barras inválido');
                      ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: message),
                  );});

                  
                  _formKey.currentState!.reset();
                }
              },
              child: const Text('Submit'),
            ),
          ),
        ],
      ),
    );
  }
}

class AddProduct extends StatelessWidget{

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: MyCustomForm()
    );
  }
}