import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def display_chart(data: pd.DataFrame, column: str, ylabel: str,color="purple") -> None:
    fig, ax = plt.subplots()
    ax.plot(data.index, data[column], color=color, label=column)
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    ax.set_ylabel(ylabel)
    plt.legend()
    plt.show()


def display_results(
    portfolio_return: np.float64,
    portfolio_covariance : np.float64,
    portfolio_variance: np.float64,
    portfolio_standard_dev: np.float64,
) -> None:
    print(f"Portfolio return={str(np.round(portfolio_return, 4) * 100)}%")
    print(f"Covariance={str(np.round(portfolio_covariance, 4) * 100)}%")
    print(f"Variance={str(np.round(portfolio_variance, 4) * 100)}%")
    print(f"Portfolio volatility={str(np.round(portfolio_standard_dev, 4) * 100)}%")

