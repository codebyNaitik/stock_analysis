import numpy as np


n_company=10
start = 34
steps=100
mean = 0.002
std = 0.02

returns = np.random.normal(mean,std,(n_company,steps-1))

prices = np.empty((n_company,steps))
prices [:,0]= start

for i in range(1,steps):
    prices[:,i] = prices[:,i-1] * (1 + returns[:,i-1])

prices = np.round(prices,2)

np.savetxt("simulated_stock_prices.csv",prices,delimiter="," , fmt= "%.2f")
