---
tags:
- math-131/18
- anal
---

### Monotonic functions

Monotonic functions on the real line have some really nice properties!

##### _theorem:_ monotonic functions have [[Mathematical Analysis I --- math-131/notes/Limits#_definition _ left and right limits|left and right limits]] everywhere

Let $I \subset \mathbb{R}$ be an open interval. If $f : I \to \mathbb{R}$ is monotonic (weakly increasing or decreasing) then, for each $a \in I$, $\lim_{x \to a^+} f(x)$ and $\lim_{ x \to a^- } f(x)$ exist.

###### _proof:_

We will show that $\lim_{ x \to a^- } f(x) = \sup \{ f(x) \mid x \in I, x < a \}$ for a monotonically increasing function. By similar proofs, we have the left and right limits in all the cases we want.

First note that $A = \{ f(x) \mid x \in I, x < a \}$ is bounded above by $f(a)$ since $f$ is monotonic. Thus, it has a supremum $\alpha \in \mathbb{R}$. For any $\varepsilon > 0$, $\alpha - \varepsilon$ cannot be an upper bound on $A$, so we must have some $y \in I$, $y < a$ with $\alpha - \varepsilon < f(y)$. In fact, by monotonicity, every $x \in (y, a)$ gives us $\alpha - \varepsilon < f(x) \leq \alpha$. But then taking $\delta = a - y$ this exactly the definition of the left limit.

##### _theorem:_ monotonic functions are continuous almost everywhere

Let $I \subset \mathbb{R}$ be an open interval. If $f : I \to \mathbb{R}$ is monotonic, then the set of its discontinuities is at most countable.

###### _proof sketch:_

Let $A$ be the set of discontinuities of $f$. For each $a \in A$, let $I_{a}$ be the open interval $(\lim_{ x \to a^- } f(x), \lim_{ x \to a^+ } f(x))$ which is non-empty because the left and right limits cannot coincide at a discontinuous point. We claim that the function that $Q : S_{a} \mapsto q_{a}$ where $q_{a}$ can be any rational in $S_{a}$ is injective. Thus, the set of all $S_{a}$, and thus, $A$, is at most countable.

We can show that this is function is injective by showing that any two distinct $S_{a_{1}}, S_{a_{2}}$ are disjoint. Just notice that without loss of generality $a_{1} < a_{2}$, and then by choosing $a$ between $a_{1}$ and $a_{2}$, we can see that
$$
\lim_{ x \to a_{1}+ } f(x) \le f(a) \le \lim_{ x \to a_{2}- } f(x).
$$

##### _example:_ monotonic functions with countably many discontinuities

The simplest example is just a step function on $\mathbb{R}$.

Let $( q_{1}, \dots, q_{n}, \dots)$ be an enumeration of the rational numbers in $[0, 1]$. Then consider $f : [0, 1] \to \mathbb{R}$ by
$$
f(x) = \sum_{n \text{ s.t. } q_{n} < x} \frac{1}{2^n}.
$$
It's like a step function, but discontinuous at every point in $\mathbb{Q}$!