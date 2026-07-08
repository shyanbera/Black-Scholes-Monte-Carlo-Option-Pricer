import numpy as np

# this function calculates the fair price of a European call option under Black-Scholes framework assumptions

def monte_carlo_option_pricer(S_0, r, sigma, T, K, num_simulations):
    Z = np.random.standard_normal(num_simulations)
    S_T = S_0 * np.exp((r-(sigma**2)/2)*T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(S_T-K, 0)
    expected_option_value = np.exp(-r*T) * np.mean(payoff)
    return(expected_option_value)

print(monte_carlo_option_pricer(100,0.05,1,20,100,1000000))
      

