# Monte Carlo Simulation Options Pricer with Variance Reduction

The goal of this project was to use a Monte Carlo simulation to determine the fair price of a European call option under Black-Scholes framework assumptions.

## Key Results

This log-log graph (with gradient 1/2) confirms the $\mathcal{O}(N^{-1/2})$ convergence behaviour of the Monte Carlo algorithm and the decreasing y-intercepts show the effectiveness of the variance reduction techniques.

!!!!! Remember to put some kind of statistic here as a hook :)))) come back to this at the end when you've understood everything

![Log-Log Convergence Plot](convergence_graph.png)

---
### Results Table:

Analytical Price: £10.45

[//]: # (START_TABLE)

| Paths (N) | Naive SE | Antithetic SE | Control SE |
|---|---|---|---|
| 100 | 1.5009 | 1.0115 | 0.5984 |
| 1,000 | 0.5103 | 0.3007 | 0.1646 |
| 10,000 | 0.1617 | 0.0955 | 0.0561 |
| 100,000 | 0.0429 | 0.0321 | 0.0184 |
| 1,000,000 | 0.0154 | 0.0102 | 0.0059 |

[//]: # (END_TABLE)

## Mathematical Framework:
The goal of this section is to explore as much of the theory/underlying mathematics behind this project, accessible at a level of having taken Part 1A Probability.

### Chapter 1: Black Box Assumptions

We assume the underlying asset follows Geometric Brownian Motion and behaves via the following Stochastic Differential Equation:
 
$$ dS_t = rS_tdt + \sigma S_t dW_t$$

Solving this yields the formula for the stock price at time T:

$$ S_T = S_0 \exp \left( \left(r-\frac{1}{2} \sigma ^2 \right)T + \sigma \sqrt{T} Z \right) $$

I am not currently equipped to understand the rigorous derivation behind this formula, but intend to revisit and update this page after taking Stochastic Financial Models in Part II of the Mathematical Tripos. For now we shall treat it as a magic formula.

We note that this formula uses the term r instead of $\mu$. Roughly speaking, the intuition is that we can create a risk-free portfoilo by delta hedging the call option with the underlying stock. This is thus guaranteed to grow at the risk-free interest rate r meaning that the call option's present value is independent of $\mu$.

### Chapter 2: Monte Carlo Simulation

For a strike price $K$ and stock price after T years $S_T$ the payoff of the call option is given by $\max \left(S_T - K, 0 \right)$ and the fair discounted value of the option is given by $e^{-rT} \mathbb{E}(\max(S_T-K,0))$

We simulate the stock price using NumPy for different numbers of paths and calculate this value computationally.

### Chapter 3: Compare against analytical solution

We note that we can calculate the fair option price analytically by explicitly calculating the expectation. I have detailed the calculations in MATHEMATICS.md and this serves as a ground truth for comparison against our Monte Carlo Simulation

### Chapter 4: Variance Reduction Techniques

The first technqiue used is antithetic variates. Here, we simulate half the number of paths for our normal distribution and then negate the values and combine the lists to create Z. This reduces the variance by ensuring that our sample normal distribution is indeed perfectly centered at zero.

The other variance reduction technique used is control variates. I have also detailed the math for this in the MATHEMATICS.md file.

From the end of that section we note $\text{Var}(Y_{CV}) = \text{Var}(Y_{MC}) (1-\rho^2)$ where $\rho$ (the correlation) is given by $$\rho = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}$$

### Chapter 5: Convergence Test Results

By the Central Limit Theorem, we know that the theoretical standard error of the Monte Carlo algorithm scales with the inverse square root of N: (where $\sigma$ is the standard deviation of one path)

$$SE = \frac{\sigma}{\sqrt{N}}$$

Taking logs we obtain:
$$\log(SE) = -0.5\log(N) +\log(\sigma)$$
which is why plotting on a log-log graph yiels a straight line.

We observe that the gradients produced were very close to 0.5, confirming the $\mathcal{O}(N^{-1/2})$ convergence behaviour.

We calculated $\rho$ as ...


