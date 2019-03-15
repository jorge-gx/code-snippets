for orders in orders_data_list:
    orderCount += 1
    # --- ORDERS fields ---
    orders_dict_object = {
        'Order ID': orders.get('id'),
        'User ID': orders.get('user').get('id', "N/A"),
        'Name': orders.get('user').get('name', "N/A"),
        'User Email': orders.get('user').get('email', "N/A"),
        'Catalog ID': orders.get('catalog').get('id', "N/A"),
        'Catalog': orders.get('catalog').get('name', "N/A"),
        'Listing ID': orders.get('listings')[0].get('id', "N/A"),
        'Listing': orders.get('listings')[0].get('title', "N/A"),
        'Order Date': orders.get('created_at', "N/A"),
        'List Price': orders.get('listings')[0].get('amount', 0.0),
        'Promotion Code': orders.get('promotions')[0].get('code', "N/A") if orders.get('promotions') else "N/A",
        'Discount Amount': orders.get('promotions')[0].get('amount', 0.0) if orders.get('promotions') else 0.0,
        'Amount Paid': orders.get('payments')[0].get('amount', 0.0) if orders.get('payments') else 0.0,
        'Transaction Date': orders.get('purchased_at', "N/A"),
    }
