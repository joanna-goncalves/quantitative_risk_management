from model import (
    portfolio_return,
    portfolio_cumulative_returns,
    portfolio_covariance,
    portfolio_standard_dev)

from repository import get_weights, get_data

from view import display_chart, display_results

data = get_data()
weights = get_weights()

portfolio_returns = portfolio_return(weights, data)

