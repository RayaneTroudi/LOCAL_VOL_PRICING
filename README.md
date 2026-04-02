# 📈 Local Volatility Pricing with Dupire (Python)

## 📌 Overview

This project implements a **Local Volatility model** using the Dupire equation to price European options consistently with a volatility smile.

The pipeline starts from **synthetic market data (implied volatility smile)** and builds a **local volatility surface**, which is then used to price options via a **finite difference PDE solver**.

---

## 🧠 Key Concepts

### Implied Volatility
Market-observed volatility depending on strike and maturity:
\[
\sigma_{imp}(K, T)
\]

### Local Volatility
A deterministic function used in a diffusion model:
\[
\sigma_{loc}(S, t)
\]

### Goal
Recover a model that reproduces **all market option prices consistently**

---

## ⚙️ Methodology

### 1. Market Data Generation

- Generate synthetic option prices using a volatility smile  
- Pricing via Black-Scholes

```python
σ(K) → C(K,T)
