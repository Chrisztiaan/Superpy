# Imports
from csv import writer
import datetime as dt
import pandas as pd

# Time | Gets the current date from time.txt
with open('time.txt') as f:
    global_date = f.readline()

""" 
Functions:
    - advance_time
    - set_date
    - display_stock
    - delete_stock
    - add_bought_product
    - add_sold_product
    - sold_stock
    - profit
    - revenue
    - get_price
    - get_amount
    - get_product_name
    - is_product_name_true
    - is_id_true
"""
# Advance Time | Advances time an amount of days

def advance_time(number):
    if number > 0:
        with open('time.txt') as f:
            current_date = f.readline()
        current_date = dt.datetime.strptime(current_date, '%Y-%m-%d').date()
        delta = dt.timedelta(number)
        new_date = current_date + delta
        with open('time.txt', 'w') as f:
            f.write(str(new_date))
        return(f'Travelled through time!!\nDate: {new_date}')
    else:
        return(f'Travelled through ti... wait nothing happened.\nDate is still: {global_date}')

# Set Date | Sets the date to a specific date

def set_date(date):
        with open('time.txt', 'w') as f:
            f.write(str(date))
        return(f'Travelled through time!!\nDate: {date}')

# Display Inventory | Returns dataframe of bought.tsv

def display_stock(id, date, date2):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('bought.tsv', sep='\t')
    if date != None and date2 != None:
        df = df[(df['buy_date'] >= date) & (df['buy_date'] <= date2)]
    elif date != None:
        df = df[df.buy_date.eq(date)]
    if id != None:
        # Change id to int, does not string with eq
        id = int(id)
        df = df[df.id.eq(id)]
    return df

# Deleting A Product | Deletes a product from bought.tsv or changes the amount

def delete_stock(id, amount):
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df.set_index('id', drop=False, verify_integrity=False)
    stock_amount = get_amount(id)
    if stock_amount == amount:
        df = df.drop(df[df.id == id].index)
        df.to_csv('bought.tsv', sep='\t', index=False)
        return 'Product Deleted'
    elif amount > stock_amount:
        return 'Not Enough Stock Available'
    else:
        new_amount = stock_amount - amount
        df.at[id, 'amount'] = new_amount
        df.to_csv('bought.tsv', sep='\t', index=False)
        return 'Stock Amount Changed'


# Buying A Product | Adds a product to bought.tsv

def add_bought_product(id, product_name, price, expiration_date, amount):
    list = [id, product_name, global_date, price, expiration_date, amount]
    # Check if id is the same, then only change amount
    if is_id_true(id):
        # Check if name is the same
        if is_product_name_true(id, product_name) == True:
            new_amount = get_amount(id) + amount
            df = pd.read_csv('bought.tsv', sep='\t')
            df = df.set_index('id', drop=False, verify_integrity=False)
            df.at[id, 'amount'] = new_amount
            df.to_csv('bought.tsv', sep='\t', index=False)
            return 'Stock Amount Changed'
        else:
            return 'Product name does not match ID'
    # If ID not the same, write new line
    else:
        with open('bought.tsv', 'a', newline='') as file:
            writer_object = writer(file, delimiter='\t')
            writer_object.writerow(list)
            file.close()
            return(f'{product_name} Bought')


# Selling A Product | Adds a product to sold.tsv 

def add_sold_product(id, price, amount):
    profit = (price - get_price(id)) * amount
    revenue = price * amount
    list = [id, global_date, amount, price, revenue, profit]
    delete = delete_stock(id, amount)
    if delete == 'Not Enough Stock Available':
        return 'Not Enough Stock Available'
    else:
        with open('sold.tsv', 'a', newline='') as file:
            writer_object = writer(file, delimiter='\t')
            writer_object.writerow(list)
            file.close()
        return 'Product Sold'

# Sold Stock | Returns dataframe of sold.tsv

def sold_stock(sell_date, sell_date_2):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('sold.tsv', sep='\t')
    # Potential filter on product
    if sell_date != None and sell_date_2 != None:
        df = df[(df['sell_date'] >= sell_date) & (df['sell_date'] <= sell_date_2)]
        return df
    elif sell_date != None:
        df = df[df.sell_date.eq(sell_date)]
        return df
    else:
        df = df[df.sell_date.eq(global_date)]
        return df

# Profit | Returns the profit for a certain date

def profit(date, date2):
    df = sold_stock(date, date2)
    column = 'profit'
    profit = df[column].sum()
    return(profit)

# Revenue | Returns the revenue for a certain date

def revenue(date, date2):
    df = sold_stock(date, date2)
    column = 'revenue'
    revenue = df[column].sum()
    return(revenue)

# Expired | Returns dataframe with expired products

def expired():
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df[(df['expiration_date'] < global_date)]
    return df

# Get Price | Gets price from bought.tsv

def get_price(id):
    column = 'price'
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df[df.id.eq(id)]
    price = df[column].sum()
    return(price)

# Get Amount | Gets amount from bought.tsv

def get_amount(id):
    column = 'amount'
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df[df.id.eq(id)]
    amount = df[column].sum()
    return(amount)

# Get Product Name | Gets Product name from bought.tsv

def get_product_name(id):
    df = pd.read_csv('bought.tsv', sep='\t')
    # - 1 for indexing(from 0) of csv file
    index_id = id - 1
    product_name = df._get_value(index_id, 'product_name')
    return product_name

# Is Product Name True | Checks if Product Name is in bought.tsv

def is_product_name_true(id, product_name):
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df[df.id.eq(id)]
    df_product_name = get_product_name(id)
    if df_product_name == product_name:
        return True
    else:
        return False

# Is ID True | Checks if ID is in bought.tsv

def is_id_true(id):
    column = 'id'
    df = pd.read_csv('bought.tsv', sep='\t')
    df = df[df.id.eq(id)]
    df_id = df[column].sum()
    if df_id == id:
        return True
    else:
        return False


def main():
    print(profit("2021-12-05", None))

if __name__ == "__main__":
    main()
