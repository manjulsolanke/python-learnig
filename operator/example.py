def main():
    """Assignment operators"""
    items_name = 'banana'
    quantity = 10
    discount_rate = 0.1
    eligible_items = 'orange banana carrot'
    items_price = 2 # USD

    """Arithmetic Operator"""
    # calculate subtotal as item_price * quantity
    subtotal = items_price * quantity
    # print the subtotal price 
    print(f"item_name: {items_name}, subtotal: {subtotal}")
    # Initialize discount to 0
    discount = 0

    """membership operator"""
    if items_name in eligible_items:
        discount = subtotal * discount_rate

    # print discount
        print(f"discount: {discount}")
    
    """Comparison operator"""
    # check if discount applied (discount > 0)
    was_discount_applied = discount > 0
    print(f"Was the discount applied {was_discount_applied}")
    """Logical Operator"""
    # check if free shipping should be applied (quantity > 5 AND item_name = 'banana')
    does_free_shipping_apply = quantity >= 5 and items_name == 'banana'
    print(f"Is this item eligible for free shipping? {does_free_shipping_apply}")

if __name__ == '__main__':
    main()