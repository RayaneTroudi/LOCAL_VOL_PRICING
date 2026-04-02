# 📈 Local Volatility Modeling & Option Pricing (Dupire)

This project implements a **local volatility model** to price European options starting from an implied volatility smile.

## 🚀 Overview

The pipeline follows these steps:

1. **Market Data Generation**  
   Synthetic option prices are generated using a volatility smile $\sigma_{imp}(K)$ and the Black-Scholes model  

2. **Dupire Calibration**  
   A local volatility surface $\sigma_{loc}(K, T)$ is recovered from option prices using Dupire’s formula:
   $$
   \sigma_{loc}^2(K,T) = \frac{\partial C / \partial T + rK \, \partial C / \partial K}{\tfrac{1}{2} K^2 \, \partial^2 C / \partial K^2}
   $$

3. **Surface Construction**  
   The surface $\sigma_{loc}(K, T)$ is interpolated to obtain a continuous function $\sigma_{loc}(S, t)$  

4. **Option Pricing**  
   European options are priced by solving the PDE:
   $$
   \frac{\partial C}{\partial t} + \frac{1}{2} \sigma_{loc}^2(S,t) S^2 \frac{\partial^2 C}{\partial S^2} + r S \frac{\partial C}{\partial S} - r C = 0
   $$

## 📊 Outputs

- Price comparison: Market vs Black-Scholes vs Dupire  
- Implied volatility smile $\sigma_{imp}(K)$  
- Local volatility surface $\sigma_{loc}(K, T)$  

## 🧠 Key Insight

The model reproduces the volatility smile by construction and ensures consistent pricing across strikes and maturities.

## 🛠️ Tech Stack

- Python  
- NumPy / SciPy  
- Matplotlib  

## ▶️ Usage

Run the main script:

```bash
python main.py
