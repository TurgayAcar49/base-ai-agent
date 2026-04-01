def analyze_data(data):
    if data["tx_count"] > 100:
        return "High activity wallet 🚀"
    else:
        return "Normal activity"
