import scipy.stats as si
import numpy as np

def d1(S, K, T, r, sigma):
    D1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return D1

def d2(S, K, T, r, sigma):
    dd1 = d1(S, K, T, r, sigma)
    D2 = dd1 - sigma * np.sqrt(T)
    return D2

def black_scholes(S, K, T, r, sigma, option_type='call'):
    if option_type == 'call':
        option_price = (S * si.norm.cdf(d1(S, K, T, r, sigma), 0.0, 1.0)) - (K * np.exp(-r * T) * si.norm.cdf(d2(S, K, T, r, sigma), 0.0, 1.0))
    elif option_type == 'put':
        option_price = (K * np.exp(-r * T) * si.norm.cdf(-d2(S, K, T, r, sigma), 0.0, 1.0)) - (S * si.norm.cdf(-d1(S, K, T, r, sigma), 0.0, 1.0))
    return option_price

def calc_delta(S, K, T, r, sigma, option_type='call'):
    D1 = d1(S, K, T, r, sigma)
    if option_type == 'call':
        return si.norm.cdf(D1)
    elif option_type == 'put':
        return si.norm.cdf(D1) - 1

def calc_gamma(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return si.norm.pdf(D1) / (S * sigma * np.sqrt(T))

def calc_theta(S, K, T, r, sigma, option_type='call'):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    term1 = -(S * si.norm.pdf(D1) * sigma) / (2 * np.sqrt(T))
    
    if option_type == 'call':
        term2 = r * K * np.exp(-r * T) * si.norm.cdf(D2)
        return term1 - term2
    elif option_type == 'put':
        term2 = r * K * np.exp(-r * T) * si.norm.cdf(-D2)
        return term1 + term2

def calc_vega(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return S * si.norm.pdf(D1) * np.sqrt(T)
