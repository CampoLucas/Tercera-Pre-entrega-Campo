# Coder House Third Project - Python
<strong>
Student: Lucas Campo</br>
Commission: 48405</br>
</strong>

## Description
This is a simple web page for managing orders, products, and stores. The following features are available:</br>

## Features
- Add new orders.
- See orders.
- Add new products.
- See products.
- Add new stores.
- See stores.
- Search products.

## Dependencies
To run this project, you'll need Python 3.x and Django 3.x.

## How to run the page
Do these steps in terminal</br></br>
<strong>1. Clone the repository:</strong>
```
git clone https://github.com/CampoLucas/Tercera-Pre-entrega-Campo.git
```
<strong>2. Run migrations</strong>
```
python manage.py migrate
```
<strong>3. Start the server</strong>
```
python manage.py runserver
```
<strong>4. Once the server is running, in the browser visit the website</strong>
```
http://localhost:8000
```

## Testing
These features can be tested:
- Add a product.
- List of all products.
- Add an order.
- List of all orders.
- Add a store.
- List of all stores.
- Search for products by name.

## Code Structure
The code is organized as follows:
- <strong>admin.py</strong> – Django admin site configuration.
- <strong>forms.py:</strong> – Django forms for adding models.
- <strong>models.py:</strong> Django models for orders, products, and stores.
- <strong>views.py:</strong> – Django views for handling HTTP requests and responses.
- <strong>urls.py:</strong> Django url routing to map urls to views

## The URLs:
- <strong>Homepage:</strong> localhost:8000/
- <strong>List of all products:</strong> localhost:8000/products/
- <strong>Add a product:</strong> localhost:8000/products/add/
- <strong>List of all orders:</strong> localhost:8000/orders/
- <strong>Add an order:</strong> localhost:8000/orders/add/
- <strong>List of all stores:</strong> localhost:8000/stores/
- <strong>Add a store:</strong> localhost:8000/stores/add/
- <strong>Search for a product by name:</strong> localhost:8000/products/search/

## Used Technology
- Front-End:
    - CSS
    - Bootstrap
    - HTML5
- Back-End:
    - Python
    - Django

