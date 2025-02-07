from model import (
    portfolio_return,
    portfolio_cumulative_returns,
    portfolio_covariance,
    portfolio_standard_dev, portfolio_variance)

from repository import get_weights, get_data

from view import display_chart, display_results

data = get_data()
weights = get_weights()

asset_returns = portfolio_return(weights, data)
portfolio_returns = portfolio_cumulative_returns(weights, data)
covariance = portfolio_covariance(weights, data)
variance = portfolio_variance(weights, data)
volatility = portfolio_standard_dev(weights, data)

display_results(portfolio_returns, covariance, variance, volatility)


