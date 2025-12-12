import pandas as pd
import plotly.express as px

def plot_sales_by_region(df: pd.DataFrame):
    region_sales = df.groupby("region")["total_sales"].sum().reset_index()
    fig = px.bar(region_sales, x="region", y="total_sales", title="Total Sales by Region")
    return fig

def plot_sales_by_product(df: pd.DataFrame):
    product_sales = df.groupby("product")["total_sales"].sum().reset_index()
    fig = px.pie(product_sales, names="product", values="total_sales", title="Sales Distribution by Product")
    return fig

def bar_chart_sales_by_region(df: pd.DataFrame):
    region_sales = df.groupby("region")["total_sales"].sum().reset_index()
    return px.bar(region_sales, x="region", y="total_sales", title="Sales by Region (Bar Chart)")

def pie_chart_sales_by_region(df: pd.DataFrame):
    region_sales = df.groupby("region")["total_sales"].sum().reset_index()
    return px.pie(region_sales, names="region", values="total_sales", title="Sales by Region (Pie Chart)")

def line_chart_sales_over_time(df: pd.DataFrame):
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    daily_sales = df.groupby("order_date")["total_sales"].sum().reset_index()
    return px.line(daily_sales, x="order_date", y="total_sales", title="Total Sales Over Time")

def plot_sales_forecast(forecast_df: pd.DataFrame):
    if forecast_df.empty:
        return None

    color_map = {
        "Actual": "#1f77b4",     # blue
        "Forecast": "#ff7f0e"    # orange
    }

    fig = px.line(
        forecast_df,
        x="order_date",
        y="total_sales",
        color="type",
        title="📈 Sales Forecast (Next 30 Days)",
        labels={"order_date": "Date", "total_sales": "Total Sales"},
        color_discrete_map=color_map
    )

    fig.update_traces(mode="lines+markers")
    return fig