import time
from utils.helpers import analyze_data

def fetch_data():
    return {
        "wallet": "0xABC123",
        "tx_count": 150
    }

def run():
    while True:
        data = fetch_data()
        result = analyze_data(data)
        print(f"Analysis Result: {result}")
        time.sleep(10)

if __name__ == "__main__":
    run()
