from LocalVolSurface import LocalVolSurface
from EuropeanCall import EuropeanCall
import numpy as np


class DupireModel:
    
    def __init__(self, r, local_vol_surface: LocalVolSurface,
                 S_min=50, S_max=150, dS=1, dt=0.01):
        self.r = r
        self.local_vol_surface = local_vol_surface
        self.S_min = S_min
        self.S_max = S_max
        self.dS = dS
        self.dt = dt
            
    def ComputePriceOption(self, option: EuropeanCall) -> float:
        
        S_grid = np.arange(self.S_min, self.S_max + self.dS, self.dS)
        T_grid = np.arange(0, option.T + self.dt, self.dt)
        
        C = np.maximum(S_grid - option.K, 0)
        
        for t in reversed(T_grid[:-1]):
            sigma = np.array([
                float(self.local_vol_surface.interpolate(S, t)) 
                for S in S_grid
            ])
            
            a = 0.5 * self.dt * (
                self.r * S_grid / self.dS
                - sigma**2 * S_grid**2 / self.dS**2
            )
            b = 1 + self.dt * (
                sigma**2 * S_grid**2 / self.dS**2 + self.r
            )
            c = -0.5 * self.dt * (
                self.r * S_grid / self.dS
                + sigma**2 * S_grid**2 / self.dS**2
            )
            
            A = np.diag(b) + np.diag(a[1:], -1) + np.diag(c[:-1], 1)
            
            A[0, :] = 0
            A[0, 0] = 1
            
            A[-1, :] = 0
            A[-1, -1] = 1
            
            rhs = C.copy()
            rhs[0] = 0

            tau = option.T - t
            rhs[-1] = S_grid[-1] - option.K * np.exp(-self.r * tau)
            
            C = np.linalg.solve(A, rhs)
        
        return float(np.interp(option.S0, S_grid, C))