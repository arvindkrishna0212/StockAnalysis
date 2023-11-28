import requests
from bs4 import BeautifulSoup
from twisted.internet import task, reactor
import mysql.connector
import datetime
import matplotlib.pyplot as plt

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="test"
    )

    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists stock (stock_price float, time varchar(20))")
    mycursor.execute("delete from stock")
    print(mydb)
except mysql.connector.Error as err:
    print("MySQL Error:", err)
    exit()

a = input("Enter the stock: ")
b = float(input("Enter the number of minutes you want the program to run: "))
ct = 0
url = f'https://www.google.com/search?q={a}+stock+price'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

time_data = []
stock_price_data = []

def stock():
    global ct
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd")

    if price_element:
        price = price_element.text
        new = ""
        for i in price:
            new = new + i
            if i == " ":
                break
        print(f"Stock: {a}")
        print(f"Stock Price: {new}")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)
        try:
            sql = "insert into stock (stock_price, time) values (%s, %s)"
            val = (round(float(new),2), current_time)
            mycursor.execute(sql, val)
            mydb.commit()

            time_data.append(current_time)
            stock_price_data.append(float(new))

            ct = ct + 1
            if ct > (b * 60) / 5:
                mycursor.execute("select max(stock_price) from stock")
                e = round(mycursor.fetchone()[0], 2)
                mycursor.execute("select min(stock_price) from stock")
                f = round(mycursor.fetchone()[0], 2)
                mycursor.execute("select avg(stock_price) from stock")
                g = round(mycursor.fetchone()[0], 2)
                print(f"The max price is {e}")
                print(f"The min price is {f}")
                print(f"The avg price is {g}")
                print("Program finished.")
                reactor.stop()
        except mysql.connector.Error as err:
            print("MySQL Error:", err)

    else:
        print("Stock price not found on Google.")

l = task.LoopingCall(stock)
l.start(5.0)
reactor.run()

plt.plot(time_data, stock_price_data)
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.title(f"{a} Stock Price Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

