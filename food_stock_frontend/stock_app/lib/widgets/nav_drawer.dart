import 'package:flutter/material.dart';
import 'package:stock_app/widgets/get_stock.dart';
import 'package:stock_app/widgets/post_stock.dart';

class NavDrawer extends StatelessWidget{
  
  @override
  Widget build(BuildContext context){
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          DrawerHeader(
            child: Text(
              'Menu',
              style: TextStyle(color: Colors.white, fontSize: 25),
          ),
            decoration: BoxDecoration(
              color: Colors.green,
              image: DecorationImage(
                fit: BoxFit.fill,
                image: NetworkImage('https://img.freepik.com/vetores-gratis/despensa-plana-com-alimentos-diversos_23-2148722383.jpg?w=1060&t=st=1667772870~exp=1667773470~hmac=6a664c98e186e60cea86aebbde2af4154a02568166588805b13ad93a36503f42')
              )
            ),
          ),
          ListTile(
            leading: Icon(Icons.list),
            title: Text('Estoque'),
            onTap: () => {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => Stock()))
            },
          ),
            ListTile(
            leading: Icon(Icons.ad_units),
            title: Text('Addicionar produto'),
            onTap: () => {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AddProduct()))
            },
          ),
          ListTile(
            leading: Icon(Icons.settings),
            title: Text('Settings'),
            onTap: () => {Navigator.of(context).pop()},
          ),
          ListTile(
            leading: Icon(Icons.border_color),
            title: Text('Feedback'),
            onTap: () => {Navigator.of(context).pop()},
          ),
          ListTile(
            leading: Icon(Icons.exit_to_app),
            title: Text('Logout'),
            onTap: () => {Navigator.of(context).pop()},
          ),
        ],
      ),
    );
  }

}