from model import (
    portfolio_return,
    portfolio_cumulative_returns,
    portfolio_covariance,
    portfolio_standard_dev, portfolio_variance, portfolio_cumulative_returns_rolling_30)

from repository import get_weights, get_data

from view import display_chart, display_results

data = get_data()
weights = get_weights()

daily_cum_ret = portfolio_cumulative_returns(weights, data)
asset_returns = portfolio_return(weights, data)
covariance = portfolio_covariance(weights, data)
variance = portfolio_variance(weights, data)
volatility = portfolio_standard_dev(weights, data)

returns_windowed = portfolio_cumulative_returns_rolling_30(weights, data)

display_results(asset_returns, covariance, variance, volatility)

display_chart(daily_cum_ret, "Portfolio", "Daily Return, %")
display_chart(returns_windowed, "Portfolio", "Annualized Volatility, 30-day Window")

