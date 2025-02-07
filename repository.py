import pandas as pd
import numpy as np

portfolio = {"Citi": 0.25, "MS": 0.25, "GS": 0.25, "JPM": 0.25}
begin_date = "2008-01-01"
end_date = "2009-12-31"

def get_data():
    return pd.read_csv(
        r"input\crisis_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


def get_weights() -> np.array:
    return np.array(list(portfolio.values()))



