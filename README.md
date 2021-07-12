# ADM Shop

An Ecommerce built in Django
**WORKING IN PROGRESS**

**FEATURES**
- Product added to cart are inserted into the DB if the user is logged; otherwise, a cookie will be created containing all the products in the cart.
- The payment is managed by stripe (you need to retrieve stripe keys).

To work correctly, it needs a .env file inside the folder adm including:
```
SECRET_KEY=your secret key
DEBUG=True (True/False)
DATABASE_NAME=db name
DATABASE_USER=db user name
DATABASE_PASS=db user password
DATABASE_HOST=db host
```

