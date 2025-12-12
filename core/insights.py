import pandas as pd

def generate_summary(df: pd.DataFrame) -> dict:
    return {
        "Total Orders": len(df),
        "Total Revenue": float(df["total_sales"].sum()),
        "Unique Regions": df["region"].nunique(),
        "Top Sales Rep": df["sales_rep"].value_counts().idxmax()
    }
    
def generate_ai_insights(df):
    if df.empty:
        return "No data available for insight generation."

    try:
        top_month = (
            df.groupby("Month")["total_sales"].sum()
            .sort_values(ascending=False)
            .index[0]
        )
        top_product = (
            df.groupby("product")["total_sales"].sum()
            .sort_values(ascending=False)
            .index[0]
        )
        top_region = (
            df.groupby("region")["total_sales"].sum()
            .sort_values(ascending=False)
            .index[0]
        )
        total_sales = df["total_sales"].sum()

        insight = (
            f"💡 Total sales for the selected period were ${total_sales:,.2f}. "
            f"Sales peaked in **{top_month}**. "
            f"The top-performing product was **{top_product}**, "
            f"and the **{top_region}** region generated the most revenue."
        )

        return insight

    except Exception as e:
        return f"Unable to generate insights: {e}"