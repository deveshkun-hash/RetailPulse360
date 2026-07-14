from generate_stores import run as stores
from generate_products import run as products
from generate_customers import run as customers
from generate_orders import run as orders
from generate_order_items import run as items

if __name__=='__main__':
    stores()
    products()
    customers()
    orders()
    items()
    print("All CSV files generated successfully.")
