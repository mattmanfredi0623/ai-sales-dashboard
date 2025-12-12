import pandas as pd
import streamlit as st
from core.data_loader import load_data
from core.insights import generate_summary, generate_ai_insights
from components.charts import plot_sales_forecast
from core.analysis import forecast_sales

st.set_page_config(page_title="Sales Dashboard", layout="wide")

def main():
    st.title("📊 AI-Powered Sales Dashboard")
    
    # Upload feature
    from utils.helper import auto_map_columns
    from config.settings import EXPECTED_COLUMNS

    upload_col, _ = st.columns([1, 3])
    with upload_col:
        uploaded_file = st.file_uploader("📤 Upload your sales data", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            df = auto_map_columns(df, EXPECTED_COLUMNS)
        except Exception as e:
            st.error(f"Error processing uploaded file: {e}")
            st.stop()
    else:
        df = load_data()

    if df is not None:
        # Show summary insights
        st.subheader("Summary Insights")
        summary = generate_summary(df)
        
        # Month Filter (Checkboxes)
        st.sidebar.subheader("📅 Filter by Month")

        # Fixed month order
        all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        # Create checkboxes in 3 columns
        selected_months = []
        month_cols = st.sidebar.columns(3)

        for idx, month in enumerate(all_months):
            col = month_cols[idx % 3]
            if col.checkbox(month, value=True):
                selected_months.append(month)

        # Apply month filter
        df = df[df["Month"].isin(selected_months)]


        # Region Filter (Checkboxes)
        st.sidebar.subheader("🌍 Filter by Region")

        # Sorted list of unique regions
        all_regions = sorted(df["region"].dropna().unique())

        # Create checkboxes in 2 columns
        selected_regions = []
        region_cols = st.sidebar.columns(2)

        for idx, region in enumerate(all_regions):
            col = region_cols[idx % 2]
            if col.checkbox(region, value=True):
                selected_regions.append(region)

        # Apply region filter
        df = df[df["region"].isin(selected_regions)]

        # Generate insights and charts below...
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Orders", summary["Total Orders"])
        col2.metric("Total Revenue", f"${summary['Total Revenue']:,.2f}")
        col3.metric("Regions", summary["Unique Regions"])
        col4.metric("Top Sales Rep", summary["Top Sales Rep"])
        
        # AI-style summary insight
        st.subheader("🧠 AI Insight Summary")

        col1, _ = st.columns([2, 5])  # Left column 2/7 width, right column unused
        with col1:
            with st.expander("AI Insight", expanded=True):
                st.markdown(generate_ai_insights(df))

        # Show chart
        from components.charts import (
            bar_chart_sales_by_region,
            pie_chart_sales_by_region,
            line_chart_sales_over_time
        )

        # Chart selector
        col1, _ = st.columns([1, 3])
        with col1:
            chart_type = st.selectbox(
                "Select chart type:",
                ("Bar", "Pie", "Line")
            )

        # Show chart based on selection
        if chart_type == "Bar":
            fig = bar_chart_sales_by_region(df)
        elif chart_type == "Pie":
            fig = pie_chart_sales_by_region(df)
        elif chart_type == "Line":
            fig = line_chart_sales_over_time(df)

        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("📅 Forecast: Next 30 Days of Sales")

        forecast_df = forecast_sales(df)

        if not forecast_df.empty:
            fig = plot_sales_forecast(forecast_df)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Not enough data to generate forecast.")
        
    else:
        st.warning("No data available.")

if __name__ == "__main__":
    main()