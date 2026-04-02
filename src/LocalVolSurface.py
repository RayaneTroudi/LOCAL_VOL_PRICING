import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import RegularGridInterpolator


class LocalVolSurface:
    
    def __init__(self, array_K, array_T, grid_vol_loc):
        self.array_K = np.array(array_K, dtype=float)
        self.array_T = np.array(array_T, dtype=float)
        self.grid_vol_loc = np.array(grid_vol_loc, dtype=float)

        self.interpolator = RegularGridInterpolator(
            (self.array_T, self.array_K),
            self.grid_vol_loc,
            method='linear',
            bounds_error=False,
            fill_value=None
        )
    
    def PrintLocalVolSurface(self):
        K_grid, T_grid = np.meshgrid(self.array_K, self.array_T)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(K_grid, T_grid, self.grid_vol_loc, cmap='viridis')
        
        ax.set_xlabel('Strike K')
        ax.set_ylabel('Maturity T')
        ax.set_zlabel('Local Vol σ(K,T)')
        ax.set_title('Local Volatility Surface')
        
        plt.show()
        
    def interpolate(self, S, t):
        return float(self.interpolator([[t, S]])[0])