---
tags:
- math-131/26
- math-131/27
- anal
- metric
---

We are working towards a first fundamental result in functional analysis — that the space of real functions on a compact set is a complete metric space.

Let $K$ be a [[Analysis --- math-131/notes/Compactness#_definition _ compact|compact]] metric space. Then we can define

##### _definition, proposition:_ the space of continuous functions is a metric space

The space of continuous functions $f : K \to \mathbb{R}$ is a metric space $\mathcal{C}(K), d$ under the $\sup$ metric with
$$
d(f, g) = \sup_{x \in K} \lvert f(x) - g(x) \rvert.
$$

Note that since [[Analysis --- math-131/notes/Uniform continuity#_proposition _ continuity and uniform continuity are equivalent on compact sets|continuous functions on a compact set are uniformly continuous]], and [[Analysis --- math-131/notes/Compactness#_theorem _ compact sets are closed and bounded|compact sets are closed]], we can replace continuous with uniformly continuous and $\sup$ with $\max$.

###### _proof:_

We just need to verify the [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric space axioms]] for $\mathcal{C}(K)$.

Clearly, $d(f, g) = 0$ if and only if $f = g$. Also, $d$ is clearly symmetric since the absolute value of the difference of $f$ and $g$ is symmetric. It remains to show that the triangle inequality holds.

Note that the triangle inequality holds point-wise to give
$$
d(f, g) = \lvert f(x) - g(x) \rvert \le \lvert f(x) - h(x) \rvert + \lvert h(x) - g(x) \rvert.
$$
By definition the right hand side must be bounded by $d(f, h) + d(h, g)$, so we have the desired inequality.

Actually, we can say more than just verifying that $\mathcal{C}(K)$ is a metric space. $\mathcal{C}(K)$ is a [[Norms|normed vector space]] since the continuous functions form a [[Linear algebra done right --- ladr/notes/Vector spaces|vector space]]. $\mathcal{C}(K)$ is also a [[Abstract algebra --- math-171/notes/Rings#_definition _ rings|ring]] since [[Analysis --- math-131/notes/Continuity#_proposition _ continuity of operations on the complex numbers|products of continuous functions are continuous]].

First we will show that $\mathcal{C}(K)$ is complete.

##### _theorem:_ $\mathcal{C}(K)$ is [[Analysis --- math-131/notes/Cauchy sequences#_definition _ completeness|complete]]

###### _proof sketch:_

Suppose $(f_{n} )_{n \in \mathbb{N}}$ is a [[Analysis --- math-131/notes/Cauchy sequences#_definition _ Cauchy sequence|Cauchy sequence]] in $\mathcal{C}(K)$. Show that there is a sensible function $f : K \to \mathbb{R}$ defined by $f(x) = \lim_{ n \to \infty } f_{n}(x)$ since [[Analysis --- math-131/notes/Cauchy sequences#_theorem _ real spaces are complete|the reals are complete]]. This follows since the maximum distance between $f_{n}(x)$ and $f_{m}(x)$ being bounded by $\varepsilon$ means this bound holds at each $x \in K$, and thus, each $(f_{n}(x))_{n \in \mathbb{N}}$ is a Cauchy sequence. 

It remains to show that $f$ is continuous. This will follow by the strength of the convergence. It is not generally true that the point-wise limit of uniformly continuous functions is continuous — consider the sequence of all $x^n$ on $[0, 1]$ converging to the discontinuous function $f$ with
$$
f(x) = \begin{cases}
0 & x \neq 1 \\
1 & x = 1.
\end{cases}
$$
Note here that this sequence of functions is not Cauchy under our $\sup$ metric since the steep slope of the functions near $1$ allows the maximum point-wise distance between any two functions be sufficiently large. In particular, $\lvert x^{2n} - x^n \rvert$ always achieves $1/4$ for the right $x$.

We can show that $f$ is continuous is true by picking $N$ large enough and $x$ close enough to $x_{0}$ at each $x_{0}$. It only remains to show that the point-wise limit $f$ is really the limit of the $f_{n}$ under the $\sup$ metric.

First we show that $f_{n} \to f$ locally — for any $\varepsilon > 0$, around each $x \in K$ there is an open ball $B_{\delta}(x)$ with its image under $f - f_{n}$ less than $\varepsilon$ away from $0$. This follows by choosing $\delta$ small enough that $f$ is close to $f(x)$ and $f_{n}$ is close to $f_{n}(x)$, and $n$ large enough that $f_{n}(x)$ is close to $f(x)$. (Technically, to avoid $\delta$ depending on $n$, we use a fourth term in the triangle inequality to show with $N$ big enough that the Cauchy condition holds, so that we can have a uniform $\delta$ to compare against).

But then these $B_{\delta}(x)$ form an open cover of compact $K$, and [[Analysis --- math-131/notes/Compactness#_definition _ compact|must reduce to a finite sub-cover]]. Then by picking the largest $n$ required in any of the $\delta$-balls for $f$ and $f_{n}$ to be close, we have $f$ and $f_{n}$ uniformly close on $K$.