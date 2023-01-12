import pandas as pd
import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from  email.message import EmailMessage
import ssl
import smtplib
import time

PATH = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)


URL = ["https://www.akakce.com/anakart/en-ucuz-msi-pro-b650m-a-wi-fi-amd-am5-ddr5-matx-fiyati,30374251.html"
,"https://www.akakce.com/anakart/en-ucuz-msi-mag-b650m-mortar-wi-fi-amd-am5-ddr5-matx-fiyati,30374291.html"]

today = datetime.date.today()
yesterday = (today) - timedelta(days=1)
email_sender = "mrtinc40@gmail.com"
email_password = "your_password"
email_receiver = "mrtinc15@gmail.com"
subject = "Prices dropped for these items:"
items = []

from datetime import datetime
today_str = datetime.strftime(today, "%Y-%m-%d")
yesterday_str = datetime.strftime(yesterday, "%Y-%m-%d")

def price_checker():
   for x in URL:
      driver.get(x)
      time.sleep(2)
      product = driver.find_elements(By.XPATH, "/html/body/main/div[1]/div/div[1]/h1")
      try:
         driver.find_element(By.XPATH, "/html/body/main/div[1]/div/p[2]")
         stock = ("Stok yok")
         data = {"Product": [product[0].text],
         "Stock": [stock],
         "Price": ["-"],
         "Shipping": ["-"],
         "Date": [today]}
      except NoSuchElementException:
         price = driver.find_elements(By.CLASS_NAME, "pt_v8")
         shipping =driver.find_elements(By.XPATH, "/html/body/main/div[1]/div/div[3]/span[1]/em")
         stock = ("Stok var")
         data = {"Product": [product[0].text],
         "Stock": [stock],
         "Price": [price[0].text],
         "Shipping": [shipping[0].text],
         "Date": [today]}
         yol = 1
      finally:
         df = pd.DataFrame(data)
         print(df)
         df.to_csv(r"C:\Users\mrtin\urun_fiyatlari.csv", mode="a", header=False, index=False)
         df1 = pd.read_csv(r"C:\Users\mrtin\urun_fiyatlari.csv", on_bad_lines="skip")
         if yol == 1:
            df["Price"].str.replace(".","", regex=True)
            df["Price"] = df["Price"].str[:-6]
         df1["Price"] = df1["Price"].str[:-6]
         df1["Price"] = pd.to_numeric(df1["Price"])
         df["Price"] = pd.to_numeric(df["Price"])
         price_today = df[(df["Date"] == today) & (df["Product"] == product[0].text)]
         price_yesterday = df1[(df1["Date"] == yesterday_str) & (df1["Product"] == product[0].text)]
         price_today1 = price_today["Price"]
         price_yesterday1 = price_yesterday["Price"]
         price_today2 = price_today1.iloc[0]
         price_yesterday2 = price_yesterday1.iloc[0]
         print("Price yesterday is:", price_yesterday2)
         print("Price today is:", price_today2)
         if (price_today2 != "-") and (price_today2 < price_yesterday2):
            print("fiyat dustu")
            items.append(product[0].text)
         time.sleep(3) 
   s = ", "
   items2 = s.join(items)
   em = EmailMessage()
   em["From"] = email_sender
   em["To"] = email_receiver
   em["Subject"] = subject
   em.set_content(items2)
   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())
while(True):
   price_checker()
   time.sleep(86400)          
