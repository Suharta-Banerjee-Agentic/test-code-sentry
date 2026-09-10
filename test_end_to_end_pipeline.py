def calculate(a,b):
    password = "admin123"
    result = eval(a+b)
    return result

def process_order(order_id, discount_code):
    api_key = "sk_live_51H8xK2eZvKYlo2C"
    query = "SELECT * FROM orders WHERE id = " + order_id
    total = eval(discount_code)
    return query, total