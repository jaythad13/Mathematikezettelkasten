---
tags:
- math-131/23
- math-131/24
- anal
---

Riemann integration helps us make sense of the area under the nicest bounded functions $f : [a, b] \to \mathbb{R}$, approximating the area to be somewhere between the sum of the area of minimum and maximum height rectangles under the curve. 

For this note $f$ is always a bounded function $[a, b] \to \mathbb{R}$.

### Partitions

In order to approximate the area, we divide the interval up into partitions.

##### _definition:_ partition

A partition $P$ of $[a, b]$ is a finite set of $x_{i}$ with
$$
a = x_{0} < x_{1} < \dots < x_{i} < x_{i + 1} < \dots < x_{n} = b.
$$
Each $[x_{i}, x_{i + 1}]$ is a sub-interval of the partition.

Then, for any partition, $P$, any natural definition of area is bounded between the two sums below —

##### _definition:_ lower and upper sums

For a partition $P$ of $[a, b]$ the lower Riemann sum of $f$ with respect to $P$ is
$$
L(P, f) = \sum_{i = 1}^{n} (x_{i} - x_{i - 1}) m_{i}
$$
and the upper Riemann sum of $f$ with respect to $P$ is
$$
U(P, f) = \sum_{i = 1}^{n} (x_{i} - x_{i - 1}) M_{i}
$$
where $m_{i} = \inf_{x \in [x_{i - 1}, x_{i}]} f(x)$ and $M_{i} = \sup_{x \in [x_{i - 1}, x_{i}]} f(x)$. (These bounds exist since $f$ is bounded)

A natural idea is then to make this partition smaller and thus, intuitively, the lower and upper sums should come closer together.

##### _definition:_ refinement

A partition $P'$ is a refinement of $P$ if $P' \subset P$.

Note that if $P'$ is a refinement of $P$, every sub-interval of $P$ is divided into finitely many (possibly just one) sub-interval in $P'$.

##### _proposition:_ refinements bring lower and upper sums closer

If $P'$ is a refinement of $P$, then $L(P, f) \le L(P', f)$ and $U(P', f) \le U(P, f)$.

###### _proof sketch:_

Notice that if the interval $I$ is written as the disjoint union of intervals $\bigcup I_{n}$, since $\inf_{x \in I} f(x)$ is a lower bound on $f$ on all of $I$, it is a lower bound on each $I_{n}$, and thus, $\inf_{x \in I_{n}} f(x)$, being the greatest lower bound on $I_{n}$ must be greater than it. That is, $\inf_{x \in I} f(x) \le \inf_{x \in I_{n}} f(x)$. Similarly, $\sup_{x \in I} f(x) \ge \sup_{x \in I_{n}} f(x)$.

Now just apply this over the sums.

##### _proposition:_ upper sums are always greater than lower sums

For any two partitions $P_{1}, P_{2}$
$$
L(P_{1}, f) \le U(P_{2}, f).
$$

###### _proof:_

Notice that $P = P_{1} \cup P_{2}$ is a partition that refines both $P_{1}$ and $P_{2}$. Thus,
$$
L(P_{1}, f) \le L(P, f) \le U(P, f) \le U(P_{2}, f).
$$

### The integral

With this last proposition, we have a natural definition of "lower" and "upper" integrals.

##### _definition:_ lower and upper integrals

The lower and upper Riemann integrals of $f$ on $[a, b]$ are
$$
\underline{\int_{a}^b f(x) \, dx} = \sup_{\text{partitions } P} L(P, f)
$$
and
$$
\overline{\int_{a}^b f(x) \, dx} = \inf_{\text{partitions } P} U(P, f)
$$
respectively.

We also have a natural definition of what it means to be Riemann integrable at all —

##### _definition:_ Riemann integrable

We say that $f : [a, b] \to \mathbb{R}$ is Riemann integrable if
$$
\underline{\int_{a}^b f(x) \, dx } = \overline{\int_{a}^b f(x) \, dx }
$$

![[Calculus --- spivak/notes/Integration over closed rectangles#_example _ the famous non-integrable Dirichlet function|Integration over closed rectangles]]

![[Calculus --- spivak/notes/Integration over closed rectangles#_theorem _ integrable upper and lower sums get arbitrarily close|Integration over closed rectangles]]

An incredibly nice fact that just so turns out to be true is that continuous functions are integrable. In fact, integrable functions don't have to be integrable everywhere — almost everywhere is enough.

Note that for this theorem, our hypothesis that $f$ is bounded is crucial.

##### _theorem:_ finitely discontinuous functions are integrable

If the set of discontinuities of $f$ is finite, then $f$ is Riemann integrable.

###### _proof sketch:_

Suppose $f$ has discontinuities at $z_{1}, \dots, z_{k}$. Choose partitions containing $z_{i} \pm 1 / n$ for small enough $n$ so that the "integral" over all the intervals around the $z_{i}$ can be bounded using the bound on the function and just making $n$ sufficiently small.

Excluding these open intervals, $K = [a, b] \setminus \bigcup_{i = 1}^k (z_{i} - 1 / n, z_{i} + 1 / n)$ is compact, so $f$ is [[Analysis --- math-131/notes/Uniform continuity#_definition _ uniform continuity|uniformly continuous]] on $K$. Thus, by picking small enough partitions on $K$, we will get that the difference between the maximum and minimum on the interval is small.

Thus, we can get the difference between the upper and lower partitions to be

The real theorem here is that functions that are "almost everywhere" continuous are integrable. Using the definition of measure zero.

![[Calculus --- spivak/notes/Measure#_definition _ measure $0$|Measure]]

it's easy to see that we can pull the same trick as we did earlier — we can draw open neighbourhoods of arbitrarily small total length around the discontinuities, bound the integral over them by the maximum and minimum, and leave the rest to continuity to take care of. 

##### _corollary:_ monotonic functions are integrable

If $f$ is monotonic(ally increasing or decreasing), it is Riemann integrable.

###### _proof:_

[[Analysis --- math-131/notes/Continuous functions on the reals#_theorem _ monotonic functions are continuous almost everywhere|Monotonic functions are continuous almost everywhere]] since [[Calculus --- spivak/notes/Measure#_proposition _ countable sets have measure $0$|countable sets have measure zero]].

Note that we can also prove this by noting that the difference between the maximum and minimum values of a monotonic function on an interval is just the difference between the values on the boundary. Since this sum is telescoping, uniform partitions with subintervals of length $1/n$, will cause the difference between upper and lower sums to go to zero — $(f(b) - f(a))/n$ goes to zero.