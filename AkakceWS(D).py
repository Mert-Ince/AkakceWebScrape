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
,"https://www.akakce.com/anakart/en-ucuz-msi-mag-b650m-mortar-wi-fi-amd-am5-ddr5-matx-fiyati,30374291.html"
,"https://www.akakce.com/anakart/en-ucuz-msi-mag-b650-tomahawk-wi-fi-amd-am5-ddr5-atx-fiyati,30374310.html"
,"https://www.akakce.com/anakart/en-ucuz-asus-tuf-gaming-b650-plus-wifi-amd-am5-ddr5-atx-fiyati,66156160.html"
,"https://www.akakce.com/anakart/en-ucuz-asus-tuf-gaming-b650m-plus-wifi-amd-am5-ddr5-micro-atx-fiyati,66157202.html"
,"https://www.akakce.com/bilgisayar-kasasi/en-ucuz-aerocool-airhawk-duo-argbairhawkd-led-fanli-atx-fiyati,577001818.html"
,"https://www.akakce.com/ekran-karti/en-ucuz-sapphire-radeon-rx-7900-xtx-gaming-21322-01-20g-384-bit-gddr6-24-gb-fiyati,186465309.html"
,"https://www.akakce.com/ekran-karti/en-ucuz-msi-rtx-4080-16gb-ventus-3x-oc-256-bit-gddr6x-16-gb-fiyati,2121828611.html"
,"https://www.akakce.com/ekran-karti/en-ucuz-gigabyte-rtx-4080-16gb-eagle-oc-gv-n4080eagle-oc-16gd-256-bit-gddr6x-16-gb-fiyati,121429413.html"
,"https://www.akakce.com/ekran-karti/en-ucuz-gigabyte-rtx-4080-eagle-gv-n4080eagle-16gd-256-bit-gddr6x-16-gb-fiyati,121429465.html"
,"https://www.akakce.com/ekran-karti/en-ucuz-xfx-speedster-merc-310-rx-7900-xtx-black-rx-79xmercb9-384-bit-gddr6-24-gb-fiyati,186443737.html"
,"https://www.akakce.com/islemci/en-ucuz-amd-ryzen-7-7700x-sekiz-cekirdek-4-50-ghz-kutulu-fiyati,2120992215.html"
,"https://www.akakce.com/islemci/en-ucuz-amd-ryzen-7-5800x3d-3-40ghz-8-cekirdek-100mb-onbellek-soket-am4-fiyati,1863582320.html"
,"https://www.akakce.com/islemci/en-ucuz-amd-ryzen-5-7600x-alti-cekirdek-4-7-ghz-fiyati,2120992208.html"
,"https://www.akakce.com/islemci-sogutucu/en-ucuz-deepcool-ak620-ak400-fiyati,2060660649.html"
,"https://www.akakce.com/islemci-sogutucu/en-ucuz-deep-cool-ak620-fiyati,1664695837.html"
,"https://www.akakce.com/monitor/en-ucuz-samsung-ls49ag950nuxuf-kavisli-oyuncu-u-49-odyssey-neo-g9-1-ms-240-hz-dual-qhd-quantum-mini-led-hdr-2000-rgb-1000r-siyah-fiyati,1618509300.html"
,"https://www.akakce.com/monitor/en-ucuz-samsung-odyssey-g7-lc32g75tqsrxuf-32-1ms-wqhd-g-sync-freesync-curved-pivot-oyuncu-u-fiyati,1230222788.html"
,"https://www.akakce.com/power-supply/en-ucuz-asus-rog-strix-1000g-1000-w-fiyati,911172949.html"
,"https://www.akakce.com/power-supply/en-ucuz-corsair-rm1000e-1000w-80-plus-gold-dusuk-gurultulu-tam-moduler-guc-kaynagi-fiyati,152580434.html"
,"https://www.akakce.com/power-supply/en-ucuz-corsair-rm850-cp-9020196-eu-850-w-fiyati,609823230.html"
,"https://www.akakce.com/power-supply/en-ucuz-fsp-hg2-850-hydro-g-pro-850w-fiyati,759182471.html"
,"https://www.akakce.com/power-supply/en-ucuz-fsp-hydro-g-pro-hg2-1000-1000w-80-gold-120mm-fan-moduler-fiyati,1347244580.html"
,"https://www.akakce.com/power-supply/en-ucuz-corsair-rm850-cp-9020235-eu-850-w-fiyati,1474415784.html"
,"https://www.akakce.com/ram/en-ucuz-kingston-fury-beast-rgb-kf552c40bbak2-16-16-gb-2x8-ddr5-5200-mhz-cl40-fiyati,1905501395.html"
,"https://www.akakce.com/ram/en-ucuz-kingston-furybeast-8-gb-5200-mhz-ddr5-cl40-kf552c40bb-8-fiyati,1773387219.html"
,"https://www.akakce.com/ram/en-ucuz-kingston-fury-beast-black-16gb-5200mt-s-ddr5-cl40-xmp-3-0-masaustu-kit-of-2-kf552c40bbk2-16-fiyati,173414046.html"
,"https://www.akakce.com/ssd/en-ucuz-western-digital-1-tb-blue-sn550-wds100t2b0c-m-2-pci-express-3-0-fiyati,640643605.html"
,"https://www.akakce.com/ssd/en-ucuz-silicon-power-p34a60-512-gb-sp512gbp34a60m28-m-2-pci-express-3-0-fiyati,1053122830.html"
,"https://www.akakce.com/ssd/en-ucuz-kingston-500-gb-a2000-sa2000m8-500g-m-2-pci-express-3-0-fiyati,535280303.html"
,"https://www.akakce.com/ssd/en-ucuz-western-digital-500-gb-blue-sn550-wds500g2b0c-m-2-pci-express-3-0-fiyati,631482856.html"
,"https://www.akakce.com/bilgisayar-kasasi/en-ucuz-deep-cool-ck560-siyah-atx-oyuncu-kasasi-fiyati,2050740891.html"
,"https://www.akakce.com/monitor/en-ucuz-samsung-odyssey-g7-lc27g75tqsrxuf-27-1ms-wqhd-g-sync-freesync-curved-pivot-oyuncu-u-fiyati,1231022518.html"
,"https://www.akakce.com/monitor/en-ucuz-gigabyte-m28u-28-1-ms-4k-oyuncu-u-fiyati,1522463759.html"
,"https://www.akakce.com/bilgisayar-kasasi/en-ucuz-corsair-4000d-airflow-cc-9011200-ww-fanli-atx-oyuncu-kasasi-fiyati,811352456.html"
,"https://www.akakce.com/monitor/en-ucuz-msi-27-9-optix-mag281urf-flat-rapid-ips-3840x2160-uhd-169-144hz-1ms-g-sync-compatible-gaming-monitor-fiyati,2077826255.html"
,"https://www.akakce.com/monitor/en-ucuz-samsung-odyssey-neo-g7-ls32bg750nuxuf-32-1ms-165hz-uhd-quantum-mini-led-hdr2000-1000r-pivot-gaming-fiyati,2115869419.html"
,"https://www.akakce.com/monitor/en-ucuz-hp-x27q-qhd-oyuncu-u-fiyati,33990942.html"
,"https://www.akakce.com/monitor/en-ucuz-lg-27gp850-27-1ms-qhd-g-sync-freesync-pivot-oyuncu-u-fiyati,1477232249.html"
,"https://www.akakce.com/monitor/en-ucuz-lg-32gp850-b-31-5-1-ms-2k-g-sync-freesync-ohd-ips-oyuncu-u-fiyati,1611529358.html"
,"https://www.akakce.com/monitor/en-ucuz-gigabyte-31-5-m32u-1ms-144hz-hdmi-displayport-usb-type-c-adaptive-sync-4k-gaming-fiyati,1531517715.html"
,"https://www.akakce.com/monitor/en-ucuz-gigabyte-m34wq-34-1-ms-wqhd-oyuncu-u-fiyati,1509980886.html"]

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
