# Miller Rabin Primality Test

## Pseudocode
Suppose you want to test if a number $n$ is prime:
1. $n$ is even or $< 3 \rightarrow$ false
2. Write $n - 1 = 2^r \times d$, factor out powers of 2 from $n$
3. Pick a <span style="color:rgb(198, 160, 246)">random</span> base $a$ such that $2 \leq a \leq n - 2$ 
4. Compute $x = a^d ~\text{mod}~n$ 
5. If $x = 1$ or $x = n - 1$ then we <span style="color:rgb(198, 160, 246)">probably</span> have a prime
6. Otherwise, $x = x^2~\text{mod}~n$ up to $r-1$ times. If $x$ ever becomes $n-1$, still <span style="color:rgb(198, 160, 246)">probably</span> prime
7. If we never hit $n-1$ then is definitely composite
8. <span style="color:rgb(198, 160, 246)">Repeat</span> steps **3-7** many times to boost accuracy

## Runtime Complexity
Let 
- $b=\text{number of bits of n}~(b = \lceil log_2 n \rceil)$ 
- $k = \text{number of rounds you repeat the check}$
- $M(b)=\text{runtime complexity to perform multiplication on b-bit integer}$

Each loop runs $k$ times, and each round does one exponentiation (assume modular exponentiation), so bit-complexity is in general: $O(k \cdot b \cdot M(b))$. Note modular exponentiation is roughly $O(log n) = O(b)$ because the exponent has $b$ bits.
- With naive multiplication: $M(b)=O(b^2)$, per round: $O(b \cdot b^2) = O(b^3)$ and with $k$ rounds, $O(k \cdot b^3)$; or in terms of $n$ $O(k \cdot log^3 n)$ 
- With faster multiplication algorithms, i.e. Karatsuba: $M(b) = b^{1.585}$ or FFT: $M(b)=b~logb~log~log b$. We can improve the runtime of the Miller-Rabin Primality Test.
