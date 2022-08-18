# Imports
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import ConciseDateFormatter

# Time | Gets the current date from time.txt
with open('time.txt') as f:
    global_date = f.readline()


# Report | Initial function called with argument

def report(type, date, date2):
    if type == "profit":
        return profit_plot(date, date2)
    elif type == "revenue":
        return revenue_plot(date, date2)


# Revenue Plot

def revenue_plot(date, date2):
    # Defining columns to be used
    columns = ["sell_date", "revenue"]
    # Creating dataframe
    df = pd.read_csv("sold.tsv", sep='\t', usecols=columns, parse_dates=['sell_date'])
    if date != None and date2 != None:
        df = df[(df['sell_date'] >= date) & (df['sell_date'] <= date2)]
    # Dates to datetime | Used in locator
    df['sell_date'] = pd.to_datetime(df['sell_date'])
    # Making figure
    plt.title("Revenue")
    plt.ylabel('Amount')
    plt.xlabel('Date')
    # Locator | Locates dates and auto formats
    locator = AutoDateLocator()
    formatter = ConciseDateFormatter(locator)
    # Plotting 
    plt.plot(df.sell_date, df.revenue)
    # Show graph
    plt.show()
        # Return message to terminal
    print("Data that the graph is based on:")
    return df


# Profit Plot

def profit_plot(date, date2):
    # Defining columns to be used
    columns = ["sell_date", "profit"]
    # Creating dataframe
    df = pd.read_csv("sold.tsv", sep='\t', usecols=columns, parse_dates=['sell_date'])
    if date != None and date2 != None:
        df = df[(df['sell_date'] >= date) & (df['sell_date'] <= date2)]
    # Dates to datetime | Used in locator
    df['sell_date'] = pd.to_datetime(df['sell_date'])
    # Making figure
    plt.title("Revenue")
    plt.ylabel('Amount')
    plt.xlabel('Date')
    # Locator | Locates dates and auto formats
    locator = AutoDateLocator()
    formatter = ConciseDateFormatter(locator)
    # Plotting 
    plt.plot(df.sell_date, df.profit)
    # Show graph
    plt.show()
    # Return message to terminal
    print("Data that the graph is based on:")
    return df

def main():
    revenue_plot(None, None)
if __name__ == "__main__":
    main()
