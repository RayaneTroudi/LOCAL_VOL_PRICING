from BlackShcolesModel import BlackScholesModel
from EuropeanCall import EuropeanCall

# model parameters
r = 0.02
sigma = 0.2
T = 1
K = 100
S = 90

# smile computing
array_K = [80,100,120]
array_sigma = [0.25,0.20,0.25]

# computing vol smile

# computing price
call = EuropeanCall(S,K,T)
BS_model = BlackScholesModel(r,sigma)
d1 = BS_model.d1(call)
price = BS_model.price(call)
print(price)