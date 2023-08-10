# Option Pricing Models
the pricing model used for the options is Monte Carlo simulation, which belongs to the class of numerical (non-analytical) models.

* **Numerical Models**
Monte Carlo Simulation: Generates random stock price paths and discounted payoffs. Allows flexibility in modeling stochastic processes and payoff functions.

# Pricing-strategy-for-European-and-American-Options-through-Monte-Carlo-Simulation
The code first simulates future price paths for the underlying asset (AAPL stock) using Monte Carlo simulation. It starts with the current price, then randomly samples from historical log returns to generate possible future price movements.

* For a **European option**, it calculates the payoff at expiration across all simulated paths. The option value is the average discounted payoff. Here it plots simulated paths and histograms of gains from put and call options.

* For an **American option**, it tracks the minimum and maximum price on each path before expiration. The payoff is based on the earliest optimal exercise point, not necessarily at expiration. It compares the payoff from immediate exercise to holding the option.

The key differences from a European option:

* It looks for optimal early exercise along each path, not just at expiration
* The payoff distribution has higher values due to early exercise
* The put option value converges to the strike price as time passes

Monte Carlo simulation provides a flexible way to model complex American option payoffs based on simulated paths and optimal early exercise logic. It is more computationally intensive than valuing European options, but can handle path-dependent behavior.
