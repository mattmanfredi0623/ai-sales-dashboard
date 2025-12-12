import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def forecast_sales(df, days_ahead=30):
    if df.empty:
        return pd.DataFrame()

    # Ensure date format
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Daily sales
    daily = df.groupby("order_date")["total_sales"].sum().reset_index()

    # Create time index for regression
    daily = daily.sort_values("order_date")
    daily["day_index"] = (daily["order_date"] - daily["order_date"].min()).dt.days

    # Prepare X and y
    X = daily["day_index"].values.reshape(-1, 1)
    y = daily["total_sales"].values

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future
    last_day = daily["order_date"].max()
    future_dates = [last_day + timedelta(days=i) for i in range(1, days_ahead + 1)]
    future_index = np.array([(d - daily["order_date"].min()).days for d in future_dates]).reshape(-1, 1)
    future_sales = model.predict(future_index)

    forecast_df = pd.DataFrame({
        "order_date": future_dates,
        "total_sales": future_sales
    })

    forecast_df["type"] = "Forecast"
    daily["type"] = "Actual"

    return pd.concat([daily[["order_date", "total_sales", "type"]], forecast_df])