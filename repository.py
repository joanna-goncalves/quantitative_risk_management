import pandas as pd
import numpy as np

portfolio = {"Citi": 0.25, "MS": 0.25, "GS": 0.25, "JPM": 0.25}


def get_data():
    df = pd.read_csv(
        r"input\crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )
    df = df.loc["2008-01-01":"2009-12-31"]
    return df


def get_weights() -> np.array:
    return np.array(list(portfolio.values()))



