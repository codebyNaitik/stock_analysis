import numpy as np

prices = np.loadtxt("simulated_stock_prices.csv" , delimiter= ",")

daily_returns = (prices[:,1:]-prices[:,:-1])/prices[:,:-1]
daily_returns = np.round(daily_returns,4)
# print(daily_returns)

volatility = np.std(daily_returns , axis= 1)
#print(volatility)

total_return = prices [:,-1] / prices [:,0]
#print(total_return)

best_idx = np.argmax(total_return)
print(f"Best performer: Company {best_idx + 1}")
print(f"Total Return: {total_return[best_idx]:.2f}")
print(f"Volatility: {volatility[best_idx]:.4f}")


correlation_matrix = np.corrcoef(daily_returns)
print("\nCorrelation Matrix:\n", np.round(correlation_matrix, 2))

