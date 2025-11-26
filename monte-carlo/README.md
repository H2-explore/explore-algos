# Monte-Carlo Simulation
In a nutshell, there are two key ingredients that make up Monte-Carlo simulation:
> Repeated Random Sampling + Random Number Generator

The RNGs are generated from a known probability distribution, i.e. binomial, normal, exponential distributions. 

In a statistical lens, Monte-Carlo simulation is pretty simple, you repeatedly generate data points via some RNGs with a known distribution and calculate the parameters of interest (mean, median, bias etc.)
<span style="color:rgb(198, 160, 246)">With the caveat that one needs to first find out a way to generate data from RNGs that approximates a more complex process.</span>

This is useful because the inherit randomness in this process resembles the randomness in the real world data we observe, hence sheds lights on how these randomness affect the parameters. 
And of course, it is always an approximation of the parameters.

## Monte-Carlo Algorithm
As a computer science student, I picked this topic for to write about for a REASON.

I think of Monte-Carlo algorithm a special type of Monte-Carlo simulation, with one more constraint:
> Always draw from a uniform distribution

It is fast, normally polynomial runtime, given that RNGs are fast. Due to its randomness nature, it is non-deterministic, meaning sometimes it will output the wrong answer. So it trades speed with accuracy. 

A generic Monte-Carlo algorithm roughly works like this:
1. Define a problem, what do we want to approximate (i.e. is n prime?)
2. Use uniform RNG to pick samples 
3. Perform some tests to find an answer to the problem and record it
4. Repeat many times for accuracy
5. Aggregate results - combine all trials into a final estimate, for example, if any run results in a composite $\rightarrow$ number is composite

## Examples
- [**Miller-Rabin Primality Test**](monte-carlo/miller-rabin-primality-test/OUTLINE.md)