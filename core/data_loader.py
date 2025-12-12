import pandas as pd
import os

def load_data(path: str = "data/sales_data.csv") -> pd.DataFrame:
    if not os.path.exists(path):
        return None

    df = pd.read_csv(path)
    
    # Optional: Convert dates
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['Month'] = df['Month'].astype(str)

    return df