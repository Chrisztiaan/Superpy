# Imports
import argparse
import csv
import datetime as dt
import sys
import pandas as pd
# function.py
from functions import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

# Superpy class


class Superpy (object):

    # Define general command. This code is used for all subcommands.

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="Superpy", epilog="Enjoy the program!\n", usage='\n\nWelcome to Superpy!!\n\nUse a command and required arguments (positional arguments). You can also use optional arguments in some cases.\nIf you do not know how to use a command type the command -h for help.\n\nUse the UP arrow to copy last command.')
        parser.add_argument(
            'command', help='Use: buy, sell, delete, inventory, revenue, advance')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

# The buy subcommand. Used for buying products.

    def buy(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this command to buy a product and add it to the inventory.\nYou have to fill in all the arguments mentioned below.')
        parser.add_argument('id', type=int, help='Fill in ID')
        parser.add_argument('product_name', type=str,
                            help='Fill in product name')
        parser.add_argument('price', type=float, help='Fill in price')
        parser.add_argument('expiration_date', type=lambda s: dt.datetime.strptime(
            s, '%Y-%m-%d'), help='Fill in the expiration date as yyyy-mm-dd')
        parser.add_argument('amount', type=int,
                            help='Fill in the amount of the product')
        args = parser.parse_args(sys.argv[2:])
        print(add_bought_product(args.id, args.product_name,
                                 args.price, args.expiration_date, args.amount))

# The sell command. Used for selling products.

    def sell(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this command to sell a product and remove it from the inventory.\nYou have to fill in all the arguments mentioned below.')
        parser.add_argument('id', type=int, help='Fill in the ID')
        parser.add_argument('price', type=float, help='Fill in the price')
        parser.add_argument('amount', type=int, help='Fill in the amount')
        args = parser.parse_args(sys.argv[2:])
        print(add_sold_product(args.id, args.price, args.amount))


# The delete command. Used for deleting products.

    def delete(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this command to delete a product.\nThe amount you fill in will be removed from the inventory.\nUse this for damaged goods or other exceptions.')
        parser.add_argument('id', type=int, help='Fill in the ID')
        parser.add_argument('amount', type=int, help='Fill in the amount')
        args = parser.parse_args(sys.argv[2:])
        print(delete_stock(args.id, args.amount))


# The inventory command. Used for displaying inventory.

    def inventory(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this command to view the inventory.\nCan be filtered by product or date.\nTo filter use the argument followed by the product/date or both.')
        parser.add_argument('--product', help='Add a product to filter')
        parser.add_argument('--date', help='Add a date to filter the buy date')
        args = parser.parse_args(sys.argv[2:])
        print(display_stock(args.product, args.date))

# The revenue command. Used to calculate the revenue of a certain day.

    def revenue(self):
        parser = argparse.ArgumentParser(
            usage='\n\nCalculate revenue, today is standard but you can filter by date.')
        parser.add_argument('--date', help='Add a date to filter by date')
        args = parser.parse_args(sys.argv[2:])
        print(revenue(args.date))


# The profit command. Used to calculate the profit of a certain day.

    def profit(self):
        parser = argparse.ArgumentParser(
            usage='\n\nCalculate profit, today is standard but you can filter by date.')
        parser.add_argument('--date', help='Add a date to filter by date')
        args = parser.parse_args(sys.argv[2:])
        print(revenue(args.date))


# The advance command. Used to advance time by a number of days.

    def advance(self):
        parser = argparse.ArgumentParser(
            usage='\n\n Use this command to advance time by a number of days.')
        parser.add_argument(
            'days', help='Fill in number of days you want to advance time')
        args = parser.parse_args(sys.argv[2:])
        print(advance_time(int(args.days)))


def main():
    Superpy()


if __name__ == "__main__":
    main()
