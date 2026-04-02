from scipy import interpolate

class VolSmile():
    
    def __init__(self,array_K,array_sigma):
        
        self.array_K = array_K
        self.array_sigma = array_sigma
         
    def interpolFunctionSmile(self,method:bool):
        
        # 0 : lagrange
        # 1 : cubic spline
        
        if (method == 0):
            return interpolate.lagrange(self.array_K, self.array_sigma)
        elif (method==1):
            return interpolate.CubicSpline(self.array, self.array_sigma)
        else:
            ValueError("Method selected is not existing.")