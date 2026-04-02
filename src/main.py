from VolSmile import VolSmile
from MarketData import MarketData
from MarketDataGenerator import MarketDataGenerator
import numpy as np

# model parameters
r = 0.02
sigma = 0.2
T = 1
K = 100
S0 = 90

# smile computing
array_K = [80,100,120]
array_sigma = [0.25,0.20,0.25]

# computing vol smile
vol_smile_data = VolSmile(array_K,array_sigma)

# computing option price with vol smile
array_K_generator = np.arange(80,120,10) # in $
array_T_generator = np.arange(1,6,1) # in months
engine_generator = MarketDataGenerator(S0,r,array_K_generator,array_T_generator,vol_smile_data)
MarketData = engine_generator.GenerateData()
MarketData.PrintMarketData()
