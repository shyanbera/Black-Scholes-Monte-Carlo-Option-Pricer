# Monte Carlo Simulation Options Pricer

The goal of this project is to use a Monte Carlo simulation to determine the fair price of a European call option under Black-Scholes framework assumptions. We are assuming the market to be perfectly liquid, meaning that there is no bid-ask spread or transaction costs which would significantly cut into profits. Also, we assume constant volatility which is unlikely in practice.

I intend on adding further sections to be able to visualise the results and plot the convergence, calculate the greeks, implement variance reduction techniques and hopefully use some real market data to calculate the parameters for the option pricer function.

With regards to the mathematics behind these models, after taking 'Stochastic Financial Models' in Part II of the Mathematical Tripos, I intend to go back and learn the rigorous derivation for modelling the stock price with GBM and solving the SDE. However, I am currently in a position to understand how we obtain the analytical formula for the call option's value if we accept the formula for terminal stock price:

$$S_T = S_0 \exp\left( \left(r - \frac{\sigma^2}{2}\right)T + \sigma \sqrt{T} Z \right)$$

For this derivation please refer to MATHEMATICS.md
