import requests      
import csv          
from datetime import datetime  
import os            

file_name = "bitcoin_prices.csv"

if not os.path.exists(file_name):
  
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Bitcoin Price (USD)"])
    print("New file created!")
else:
    print("File already exists, adding new row...")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url, timeout=10)  
    data = response.json()                    
    price = data["bitcoin"]["usd"]            
    print(f"Bitcoin price fetched: ${price}")

except Exception as e:
    print("Something went wrong:", e)
    price = None  



if price is not None: 

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  

  
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, price]) 

    print(f"Saved successfully!")
    print(f"Time: {timestamp}")
    print(f"Price: ${price}")

else:
    print("Nothing was saved because we could not get the price.")