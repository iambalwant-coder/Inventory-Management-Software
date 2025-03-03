# Inventory Management System (Django)

This is a simple Django web application to manage products, orders, and categories. You can use it to add, view, and edit products, orders, and categories in your inventory.

## Features

- **Product List**: See all the products in your inventory.
- **Order List**: View all the orders placed in the system.
- **Add Product**: Add new products to the inventory.
- **Add Order**: Create new orders for products.
- **Add Category**: Add categories for your products.

## What You Need

- **Backend**: Django
- **Frontend**: HTML, CSS (using Bootstrap for styling)
- **Database**: SQLite (Django’s default)

## How to Set It Up

### Step 1: Clone the repository

Clone this repository to your computer using this command:

```bash
git clone https://github.com/your-username/inventory-management-system.git
```

### Step 2: Set up a virtual environment

Create and activate a virtual environment to manage your dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Create the database tables

Run this command to create the necessary tables for your app:

```bash
python manage.py migrate
```

### Step 5: Create a superuser (optional)

You can create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Step 6: Run the server

Start the server with this command:

```bash
python manage.py runserver
```

You can now open your browser and go to `http://127.0.0.1:8000/` to use the app.

## How to Use

- **Product List**: See all the products in the inventory.
- **Order List**: View all the orders.
- **Add Product**: Add a new product to the inventory.
- **Add Order**: Create an order for a product.
- **Add Category**: Add a new category for products.

## Project Structure

```
inventory_management_system/
│
├── inventory/                # App for managing products, orders, and categories
│   ├── models.py             # Defines how products, orders, and categories are stored
│   ├── views.py              # Handles how data is displayed
│   ├── forms.py              # Handles forms for adding/editing products, orders, and categories
│   ├── templates/            # Folder with HTML files for each page
│   └── migrations/           # Database migrations
│
├── inventory_management_system/  # Main project folder
│   ├── settings.py                # Django settings
│   ├── urls.py                    # URL mappings for the app
│   ├── wsgi.py                    # Web server configuration
│   └── asgi.py                    # Asynchronous server configuration
│
├── manage.py                    # Command-line script to manage the project
├── requirements.txt             # List of Python packages needed for the project
└── README.md                    # This file
```
