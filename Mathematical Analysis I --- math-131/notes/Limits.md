---
tags:
- math-131/16
- math-131/17
- math-131/18
- anal
- top
---

For this note, let $(X, d_{X})$ and $(Y, d_{Y})$ be metric spaces.

##### _definition:_ limit

Suppose $E \subset X$ and $x_{0}$ is a limit point of $E$. Then for a function $f : E \to Y$, we say the limit of $f$ as $x$ approaches $x_{0}$ is
$$
\lim_{ x \to x_{0} } f(x) = y_{0} 
$$
if for any $\varepsilon > 0$, there exists some $\delta > 0$ such that all $x$ with $0 < d_{X}(x, x_{0}) < \delta$, we have $d_{Y}(f(x), y_{0}) < \varepsilon$.

Note that $x_{0}$ is not necessarily in $E$ and $y_{0}$ is not necessarily in $f^\text{img}(E)$. 

The limit has an equivalent definition in terms of sequences — 

##### _proposition:_ limits of functions are limits of functions on sequences

$\lim_{ x \to x_{0} } f(x) = y_{0}$ if and only if $f(x_{n}) \to y_{0}$ whenever $x_{n} \to x_{0}$.

###### _proof:_

Suppose the limit holds and $x_{n} \to x_{0}$. Then for any, $\delta > 0$, there exists, $N$ such that for all $n > N$, $d_{X}(x_{n}, x_{0}) < \delta$. Given any $\varepsilon > 0$, choose $\delta$ such that $d_{X}(x_{n}, x_{0}) < \delta$ forces $d_{Y}(f(x_{n}), y_{0}) < \varepsilon$. Thus, for any $\varepsilon > 0$ there exists $N$ such that for all $n > N$, we have $d_{Y}(f(x_{n}), y_{0})$, and thus, $f(x_{n}) \to y_{0}$.

Suppose $\lim_{ x \to x_{0} } f(x) \neq y_{0}$. Thus, for there exists $\varepsilon > 0$ such that for any $\delta > 0$, there is some $x_{\delta}$ with $\delta$ of $x_{0}$ but with $f(x)$ at least $\varepsilon$ away from $y_{0}$. Choose a sequence of these $x_{\delta}$ such that $\delta \to 0$. For example, choose $x_{1/n}$. Obviously $x_{1 / n} \to x_{0}$. However, by our choice, $f(x_{n}) \not \to y_{0}$.

### Limits on the real and complex numbers

On the real and complex numbers, we can leverage their structure to define some natural functions that happen to be continuous. For example — we have continuity of operations on the complex numbers.

##### _proposition:_ limits of operations on the complex numbers

If $f, g : X \to \mathbb{C}$ have defined limits at $x_{0}$, then
$$
\begin{split}
\lim_{ x \to x_{0} } f(x) + g(x) & = \lim_{ x \to x_{0} } f(x) + \lim_{ x \to x_{0} } g(x) \\
\lim_{ x \to x_{0} } f(x) g(x) & = (\lim_{ x \to x_{0} } f(x)) (\lim_{ x \to x_{0} } g(x)) \\
\lim_{ x \to x_{0} } \frac{f(x)}{g(x)} & = \frac{\lim_{ x \to x_{0} } f(x)}{\lim_{ x \to x_{0} } g(x)}
\end{split}
$$
(where the last equation holds only if $\lim_{ x \to x_{0} } g(x) \neq 0$).

###### _proof sketch:_

This follows from [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ the convergence of operations on the complex numbers|the corresponding result for sequences]].