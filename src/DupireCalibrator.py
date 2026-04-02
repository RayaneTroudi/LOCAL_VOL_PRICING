from MarketData import MarketData
from VolSmile import VolSmile
from LocalVolSurface import LocalVolSurface
import numpy as np

class DupireCalibrator():
    
    def __init__(self, market_data:MarketData, vol_smile:VolSmile):
        self.market_data = market_data
        self.vol_smile = vol_smile
    
        
    def ComputeLocalVolSurface(self) -> LocalVolSurface:
        
        grid = self.market_data.grid_price
        array_K = self.market_data.array_K
        array_T = self.market_data.array_T
        r = self.market_data.r
        
        sigma_grid = np.zeros((len(array_T), len(array_K)))
        
        for i, T in enumerate(array_T):
            for j, K in enumerate(array_K):
                
                # gestion des bords pour T (pas de i+1 au dernier point)
                if i < len(array_T) - 1:
                    dC_dT = (grid[i+1, j] - grid[i, j]) / (array_T[i+1] - array_T[i])
                else:
                    dC_dT = (grid[i, j] - grid[i-1, j]) / (array_T[i] - array_T[i-1])
                
                # gestion des bords pour K (différence centrée sauf aux extrémités)
                if j == 0:
                    dC_dK = (grid[i, j+1] - grid[i, j]) / (array_K[j+1] - array_K[j])
                    d2C_dK2 = (grid[i, j+2] - 2*grid[i, j+1] + grid[i, j]) / (array_K[j+1] - array_K[j])**2
                elif j == len(array_K) - 1:
                    dC_dK = (grid[i, j] - grid[i, j-1]) / (array_K[j] - array_K[j-1])
                    d2C_dK2 = (grid[i, j] - 2*grid[i, j-1] + grid[i, j-2]) / (array_K[j] - array_K[j-1])**2
                else:
                    dC_dK = (grid[i, j+1] - grid[i, j-1]) / (array_K[j+1] - array_K[j-1])
                    d2C_dK2 = (grid[i, j+1] - 2*grid[i, j] + grid[i, j-1]) / (array_K[j+1] - array_K[j])**2
                
                # formule de Dupire
                num = dC_dT + r * K * dC_dK
                den = 0.5 * K**2 * d2C_dK2
                
                # protection division par zéro
                if den < 1e-10:
                    sigma_grid[i, j] = 0.0
                else:
                    sigma_grid[i, j] = np.sqrt(max(num / den, 0))
        
        return LocalVolSurface(array_K, array_T, sigma_grid)
            
        
    