<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Superpy :smile:</h3>

  <p align="center">
    A CLI Application for Supermarkets!
    <br />
    <a href="https://github.com/Chrisztiaan/Superpy"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Chrisztiaan/Superpy/issues">Report Bug</a>
    ·
    <a href="https://github.com/Chrisztiaan/Superpy/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
        <ul>
            <li><a href="#Python and Pip">Python and Pip</a></li>
            <li><a href="#Requirements">Requirements</a></li>
        </ul>
    </li>
    <li>
      <a href="#usage">Usage</a></li>
        <ul>
            <li><a href="#Intro">Intro</a></li>
            <li><a href="#Commands">Commands</a></li>
        </ul>
    </li>
    <li><a href="#report">Report</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Superpy is a CLI application for supermarkets.

With Superpy you can do the following:
* Keep track of products bought
* Keep track of products sold
* Keep track of expired products
* Calculate profit and revenue
* Show profit and revenue in a graph

This way you have full control of your stock without having to rely on pen and paper.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Python and Pip

To use Superpy you need to have Python and Pip installed. Usually Pip is installed with python.
Here's how to check if you have python and pip installed:

Type in your terminal:

* Python

  ```sh
  python --version
  ```

* Pip

  ```sh
  pip --version
  ```

  If you get a version back for both, you are good to go! :smile:
  If not see below for help:
    [https://www.python.org/downloads/](https://www.python.org/downloads)
    [https://pypi.org/project/pip/](https://pypi.org/project/pip/)

### Requirements

When you have python and pip installed there are some more requirements you need to use Superpy.
You can easily install these requirements with the [https://github.com/Chrisztiaan/Superpy/blob/main/requirements.txt](requirements.txt) file

Just use the below command in your terminal:
  ```sh
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

Here I will describe how to use Superpy. 

### Intro

Before giving Superpy a command you will allways have to start with:
  ```sh
  py superpy.py
  ```
Followed by the command.

Every command has a help function. For example:
  ```sh
  py superpy.py inventory -h
  ```
Use this if you feel lost or need a reminder.

### Commands

Below is a list of all the commands :point_down::
* Buy
* Sell
* Delete
* Inventory
* Sold
* Revenue
* Profit
* Report
* Advance
* Set Date
* Expired

Let's dive in and have a closer look 1 by 1 :swimmer:

#### Buy

Use this command  to buy products for your supermarket.
Fill in the id, product name, price, expiration date and the amount of the product.

Example:
  ```sh
  py superpy.py buy 1002 "Bananas - Chiquita" 0.10 2022-09-01 60
  ```

#### Sell

Use this command to sell a product and remove it from the inventory.
Fill in the id, price and the amount your selling.
Example:
  ```sh
  py superpy.py sell 1002 0.20 30
  ```

#### Delete


#### Inventory
#### Sold
#### Revenue
#### Profit
#### Report
#### Advance
#### Set Date
#### Expired



    

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: www.linkedin.com/in/christiaan-verlaan-86541610b/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555