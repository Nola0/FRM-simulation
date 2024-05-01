This is a financial risk management project focused on simulating arbitrage trading strategy by LTCM.

The group applied Monte Carlo Simulation to reproduce LTCM’s trading strategy. The method used for simulating correlated price series is Cholesky decomposition.

Assumptions
1. Prices of equity pairs are simulated assuming a normal return distribution per period.
This is an approximate illustration of LTCM’s bond arbitrage trades as bond returns are
shown to be asymmetric.5
2. We model the impact of Black Swan event as 1) an increase in correlation between
trade pairs as asset prices start to all move downwards 2) a decrease in correlation
within convergence trade pairs as the more liquid asset is traded more than the other 3)
An increase in SD of stock returns.
3. We assume a normal distribution of returns with mean return of 0% and standard
deviation of 5% under normal conditions and 10% during Black Swan event.
4. We assume a almost perfect positive correlation(e.g. 0.999) for underlying assets of
convergence trades during normal times and a drop in correlation during Black Swan event
to 0.8 potentially due to one of the assets being more liquid (e.g. Liquidity of 30Y Treasury
Bond > Liquidity of 29Y Treasury bond)
5. We assume the correlation between different convergence trade pairs to be zero during
normal times so as to replicate a well-diversified portfolio managed by LTCM.
6. We assume an arbitrary enter and exit thresholds for convergence trading: enter when
prices diverge by more than 1% and exit when price differences decrease to less than
0.1%
7. We assume equal starting asset prices in our simulation for convenience and as a result
we believe the same expected return(0%) and standard deviation of return(5%/10%)
could be reasonably applied to all assets held. In reality, different assets have different
liquidity as price can be one important factor(i.e. More expensive stocks might be less
accessible to retail investors). Hence, the assumptions about expected and standard
deviation of returns could be very different for different assets.
