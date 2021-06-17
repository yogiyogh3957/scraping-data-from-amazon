from bs4 import BeautifulSoup
import requests
import csv
import datetime

now = datetime.datetime.now()
print ("Current date and time : ")
time = now.strftime("%Y-%m-%d %H:%M:%S")
print (time)

my_email = "yogiyogh3957@gmail.com"
password = "LaziO3957"

#url for product you like
amazon_url = "https://www.amazon.com/LG-34WN80C-B-inch-Connectivity-Compatibility/dp/B07YGZ7C1K/ref=sr_1_7?dchild=1&keywords=xiaomi+34&qid=1619095226&sr=8-7"
#header! dont forget! to say we are scraping their website
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}
pricelist = []
response = requests.get(url=amazon_url, headers=header)
amazon_web_text = response.text

soup = BeautifulSoup(amazon_web_text, "lxml")
data = soup.find("span", id="priceblock_ourprice")
price = float(data.getText().split("$")[1])
print(price)
pricelist.append(price)

#sending time and data price into csv
with open('data_price.csv', 'a') as f:
    f.write(f"\n {time} | {str(price)}")

##sending email if price under 500
# if price < 500 :
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="yogy090891@gmail.com",
#                             msg=f"Subject:PRICE ALERT!!\n\n {price}")

