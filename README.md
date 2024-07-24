# VendingMachine

This is a Django-based backend project for managing a beverage vending machine.

## Features

- Display all available beverages
- Dispense beverages with specified ingredients
- Manage and update ingredient inventory
- Notify staff when inventory is low

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/VendingMachine.git
   cd VendingMachine
--------------------------------------------------------------------------------------------------------------------------------
   Step 2:
Create and activate a virtual environment:

bash
python -m venv venv
venv\Scripts\activate  # On Windows
-------------------------------------------------------------------------------------------------
Step 3:
Install dependencies:

bash

pip install -r requirements.txt
-------------------------------------------------------------------------------------------------------
step 4:

Run migrations and start the development server:

bash

python manage.py migrate
python manage.py runserver

Usage
For Acceess of Api: http://127.0.0.1:8000
for update the inventory use http://127.0.0.1:8000/api/ingredients/<inventory_id>/update_inventory/

Use the Django admin interface at http://127.0.0.1:8000/admin/ to manage ingredients and beverages
