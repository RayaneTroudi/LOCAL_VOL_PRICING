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
from mpl_toolkits.mplot3d import Axes3D  # nécessaire pour le plot 3D

# =========================
# MODEL PARAMETERS
# =========================
r = 0.02
sigma = 0.2
T = 5 / 12
K = 100
S0 = 100
call_eu = EuropeanCall(S0, K, T)

# =========================
# IMPLIED VOL SMILE
# =========================
array_K = [80, 100, 120]
array_sigma = [0.25, 0.20, 0.25]
vol_smile_data = VolSmile(array_K, array_sigma)

# =========================
# MARKET DATA GENERATION
# =========================
array_K_generator = np.arange(80, 120, 1)
array_T_generator = np.array([1, 2, 3, 4, 5]) / 12

engine_generator = MarketDataGenerator(S0, r, array_K_generator, array_T_generator, vol_smile_data)
market_data = engine_generator.GenerateData()

# =========================
# BLACK-SCHOLES MODEL
# =========================
model_BS = BlackScholesModel(r, sigma)
price_BS = model_BS.price(call_eu)

# =========================
# DUPIRE MODEL
# =========================
dupire_calibrator = DupireCalibrator(market_data, vol_smile_data)
vol_surface = dupire_calibrator.ComputeLocalVolSurface()
model_Dupire = DupireModel(r, vol_surface, S_min=80, S_max=120, dS=1, dt=0.01)
price_Dupire = model_Dupire.ComputePriceOption(call_eu)

print("BS =", price_BS)
print("Dupire =", price_Dupire)

# =========================
# PRICE COMPARISON
# =========================
i_T = np.where(np.isclose(array_T_generator, T))[0][0]

K_plot = array_K_generator
market_prices = market_data.grid_price[i_T, :]

bs_prices = []
dupire_prices = []

for K_val in K_plot:
    option = EuropeanCall(S0, K_val, T)

    bs_price = model_BS.price(option)
    bs_prices.append(bs_price)

    dupire_price = model_Dupire.ComputePriceOption(option)
    dupire_prices.append(dupire_price)

bs_prices = np.array(bs_prices)
dupire_prices = np.array(dupire_prices)

# =========================
# SMILE CURVE
# =========================
smile_function = vol_smile_data.SmileFunction(method=1)
K_smile = np.arange(array_K[0], array_K[-1] + 1, 1)
sigma_smile = smile_function(K_smile)

# =========================
# LOCAL VOL SURFACE
# =========================
K_surface, T_surface = np.meshgrid(vol_surface.array_K, vol_surface.array_T)
Z_surface = vol_surface.grid_vol_loc

# =========================
# SINGLE WINDOW WITH 3 PLOTS
# =========================
fig = plt.figure(figsize=(18, 5))

# --- 1) Price comparison
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(K_plot, market_prices, label="Market price", linewidth=2)
ax1.plot(K_plot, bs_prices, label="Black-Scholes", linestyle="--", linewidth=2)
ax1.plot(K_plot, dupire_prices, label="Dupire", linestyle="-.", linewidth=2)
ax1.set_title(f"Price Comparison (T = {T:.2f})")
ax1.set_xlabel("Strike K")
ax1.set_ylabel("Call Price")
ax1.grid(True)
ax1.legend()

# --- 2) Implied vol smile
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(K_smile, sigma_smile, linewidth=2, label="Interpolated smile")
ax2.scatter(array_K, array_sigma, label="Smile points")
ax2.set_title("Implied Volatility Smile")
ax2.set_xlabel("Strike K")
ax2.set_ylabel("Implied Volatility")
ax2.grid(True)
ax2.legend()

# --- 3) Local volatility surface
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.plot_surface(K_surface, T_surface, Z_surface, cmap='viridis')
ax3.set_title("Local Volatility Surface")
ax3.set_xlabel("Strike K")
ax3.set_ylabel("Maturity T")
ax3.set_zlabel("Local Vol")

plt.tight_layout()
plt.show()