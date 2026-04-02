# container
class MarketData:
    
    def __init__(self, S0, r, array_K, array_T, grid_price):
        self.S0 = S0
        self.r = r
        self.array_K = array_K
        self.array_T = array_T
        self.grid_price = grid_price
        
    
    def PrintMarketData(self):
          
        for i, T in enumerate(self.array_T):
            for j, K in enumerate(self.array_K):
                price = self.grid_price[i, j]
                print(f"T={T}, K={K}, Price={price:.4f}")