import pandas as pd

def format_currency(value, symbol="$"):
    return f"{symbol}{value:,.2f}"

def auto_map_columns(df, expected_map: dict) -> pd.DataFrame:
    mapped_cols = {}
    for expected_col, aliases in expected_map.items():
        for alias in aliases:
            if alias in df.columns:
                mapped_cols[alias] = expected_col
                break
    df = df.rename(columns=mapped_cols)

    missing = [col for col in expected_map if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    
    return df