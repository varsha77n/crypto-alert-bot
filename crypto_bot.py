import requests
import pandas as pd
from datetime import datetime
import os
import time

# --- CONFIGURATION ---
FILE_NAME = "bitcoin_history.csv"
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def fetch_crypto_data():
    """Fetches the current bitcoin price."""
    print("Fetching price...")
    
    # 1. THE FETCH (Day 8)
    response = requests.get(API_URL)
    
    # Check if the waiter is happy (200 OK)
    if response.status_code == 200:
        # 2. THE UNPACKING (Day 9)
        data = response.json()
        price = data['bitcoin']['usd']
        
        # Add the current time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Success! Bitcoin is ${price} at {now}")
        return now, price
    else:
        print("Error fetching data!")
        return None, None

def save_to_csv(timestamp, price):
    """Saves the data to a CSV file."""
    
    # 3. THE STRUCTURE (Day 11)
    # Create a small DataFrame with just this one row
    new_data = pd.DataFrame([{
        "Timestamp": timestamp, 
        "Price (USD)": price
    }])

    # 4. THE SAVE (Day 12 Logic)
    # Check if file exists. 
    # If NO: Write header (Timestamp, Price)
    # If YES: Don't write header, just append data
    if not os.path.isfile(FILE_NAME):
        new_data.to_csv(FILE_NAME, index=False)
    else:
        new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)
    
    print(f"Saved to {FILE_NAME}")

# --- MAIN EXECUTION ---
# Get the data
time_now, btc_price = fetch_crypto_data()

# If we got data successfully, save it
if btc_price:
    save_to_csv(time_now, btc_price)