from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

class VolSmile():
    
    def __init__(self,array_K,array_sigma):
        
        self.array_K = array_K
        self.array_sigma = array_sigma
         
    def SmileFunction(self,method:bool):
        
        # 0 : lagrange
        # 1 : cubic spline
        
        if (method == 0):
            return interpolate.lagrange(self.array_K, self.array_sigma)
        elif (method==1):
            return interpolate.CubicSpline(self.array_K, self.array_sigma)
        else:
            raise ValueError("Method selected is not existing.")
            
            
            
    def PrintVolSmileFunction(self,method:bool):
        
        # init the interpolation function
        smile_function = self.SmileFunction(method)
        
        # init the abscisse grid
        K_init = self.array_K[0]
        K_final = self.array_K[-1]
        step = 1
        size = (K_final - K_init + step) / step
        
        K_interpol = np.arange(K_init,K_final,step)
        sigma_interpol = smile_function(K_interpol)
        
        plt.title("Volatility Smile")
        plt.xlabel("K ($)")
        plt.ylabel("Vol (%)")
        plt.xlim(0, self.array_K[-1]+10)
        plt.ylim(0, sigma_interpol[-1]+0.10)
        plt.plot(K_interpol,sigma_interpol)
        plt.show()
