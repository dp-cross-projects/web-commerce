# Overview

This is "Computer Commerce" project. The main objective is to improve my Python skills by learning and programming a web app using the Django framework.
The site includes 3 apps or modules: Home, Profile and CheckOut. The content display dinamically with user interactions. The user can register, login, add to cart, remove from cart and purchase. Also, can add user information and check his purchase history. The system already includes a database with data to interact with.

To start the server:

`python manage.py runserver 3000`

To access the website:

_localhost:3000/_

To access the Django Admin Panel:

_localhost:3000/admin_

Credentials for Django Admin Panel:
```
Username: admin
Password: admin
```

[Software Demo Video](https://www.youtube.com/watch?v=d6pb6od1G7w)

# Web Pages
The site has a navbar where the user can navigate through the site.

- Home
    - The Home provides a view of products with price, discount, tax and stock. When the user is logged, he can add an item from the cart when stock is available.
    - Route: _/_
    - Always enabled
- Profile
    - The user profile page provides the user information, a form to update data and the purchase history. When the user updates his information, the data is applied inmediately. 
    - Route: _/user_
    - After user logged enabled

- Cart
    - When the user add an item to the cart, it is displayed on this page. The user can know how much items added, the total price and a form to complete the purchase. When the purchase is finished, it is shown in the Profile page.
    - Route: _/checkout_
    - After user logged enabled

- Login
    - This page provides a form for the user to login using his credentials.
    - Route: _/login_
    - Enabled when user is not logged

- Register
    - This page provides a form for the user to register a use their credentials for login.
    - Route: _/register_
    - Enabled when user is not logged



# Development Environment

- Language: Python
- Framework: Django
- Templates: HTML
- Styles: Bootstrap
- Database: SQLite


# Useful Websites

* [Django documentation](https://docs.djangoproject.com/en/6.0/)
* [Jinja documentation](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

# Future Work

* Protect Routes: The routes are not enabled in the navbar, but the user can access by writting on the browser.
* Managing Inventory: The user can interact and buy, but the admin needs to use the Django admin panel to add products.
* Styles Improve: The overall site has some styles added, but it requires visual improvement.