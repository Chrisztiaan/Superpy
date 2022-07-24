# Imports
from csv import writer
import datetime as dt
import pandas as pd


# Time
with open('time.txt') as f:
    global_date = f.readline()


# Advance time

def advance_time(number):
    with open('time.txt') as f:
        current_date = f.readline()
    current_date = dt.datetime.strptime(current_date, '%Y-%m-%d').date()
    print(type(current_date))
    delta = dt.timedelta(number)
    new_date = current_date + delta
    with open('time.txt', 'w') as f:
        f.write(str(new_date))
    return(f'Date is: {new_date}')


# Display Inventory

def display_stock(product, date):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('bought.csv', sep='\t')
    if product != None:
        df = df[df.product_name.eq(product)]
    if date != None:
        df = df[df.buy_date.eq(date)]
    return df


# Deleting a product

def delete_stock(id, amount):
    df = pd.read_csv('bought.csv', sep='\t')
    df.set_index('id')
    stock_amount = get_amount(id)
    if stock_amount == amount:
        df = df.drop(df[df.id == id].index)
        df.to_csv('bought.csv', sep='\t', index=False)
        return 'Product Deleted'
    elif amount > stock_amount:
        return 'Not Enough Stock Available'
    else:
        new_amount = stock_amount - amount
        df.at['id', 'amount'] = new_amount
        df.to_csv('bought.csv', sep='\t', index=False)
        return 'Stock Amount Changed'


# Buying a product

def add_bought_product(id, product_name, price, expiration_date, amount):
    list = [id, product_name, global_date, price, expiration_date, amount]
    if is_id_true(id) == True:
        with open('bought.csv', 'a', newline='') as file:
            writer_object = writer(file, delimiter='\t')
            writer_object.writerow(list)
            file.close()
            return(f'{product_name} Bought')
    else:
        df = pd.read_csv('bought.csv', sep='\t')
        df.set_index('id')
        df.at['id', 'amount'] = amount
        df.to_csv('bought.csv', sep='\t', index=False)
        return 'Stock Amount Changed'


# Selling a product

def add_sold_product(id, price, amount):
    profit = (price - get_price(id)) * amount
    list = [id, global_date, price, profit, amount]
    delete = delete_stock(id, amount)
    if delete == 'Not Enough Stock Available':
        return 'Not Enough Stock Available'
    else:
        with open('sold.csv', 'a', newline='') as file:
            writer_object = writer(file, delimiter='\t')
            writer_object.writerow(list)
            file.close()
        return 'Product Sold'

# Get Price


def get_price(id):
    column = 'price'
    df = pd.read_csv('bought.csv', sep='\t')
    df = df[df.id.eq(id)]
    price = df[column].sum()
    return(price)


# Get Amount

def get_amount(id):
    column = 'amount'
    df = pd.read_csv('bought.csv', sep='\t')
    df = df[df.id.eq(id)]
    amount = df[column].sum()
    return(amount)

# Is ID true


def is_id_true(id):
    column = 'id'
    df = pd.read_csv('bought.csv', sep='\t')
    df = df[df.id.eq(id)]
    df_id = df[column].sum()
    if df_id == id:
        return True
    else:
        return False

# Get Product Name

def get_product_name(id):
    df = pd.read_csv('bought.csv', sep='\t')
    product_name = df._get_value(id, 'product_name')
    return product_name


# Revenue


def revenue(date):
    df = pd.read_csv('sold.csv', sep='\t')
    column = 'sell_price'
    if date == None:
        df = df[(df.sell_date == global_date)]
        revenue = df[column].sum()
        return(f'Revenue is: {revenue}')


def main():
    None


if __name__ == "__main__":
    main()
