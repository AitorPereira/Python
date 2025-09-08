# Inventory Management
# Build a function called manage_inventory that handles multiple actions related to product inventory, using a dictionary as output.

# Specifications:

# The manage_inventory function will receive three parameters:

#   inventory: a list of dictionaries, where each dictionary represents a product in the inventory.

#   action: a string indicating the action to perform ('add', 'update', 'search', or 'list').

#   kwargs: Additional keyword arguments used to pass specific information for each action,
#           such as product name, quantity, or sorting order.

# The function will return a dictionary with a key 'result' containing the specific output of each action,
# or an error message in case the action is invalid or if any execution issues occur.

# Product format in the inventory: each product will be a dictionary with the keys
# name, category, and quantity.

# Instructions for each action:

# 1. Add a new product:
#    - If the product already exists (same name), return { 'result': 'Error: Product already exists' }.
#    - If it doesn’t exist, add it to the inventory list and return { 'result': 'Product successfully added' }.

# 2. Update the quantity of an existing product:
#    - Search for the product in the inventory by its name.
#    - If found, add the provided quantity to its current quantity and return { 'result': 'Quantity successfully updated' }.
#    - If the product is not found, return { 'result': 'Error: Product not found' }.

# 3. Search for products by category:
#    - Filter the products that belong to the specified category and return them in a list under the 'result' key:
#      { 'result': [{'name': 'Product1', 'quantity': x}, ...] }.
#    - If no products are found in the category, return { 'result': 'No products found in this category' }.

# 4. List products sorted by stock quantity:
#    - Sort the products in the inventory in ascending or descending order
#      according to the 'order' parameter ('ascending' or 'descending').
#    - Return the sorted product list under the 'result' key in the output dictionary.


def manage_inventory(inventory, action, **kwargs):
    if action == "register":
        for product in inventory:
            if product['name'] == kwargs['name']:
                return {'result': 'Error: Product already exists'}
        
        new_product = {
            'name': kwargs['name'],
            'category': kwargs['category'],
            'quantity': kwargs['quantity']
        }
        
        inventory.append(new_product)
        return {'result': 'Product successfully registered'}
    
    elif action == "update":
        for product in inventory:
            if product['name'] == kwargs['name']:
                product['quantity'] = product['quantity'] + kwargs['quantity']
                return {'result': 'Quantity successfully updated'}
        return {'result': 'Error: Product not found'}
    
    elif action == "search":
        found_list = []
        for product in inventory:
            if product['category'] == kwargs['category']:
                found_list.append({
                    'name': product['name'],
                    'quantity': product['quantity'],
                    'category': product['category']
                })
        
        if found_list:
            return {'result': found_list}
        else:
            return {'result': 'No products found in this category'}
    
    elif action == "list":
        order = kwargs.get('order', 'ascending')
        if order == 'descending':
            reverse = True
        else:
            reverse = False
        
        sorted_inventory = sorted(inventory, key=lambda p: p['quantity'], reverse=reverse)
        return {'result': sorted_inventory}
    
    else:
        return {'result': 'Error: Unrecognized action'}


#Test to register a product
inventory = []

result = manage_inventory(
    inventory,
    action="register",
    name="Laptop",
    category="Electronics",
    quantity=10
)

print(result)
# Output: {'result': 'Product successfully registered'}


#Test to register the same product again

result = manage_inventory(
    inventory,
    action="register",
    name="Laptop",
    category="Electronics",
    quantity=10
)

print(result)
# Output: {'result': 'Error: Product already exists'}

# Add more products for better search
manage_inventory(inventory, "register", name="Laptop", category="Electronics", quantity=10)
manage_inventory(inventory, "register", name="Smartphone", category="Electronics", quantity=20)
manage_inventory(inventory, "register", name="Book", category="Books", quantity=15)

result = manage_inventory(
    inventory,
    action="search",
    category="Electronics"
)

print(result)
# Output: {'result': [{'name': 'Laptop', 'quantity': 15, 'category': 'Electronics'}, {'name': 'Smartphone', 'quantity': 20, 'category': 'Electronics'}]}


#Search for an empty category
result = manage_inventory(
    inventory,
    action="search",
    category="Toys"
)

print(result)
# Output: {'result': 'No products found in this category'}


#List Inventory Example Ascending (default)
result = manage_inventory(
    inventory,
    action="list"
)

print(result)
# Output: {'result': [{'name': 'Book', ...}, {'name': 'Laptop', ...}, {'name': 'Smartphone', ...}]}


#List Inventory Example Descending
result = manage_inventory(
    inventory,
    action="list",
    order="descending"
)

print(result)
# Output: {'result': [{'name': 'Smartphone', ...}, {'name': 'Laptop', ...}, {'name': 'Book', ...}]}


#Unrecognized Action
result = manage_inventory(inventory, action="delete", name="Laptop")

print(result)
# Output: {'result': 'Error: Unrecognized action'}






