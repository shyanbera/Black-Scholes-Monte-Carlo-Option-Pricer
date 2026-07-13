import numpy as np
import scipy.stats as stats

# this function calculates the fair price of a European call option under Black-Scholes framework assumptions

def monte_carlo_option_pricer(S_0, r, sigma, T, K, num_simulations):
    Z = np.random.standard_normal(num_simulations)
    S_T = S_0 * np.exp((r-(sigma**2)/2)*T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(S_T-K, 0)
    expected_option_value = np.exp(-r*T) * np.mean(payoff)
    return(expected_option_value)

def analytical_call_price(S_0, r, sigma, T, K):
    d_2 = - (np.log(K/S_0)-(r-0.5*(sigma**2))*T)/(sigma*np.sqrt(T))
    d_1 = d_2 + sigma*np.sqrt(T)
    fair_price = S_0*stats.norm.cdf(d_1) - K*np.exp(-r*T)*stats.norm.cdf(d_2)
    return fair_price

def monte_carlo_antithetic(S_0,r,sigma,T,K, num_simulations):
    Z_1 = np.random.standard_normal(num_simulations//2)
    Z_2 = - Z_1
    Z = np.concatenate((Z_1,Z_2))
    # literally copy pasting the next section of code from the original monte carlo pricer
    S_T = S_0 * np.exp((r-(sigma**2)/2)*T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(S_T-K, 0)
    expected_option_value = np.exp(-r*T) * np.mean(payoff)
    return(expected_option_value)

def monte_carlo_control(S_0,r,sigma,T,K,num_simulations):
    Z=np.random.standard_normal(num_simulations)
    S_T = S_0 * np.exp((r-(sigma**2)/2)*T + sigma*np.sqrt(T)*Z)
    discounted_payoffs = np.exp(-r*T) * np.maximum(S_T-K,0)
    covariance_matrix = np.cov(S_T,discounted_payoffs)
    covariance = covariance_matrix[1,0]
    c_star = covariance/np.var(S_T)
    Y_CV = discounted_payoffs - c_star * (S_T - S_0 * np.exp(r*T))
    return np.mean(Y_CV)

