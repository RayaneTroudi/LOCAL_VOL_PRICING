import EuropeanCall
import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    
    def __init__(self, r, sigma):
        self.r = r 
        self.sigma = sigma
        
    def _getd1(self, call_option:EuropeanCall) -> float:
        S0 = call_option._getS0()
        K = call_option._getK()
        T = call_option._getT()
        
        return (
            (np.log(S0/K) + 
            (self.r + 0.5*self.sigma**2)*T)
            / (self.sigma*np.sqrt(T))
        )
        
    def _getd2(self,call_option:EuropeanCall) -> float:
        
        return (self._getd1(call_option) - self.sigma*np.sqrt(self.T))
    
        
