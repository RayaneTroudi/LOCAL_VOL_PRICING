from VolSmile import VolSmile
from MarketData import MarketData
from MarketDataGenerator import MarketDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from LocalVolSurface import LocalVolSurface
from DupireCalibrator import DupireCalibrator
from DupireModel import DupireModel
from EuropeanCall import EuropeanCall
from BlackShcolesModel import BlackScholesModel

# model parameters
r = 0.02
sigma = 0.2
T = 5 / 12
K = 100
S0 = 100
call_eu = EuropeanCall(S0, K, T)

# smile computing (generated)
array_K = [80, 100, 120]
array_sigma = [0.25, 0.20, 0.25]
vol_smile_data = VolSmile(array_K, array_sigma)

# generator of market data with smile vol
array_K_generator = np.arange(80, 120, 1)   # strikes
array_T_generator = np.array([1, 2, 3, 4, 5]) / 12   # maturities in years

engine_generator = MarketDataGenerator(S0, r, array_K_generator, array_T_generator, vol_smile_data)
market_data = engine_generator.GenerateData()
market_data.PrintMarketData()

# BS MODEL
model_BS = BlackScholesModel(r, sigma)
price_BS = model_BS.price(call_eu)

# DUPIRE MODEL
dupire_calibrator = DupireCalibrator(market_data, vol_smile_data)
vol_surface = dupire_calibrator.ComputeLocalVolSurface()
model_Dupire = DupireModel(r, vol_surface, S_min=80, S_max=120, dS=1, dt=0.01)
price_Dupire = model_Dupire.ComputePriceOption(call_eu)

# single price
print("BS =\n", price_BS)
print("Dupire =", price_Dupire)

# =========================
# COMPARISON GRAPH
# =========================

# choose maturity index corresponding to T = 5/12
i_T = np.where(np.isclose(array_T_generator, T))[0][0]

K_plot = array_K_generator
market_prices = market_data.grid_price[i_T, :]

bs_prices = []
dupire_prices = []

for K_val in K_plot:
    option = EuropeanCall(S0, K_val, T)

    # BS benchmark with constant vol
    bs_price = model_BS.price(option)
    bs_prices.append(bs_price)

    # Dupire price
    dupire_price = model_Dupire.ComputePriceOption(option)
    dupire_prices.append(dupire_price)

bs_prices = np.array(bs_prices)
dupire_prices = np.array(dupire_prices)

# plot
plt.figure(figsize=(10, 6))
plt.plot(K_plot, market_prices, label="Market price", linewidth=2)
plt.plot(K_plot, bs_prices, label="Black-Scholes (sigma=20%)", linestyle="--", linewidth=2)
plt.plot(K_plot, dupire_prices, label="Dupire price", linestyle="-.", linewidth=2)

plt.title(f"Call Price Comparison at T = {T:.2f} year")
plt.xlabel("Strike K")
plt.ylabel("Call Price")
plt.legend()
plt.grid(True)
plt.show()