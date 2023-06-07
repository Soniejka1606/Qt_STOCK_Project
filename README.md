# Project "Inventory Management"
### Description
The "Inventory Management" project is a window application designed for efficient management of products and warehouses. The application provides a set of functionalities that allow users to add products, place orders, perform product relocations between warehouses, dispose of products, and add new warehouses.

## Key Features
### Add Product
Upon clicking the "Добавить товар" button, the add_tovar.py window opens, allowing users to enter information about a new product, such as name, price, description, and other attributes. Users can also upload Word or Excel files containing product information, and the application automatically reads and adds this information to the table with additional required data.

### Place Order
By selecting the "Оформить покупку" button, the do_order.py window opens, enabling users to select products from a provided list and specify the quantity for purchase. Users can also upload Word or Excel files containing purchase information, such as a list of products and quantities, which the application automatically reads and adds to the table with additional required data. This functionality also allows users to register new customers or delete existing ones from the database.

### Product Relocation
Clicking the "Перемещение" button opens the relocation.py window, where users can choose products for relocation and specify the target warehouse. Users can also upload Word or Excel files containing information about the product relocation, and the application automatically reads and adds this information to the table with additional required data.

### Confirm Relocation
When selecting the "Подтвердить перемещение" button, the accept_relocation.py window opens, displaying a list of pending relocation requests. Users can review the details of each relocation, and the application automatically reads the associated Word or Excel file, adding the information to the table with additional required data.

### Product Disposal
Upon clicking the "Списать" button, the spisanie.py window opens, allowing users to select products for disposal and provide a reason for the disposal. Users can also upload Word or Excel files containing information about product disposal, and the application automatically reads and adds this information to the table with additional required data.

## Used Libraries
The following libraries are used in this project:
- os
- sqlite3
- docxtpl
- datetime
- docx
- subprocess
- openpyxl
- functools
- PyQt5

## Note
When placing orders, relocating products, or disposing of products, the application automatically generates Word and Excel documents containing the relevant information. The document generation is based on user-entered data stored in the database.
