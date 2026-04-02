from BlackShcolesModel import BlackScholesModel
from EuropeanCall import EuropeanCall

r = 0.02
sigma = 0.2
T = 1
K = 100
S = 90

call = EuropeanCall(S,K,T)
BS_model = BlackScholesModel(r,sigma)
d1 = BS_model.d1(call)
price = BS_model.price(call)
print(price)