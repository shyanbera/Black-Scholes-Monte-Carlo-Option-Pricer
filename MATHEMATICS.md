
## Deriving Analytical Solution:

To determine the fair price of the call option, we find the expected value of the payoff, discounted back to today:

$$C = e^{-rT} \mathbb{E}[\max(S_T - K, 0)]$$

We assume the underlying asset is modeled :

$$S_T = S_0 \exp\left( \left(r - \frac{\sigma^2}{2}\right)T + \sigma \sqrt{T} Z \right)$$

Where $Z \sim \mathcal{N}(0,1)$, with the Probability Density Function (PDF):

$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}$$

(The understanding for this requires me to take Stochastic Financial Models in my last year of uni studies)

To find the expectation we consider only where $S_T$ > K and find the critical value where:

$$S_0 \exp\left( \left(r - \frac{\sigma^2}{2}\right)T + \sigma \sqrt{T} Z \right) = K$$

Taking the natural logarithm and solving for $Z$:

$$Z = \frac{\ln\left(\frac{K}{S_0}\right) - \left(r - \frac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}$$

We define this critical boundary as $-d_2$. Hence

$$C = e^{-rT} \int_{-d_2}^{\infty} (S_T - K) \phi(z) dz$$


Split the integral:

$$C = \underbrace{e^{-rT} \int_{-d_2}^{\infty} S_T \phi(z) dz}_{\text{Part A}} - \underbrace{K e^{-rT} \int_{-d_2}^{\infty} \phi(z) dz}_{\text{Part B}}$$

### Evaluating Part B:


$$\text{Part B} = K e^{-rT} \int_{-d_2}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}} dz$$



$$ = K e^{-rT} N(d_2)$$

### Evaluating Part A:


$$\text{Part A} = e^{-rT} \int_{-d_2}^{\infty} \left[ S_0 e^{(r - \frac{\sigma^2}{2})T + \sigma \sqrt{T} z} \right] \left[ \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}} \right] dz$$

simplifying:

$$\text{Part A} = S_0 e^{-\frac{\sigma^2}{2}T} \int_{-d_2}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}{2}(z^2 - 2\sigma \sqrt{T} z) \right) dz$$


$$= S_0 e^{-\frac{\sigma^2}{2}T} \int_{-d_2}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}{2}(z - \sigma\sqrt{T})^2 \right) \exp\left( \frac{\sigma^2}{2}T \right) dz$$

leaving:

$$\text{Part A} = S_0 \int_{-d_2}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}{2}(z - \sigma\sqrt{T})^2 \right) dz$$

Finally, we apply the substitution $u = z - \sigma\sqrt{T}$ (where $du = dz$). The lower bound shifts to $u_{\text{lower}} = -d_2 - \sigma\sqrt{T}$. Defining $d_1 = d_2 + \sigma\sqrt{T}$, the new lower bound becomes $-d_1$.

$$\text{Part A} = S_0 \int_{-d_1}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}} du$$

By standard normal symmetry, this evaluates to:

$$\text{Part A} = S_0 N(d_1)$$

## 4. The Final Analytical Solution

Combining Part A and Part B yields the closed-form Black-Scholes-Merton equation for a European Call Option:

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

