# Stock Analysis

This Python script allows you to track the stock price of a specified company over time. It fetches real-time stock data from Google and stores it in a MySQL database. The program runs for a user-defined duration, and at the end of the execution, it provides statistical information about the stock prices, including the maximum, minimum, and average values.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Twisted](https://pypi.org/project/Twisted/)
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
- [Matplotlib](https://pypi.org/project/matplotlib/)

Install the dependencies using:

```bash
pip install requests beautifulsoup4 Twisted mysql-connector-python matplotlib

```

## Configuration
Update the MySQL connection details:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="test"
)
```

## User Input
The script requests the user to provide a stock name along with the duration for which it should track the stock.

## Web Scraping
The script monitors the current stock prices of the specified stock in real-time at 5-second intervals for the duration specified. It achieves this by employing a library called BeautifulSoup, designed for parsing web applications.

## Database Integration
The script inserts the stock prices into the specified database as indicated in the code. Subsequently, crucial information, including the maximum, minimum, and average stock prices, is computed.

## Data Visualization
The code fetches data from the database and utilizes matplotlib to generate a graph. In the graph, the time is represented on the x-axis, and the stock price is represented on the y-axis.
