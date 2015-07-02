
def demarcation_line_length(length):
    """prints a specified length of astrix to create a nice line for demacation in reporting"""   
    print length * "*"

def count_orders_by_type(filename_type):
    """outputs count of orders by type of melon sold and total revenue

    takes file with order data of type and number sold, 
    demarced by a pipe returns summary"""

    file_orders_type = open(filename_type)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for line in file_orders_type:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    file_orders_type.close()
  
def count_orders_by_sales_type(filename_sales):
    """outputs total sales by where sale was made

    takes file with sales data and where sale was made (i.e. internet or salesperson), 
    demarcated by pipe, and returns summary"""

    file_sales = open(filename_sales)
    salesperson_index = 0
    internet_index = 1
    sales = [0, 0]
    for line in file_sales:
        d = line.split("|")
        if d[1] == "0":
            sales[0] += float(d[3])
        else:
            sales[1] += float(d[3])
    print "Salespeople generated %0.2f in revenue." % sales[1]
    print "Internet sales generated %0.2f in revenue." % sales[0]
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


demarcation_line_length(80)
count_orders_by_type("orders-by-type.txt")
demarcation_line_length(45)
count_orders_by_sales_type("orders-with-sales.txt")
demarcation_line_length(45)
