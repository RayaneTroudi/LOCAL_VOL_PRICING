# 📈 Local Volatility Modeling & Option Pricing (Dupire)

This project implements a **local volatility model** to price European options starting from an implied volatility smile.

## 🚀 Overview

The pipeline follows these steps:

1. **Market Data Generation**  
   Synthetic option prices are generated using a volatility smile `σ_imp(K)` and the Black-Scholes model  

2. **Dupire Calibration**  
   A local volatility surface `σ_loc(K, T)` is recovered from option prices using Dupire’s formula:  
   σ_loc²(K,T) = (∂C/∂T + r K ∂C/∂K) / (0.5 K² ∂²C/∂K²)

3. **Surface Construction**  
   The surface `σ_loc(K, T)` is interpolated to obtain a continuous function `σ_loc(S, t)`  

4. **Option Pricing**  
   European options are priced by solving the PDE:  
   ∂C/∂t + 0.5 σ_loc²(S,t) S² ∂²C/∂S² + r S ∂C/∂S − r C = 0

## 📊 Outputs

- Price comparison: Market vs Black-Scholes vs Dupire  
- Implied volatility smile `σ_imp(K)`  
- Local volatility surface `σ_loc(K, T)`  

## 🧠 Key Insight

The model reproduces the volatility smile by construction and ensures consistent pricing across strikes and maturities.

## 🛠️ Tech Stack

- Python  
- NumPy / SciPy  
- Matplotlib  

## ▶️ Usage

```bash
python main.py
