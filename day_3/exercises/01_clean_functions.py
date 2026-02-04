"""
Clean Functions Exercises - Day 3

Practice writing clean, focused functions that follow the Single Responsibility
Principle, have few parameters, and maintain consistent abstraction levels.

Your tasks:
1. Refactor functions that do too many things
2. Reduce the number of parameters using dataclasses
3. Separate mixed abstraction levels

Run the tests with: pytest tests/test_01_clean_functions.py
"""

from dataclasses import dataclass


# Exercise 1: Refactor function with multiple responsibilities
# TODO: Split this function into smaller, focused functions
def process_customer_order(order_data):
    """
    Process a customer order - validates, calculates, saves, and notifies.
    
    TODO: Add proper type hints and docstring
    TODO: Split into separate functions for each responsibility
    """
    # Validate order
    if not order_data.get('customer_id'):
        raise ValueError('Customer ID required')
    if not order_data.get('items'):
        raise ValueError('Order must have items')
    
    # Calculate total
    total = 0
    for item in order_data['items']:
        price = item['price']
        quantity = item['quantity']
        discount = item.get('discount', 0)
        total += price * quantity * (1 - discount)
    
    # Apply tax
    tax_rate = 0.08
    total_with_tax = total * (1 + tax_rate)
    
    # Save to database
    # db.save_order(order_data, total_with_tax)
    
    # Send notification
    # email.send(order_data['customer_id'], f"Order total: ${total_with_tax}")
    
    return total_with_tax


# TODO: Create these helper functions:
# - validate_order_data(order_data: dict) -> None
# - calculate_items_subtotal(items: list) -> float
# - apply_tax(amount: float, tax_rate: float) -> float
# - save_order_to_database(order_data: dict, total: float) -> None
# - send_order_notification(customer_id: str, total: float) -> None
# - process_customer_order_refactored(order_data: dict) -> float


# Exercise 2: Reduce parameters using dataclasses
# TODO: Create dataclasses to group related parameters
def create_product(name, description, price, currency, category, 
                   brand, sku, weight, dimensions_length, 
                   dimensions_width, dimensions_height):
    """
    Create a new product with all details.
    
    TODO: Replace multiple parameters with dataclasses
    TODO: Add proper type hints
    """
    return {
        'name': name,
        'description': description,
        'price': price,
        'currency': currency,
        'category': category,
        'brand': brand,
        'sku': sku,
        'weight': weight,
        'dimensions': {
            'length': dimensions_length,
            'width': dimensions_width,
            'height': dimensions_height
        }
    }


# TODO: Create these dataclasses:
# @dataclass
# class ProductInfo:
#     name: str
#     description: str
#     category: str
#     brand: str
#     sku: str

# @dataclass
# class PriceInfo:
#     amount: float
#     currency: str

# @dataclass
# class Dimensions:
#     length: float
#     width: float
#     height: float

# @dataclass
# class ShippingInfo:
#     weight: float
#     dimensions: Dimensions

# TODO: Create refactored function:
# def create_product_refactored(product_info: ProductInfo, 
#                               price_info: PriceInfo,
#                               shipping_info: ShippingInfo) -> dict


# Exercise 3: Separate abstraction levels
# TODO: Extract low-level details into separate functions
def generate_sales_report(sales_data):
    """
    Generate a comprehensive sales report.
    
    TODO: Separate high-level and low-level operations
    TODO: Add proper type hints
    """
    # Filter valid sales
    valid_sales = []
    for sale in sales_data:
        if sale.get('status') == 'completed' and sale.get('amount', 0) > 0:
            valid_sales.append(sale)
    
    # Calculate metrics (low-level details mixed with high-level)
    total_revenue = sum(sale['amount'] for sale in valid_sales)
    average_sale = total_revenue / len(valid_sales) if valid_sales else 0
    
    # Group by product (more low-level details)
    by_product = {}
    for sale in valid_sales:
        product = sale['product_id']
        if product not in by_product:
            by_product[product] = {'count': 0, 'revenue': 0}
        by_product[product]['count'] += 1
        by_product[product]['revenue'] += sale['amount']
    
    # Format report (mixing abstraction levels)
    report = f"Total Revenue: ${total_revenue:.2f}\n"
    report += f"Average Sale: ${average_sale:.2f}\n"
    report += f"Total Sales: {len(valid_sales)}\n\n"
    report += "By Product:\n"
    for product_id, data in by_product.items():
        avg = data['revenue'] / data['count']
        report += f"  {product_id}: {data['count']} sales, ${data['revenue']:.2f} (avg: ${avg:.2f})\n"
    
    return report


# TODO: Create these helper functions at appropriate abstraction levels:
# - filter_valid_sales(sales_data: list) -> list
# - calculate_revenue_metrics(sales: list) -> dict
# - group_sales_by_product(sales: list) -> dict
# - format_sales_report(metrics: dict, by_product: dict) -> str
# - generate_sales_report_refactored(sales_data: list) -> str
