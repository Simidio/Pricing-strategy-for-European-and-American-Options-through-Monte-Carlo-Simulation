import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

time = 50
strike = 200
simulations = 100000

prices = yf.download("AAPL", start="2009-01-01")["Adj Close"]
startPrice = prices.iloc[-1]
log_returns = np.log(prices / prices.shift(1))

# European option
forecasted_prices = np.zeros((time + 1, simulations))
forecasted_prices[0] = np.ones((simulations)) * startPrice

for i in range(1, time + 1):
    random_index = np.random.randint(0, len(log_returns), simulations)
    random_log_returns = log_returns[random_index]
    forecasted_prices[i] = forecasted_prices[i - 1] * np.exp(np.array(random_log_returns))

forecasted_prices = pd.DataFrame(forecasted_prices)

# Plotting the first 100 simulated future price scenarios
plt.figure(figsize=(12, 6))
for i in range(100):
    plt.plot(forecasted_prices.iloc[:, i])
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Simulated Future Prices")
plt.show()

final_prices = forecasted_prices.loc[time]
gain_put = strike - final_prices  # for a put option
gain_call = final_prices - strike  # for a call option

# Setting negative gains to zero
gain_put[gain_put < 0] = 0
gain_call[gain_call < 0] = 0

# Calculating the mean gains for put and call options
mean_gain_put = gain_put.mean()
mean_gain_call = gain_call.mean()

# Calculating the probabilities of getting a zero gain for put and call options
prob_zero_gain_put = (gain_put == 0).sum() / simulations * 100
prob_zero_gain_call = (gain_call == 0).sum() / simulations * 100

# Histograms of gains for put and call options
plt.figure(figsize=(12, 6))
plt.hist(gain_put, bins=50, alpha=0.5, label="Put")
plt.hist(gain_call, bins=50, alpha=0.5, label="Call")
plt.xlabel("Gain")
plt.ylabel("Frequency")
plt.title("Histograms of Option Gains")
plt.legend()
plt.show()

# American option
forecasted_prices = np.zeros((time + 1, simulations))
forecasted_prices[0] = np.ones((simulations)) * startPrice

for i in range(1, time + 1):
    random_index = np.random.randint(0, len(log_returns), simulations)
    random_log_returns = log_returns[random_index]
    forecasted_prices[i] = forecasted_prices[i - 1] * np.exp(np.array(random_log_returns))

forecasted_prices = pd.DataFrame(forecasted_prices)

min_prices = forecasted_prices.min()
max_prices = forecasted_prices.max()

gain_put = strike - min_prices  # for a put option
gain_call = max_prices - strike  # for a call option

# Setting negative gains to zero
gain_put[gain_put < 0] = 0
gain_call[gain_call < 0] = 0

# Calculating the mean gains for put and call options
mean_gain_put = gain_put.mean()
mean_gain_call = gain_call.mean()

# Histograms of gains for put and call options
plt.figure(figsize=(12, 6))
plt.hist(gain_put, bins=50, alpha=0.5, label="Put")
plt.hist(gain_call, bins=50, alpha=0.5, label="Call")
plt.xlabel("Gain")
plt.ylabel("Frequency")
plt.title("Histograms of Option Gains")
plt.legend()
plt.show()

# Sorted plots of gains for put and call options
sorted_gain_put = np.sort(gain_put)[::-1]
sorted_gain_call = np.sort(gain_call)[::-1]

plt.figure(figsize=(12, 6))
plt.plot(sorted_gain_put, label="Put")
plt.plot(sorted_gain_call, label="Call")
plt.xlabel("Rank")
plt.ylabel("Gain")
plt.title("Sorted Option Gains")
plt.legend()
plt.show()
