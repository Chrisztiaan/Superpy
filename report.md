<br />
<div align="center">
  <a href="https://github.com/Chrisztiaan/Superpy">
    <img src="images/winclogo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Superpy report :page_with_curl:</h3>

  <p align="center">
    A report highlighting 3 notable technical elements of Superpy.
    <br />
    <a href="https://github.com/Chrisztiaan/Superpy"><strong>Back to the docs</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#The-Superpy-class">The Superpy class</a>
    </li>
    <li>
      <a href="#Tabulate">Tabulate</a>
    </li>
    <li>
      <a href="#"></a></li>
    </li>
  </ol>
</details>


<!-- The Superpy Class -->
## The Superpy class

When looking for the best way to use argparse in the Superpy application I stumbled on using argparse in a class.
This seemed very clean and organized to me so I decided to use argparse in this manner.

I start by initializing the Superpy class and adding the __init__ functuon.

  ```sh
class Superpy (object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="Superpy", epilog="Enjoy the program!\n", usage='\n\nWelcome to Superpy!!\n\nUse a command and required arguments (positional arguments). You can also use optional arguments in some cases.\nIf you do not know how to use a command type the command followed by -h for help.\n\nUse the UP arrow to copy last command.\n\nCommands:\n\n- Buy\n- Sell\n- Delete\n- Inventory\n- Sold\n- Revenue\n- Profit\n- Report\n- Advance\n- Set Date\n- Expired\n')
        parser.add_argument(
            'command', help='Use: buy, sell, delete, inventory, revenue, advance, expired after main.py')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()
  ```

Below this I created a function for every argument, all using their own parser but also being called through the Superpy class because of the code below:

  ```sh
  def main():
    Superpy()

  if __name__ == "__main__":
    main()
  ```

  Another benefit of the Superpy class is the absence of if/else statements, every argument has its own parser so there is no need for this.


<!-- Tabulate -->
## Tabulate

A second notable implementation of my Superpy application is Tabulate.
Tabulate is a tool that detects columns, aligns them and makes them pretty.
In Superpy I use Pandas to create my dataframes, Tabulate works very well with pandas which makes it a fast and easy solution.

* I call a function that returns a dataframe and put it in a variable.

  ```sh
  df = display_stock(args.id, args.date, args.date2)
  ```

* Secondly I print the dataframe using Tabulate.

  ```sh
  print(tabulate(df, headers="keys", showindex=False, tablefmt="fancy_grid"))
  ```

Very easy! :smile:


<!-- ABOUT THE PROJECT -->
## About The Project
