# ADM Shop

An Ecommerce built in Django
WORKING IN PROGRESS

FEATURES
- Product added to cart are inserted to the DB if the user is logged; otherwise, a cookie will be created containing all the products in the cart.

To work, it needs a .env file including:
```
SECRET_KEY=your secret key
DEBUG=True (True/False)
DATABASE_NAME=db name
DATABASE_USER=db user name
DATABASE_PASS=db user password
DATABASE_HOST=db host
```
