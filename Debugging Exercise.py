"""
Name: Jay Genao
Date: January 27, 2026
Program Description:
This program calculates discounts for products. The original version caused a
TypeError when a product price was stored as a string. The program was debugged
and updated to handle invalid data types gracefully.
"""


def calculate_discount(price, discount_rate):
    """
    Calculates the discount amount based on the price and discount rate.

    Parameters:
        price (float): Product price
        discount_rate (float): Discount rate

    Return:
        float: Discount amount
    """
    return price * discount_rate


def apply_discount(price, discount_amount):
    """
    Applies the discount to the original price.

    Parameters:
        price (float): Original price
        discount_amount (float): Discount amount

    Return:
        float: Final price
    """
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},  # BUG HERE
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except ValueError:
            print(
                f"Error processing {product['name']}: "
                f"Invalid price value ({product['price']}). Price must be numeric.\n"
            )


if __name__ == "__main__":
    main()
