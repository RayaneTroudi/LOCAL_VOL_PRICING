import numpy as np
from VolSmile import VolSmile
from EuropeanCall import EuropeanCall
from BlackShcolesModel import BlackScholesModel
from MarketData import MarketData
class MarketDataGenerator:
    
    def __init__(self,S0,r,array_K,array_T,smile:VolSmile):
        
        self.S0 = S0
        self.r = r
        self.array_K = array_K
        self.array_T = array_T
        self.smile = smile
        
    def GenerateData(self):
        
        smile_function = self.smile.SmileFunction(method=1)
        grid_price = np.zeros((len(self.array_T), len(self.array_K)))
        
        for i, T in enumerate(self.array_T):
            for j, K in enumerate(self.array_K):
                sigma_imp = smile_function(K)
                option = EuropeanCall(self.S0,K,T)
                bs_model = BlackScholesModel(self.r,sigma_imp)
                grid_price[i,j] = bs_model.price(option)
                
        return MarketData(self.S0,self.r,self.array_K,self.array_T,grid_price)