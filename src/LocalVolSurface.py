import matplotlib.pyplot as plt
import numpy as np

class LocalVolSurface:
    
    def __init__(self, array_K, array_T, grid_vol_loc):
        self.array_K = array_K
        self.array_T = array_T
        self.grid_vol_loc = grid_vol_loc
    
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