---
tags:
- calc
- self-study
---

### The projection principle

There is an obvious relationship between $m$ real-valued functions, and functions to $\bb R^m$. The projection principle says that they are exactly the same (upto isomorphism).

##### _definition:_ component functions

The component functions of a function $f : A \to \bb R^m$ (for $A \subset \bb R^n$) are the $m$ functions $f_1, \ldots, f_m : A \to \bb R$ such that $f(\bvec x) = (f_1(\bvec x), \cdots f_m(\bvec x))$ for all $\bvec x \in A$.

Note that they are defined uniquely, and that $m$ functions from $A$ to $\bb R$, $g_1, \ldots, g_m$ would also uniquely define a function $g : A \to \bb R^m$ with component functions $g_1, \ldots, g_m$.

##### _notation:_ $\pi$, $\pi_i$

By $\pi$, we mean the identity function on $\bb R^n$ such that $\pi(\bvec x) = \bvec x$.

By $\pi_i$ we mean the $i$th projection function on $\bb R^n$ (for $i \in \bb N_n$), giving $\pi_i(\bvec x) = x_i$, for $\bvec x = (x_1, \ldots, x_n)$.

Note that then we have the $i$th component function of any function $f$ as $\pi_i \circ f$.

### Continuity

In single variable calculus, the expression $\lim_{x \to a} f(x) = L$ means that we can get $f(x)$ arbitrarily close to $L$ for $x$ values within some range of $a$. This generalises neatly in $\bb R^n$ (and indeed in all metric spaces) — we can define limits as below, and then define continuity to be where the limit and the value of a function are the same.

##### _definition:_ limit, $\lim_{\bvec x \to \bvec a} f(\bvec x)$

For a function $f : A \to \bb R^m$ (with $A \subset \bb R^n$), we say the function has limit $L$ at $\bvec a$, denoted
$$
\lim_{\bvec x \to \bvec a} f(\bvec x) = L
$$
if for every $\varepsilon > 0$ we have some $\delta > 0$ such that all $\bvec x$ with $0 < \norm{\bvec x - \bvec a} < \delta$ give us $\norm{f(\bvec x) - f(\bvec a)} < \varepsilon$.

##### _definition:_ continuity at point, continuous function

A function $f : A \to \bb R^m$ ($A \subset \bb R^n$) is continuous at $\bvec a$ if $f(\bvec a) = \lim_{\bvec x \to \bvec a} f(\bvec x)$.

We say $f$ is continuous if $f$ is continuous at every $\bvec a \in A$.

While these definitions work, continuity can be defined purely topologically, without using limits. This more general definition makes strong results easy.

##### _theorem:_ topological continuity is equivalent to $\varepsilon-\delta$ continuity

A function $f : A \to \bb R^m$ ($A \subset \bb R^n$) is continuous if and only if every open set $U$ in $\bb R^m$ has an open pre-image in $A$. More strongly, every open set $U \subset \bb R^m$ gives us $f^{\text{pre}}(U) = V \cap A$ for some open set $V \subset \bb R^n$.

###### _proof:_

Suppose $f$ is continuous. Then if $\bvec a \in f^{\text{pre}}(U)$ and thus, $f(\bvec a) \in U$, some open set, we have for every $\varepsilon$-[[Metric spaces#_definition _ r-neighbourhood, radius, $N_r(p)$|neighbourhood]] around $f(\bvec a)$ contained in $U$ (we have one, because [[Topological considerations#Open and closed sets|we have an open rectangle]] in $U$) a $\delta$-neighbourhood around $\bvec a$ such that every $\bvec b$ in that $\delta$-neighbourhood gives $f(\bvec b)$ in the $\varepsilon$-neighbourhood, and thus $f(\bvec b) \in U$. This means that the $\delta$-neighbourhood and thus, the open rectangle inside it, is contained in $f^{\text{pre}}(U)$, making $f^{\text{pre}}(U)$ open.

Suppose $f$ is "topologically continuous". Then if we look at any $\varepsilon$-neighbourhood around $f(\bvec a)$, $U$, we have that its pre-image is open. Thus, its pre-image contains an open rectangle containing $\bvec a$, and that open rectangle contains a $\delta$-neighbourhood around $\bvec a$, which has image inside the $\varepsilon$-neighbourhood.

One example of how this topological definition is useful (and also an example of how compactness is useful) is in showing that continuous functions preserve compactness.

##### _theorem:_ continuous functions preserve compactness

If $f : K \to \bb R^m$ is continuous ($K \subset \bb R^n$), and $K$ is compact, then $f^{\text{img}}(K)$ is compact.

###### _proof:_

Let $K' = f^{\text{img}}(K)$. Suppose $\mathcal O$ is an open cover of $K'$. Then each point $f(\bvec x) \in K'$ is contained in some $U \in \mathcal O$ that has an open pre-image in $K$, $U'$ (because of continuity). All of these $U'$ together contain every $\bvec x \in K$, and thus, form an open cover of $K$, $\mathcal O'$. Because $K$ is compact, we can reduce this to a finite sub-cover $\bar{\mathcal O'}$. Since all of the (finitely many) sets in $\bar{\mathcal O'}$ are pre-images of open sets and together contain every point in $K$, their (finitely many) images are open and contain every point in $K'$, and are thus, a finite sub-cover of $\mathcal O$.

### Oscillation

If we have a discontinuous but bounded function $f : A \to \bb R$, we can measure the extent to which it fails to be continuous by looking at its "maximum" and its "minimum" in increasingly small neighbourhoods around a discontinuity. We call their difference the oscillation of the function at the point.

##### _definition:_ oscillation, $o(f, \bvec a)$, $M(f, \bvec a, \delta)$, $m(f, \bvec a, \delta)$

For a bounded function $f : A \to \bb R$ (with $A \subset \bb R^n$), $\bvec a \in A$ and $\delta > 0$ let
$$
\begin{gathered}
M(f, \bvec a, \delta) = \sup \set{f(\bvec x) : \norm{\bvec x - \bvec a} < \delta} \\
m(f, \bvec a, \delta) = \inf \set{f(\bvec x) : \norm{\bvec x - \bvec a} < \delta}
\end{gathered}.
$$
Then the oscillation of $f$ at $\bvec a$ is
$$
o(f, \bvec a) = \lim_{\delta \to 0} M(f, \bvec a, \delta) - m(f, \bvec a, \delta).
$$

Note that $M$ and $m$ exist because $f$ is bounded. Also note that $o$ is positive because the $\sup$ of a set is always greater than the $\inf$ of the set.

A sanity-check that this definition really does measure a "degree of discontinuity" for bounded functions is given by looking at its value at continuous points of the function. Intuitively it should be zero — as we look at smaller and smaller neighbourhoods around a point at which a function is continuous, the function values should get closer and closer to the value at the point, and thus, their "maximum" and "minimum" should also get closer to the same value. The converse should also hold — if the "maximum" and "minimum" values get closer and closer in small neighbourhoods around the point, then we should be able to constrain all the values of the function between them.

##### _proposition:_ continuous functions do not oscillate

A bounded function $f : A \to \bb R$ (with $A \subset \bb R$) is continuous at $\bvec a$ if and only if $o(f, \bvec a) = 0$.

###### _proof:_

Suppose $f$ is continuous at $\bvec a$. Then for any $\varepsilon > 0$ we have $\delta > 0$ such that $\abs{\bvec x - \bvec a} < \delta$ gives us $\abs{f(\bvec x) - f(\bvec a)} < \varepsilon$. Thus, we can get
$$
\begin{split}
	M(f, \bvec a, \delta) - m(f, \bvec a, \delta) & = M(f, \bvec a, \delta) - f(\bvec a) + f(\bvec a) - m(f, \bvec a, \delta)\\
	& = \abs{M(f, \bvec a, \delta) - f(\bvec a)} + \abs{m(f, \bvec a, \delta) - f(\bvec a)} \\
	& < 2 \varepsilon
\end{split}
$$
for any $\varepsilon$, as long as $\delta$ is small enough. Since if it's true for $\delta_1$, it's true for any $\delta_2 < \delta_1$, we have that
$$
o(f, a) = \lim_{\delta \to 0} M(f, \bvec a, \delta) - m(f, \bvec a, \delta) = 0.
$$

Suppose $f$ has zero oscillation at $\bvec a$. Then for any $\varepsilon > 0$ we have $\delta > 0$ such that $r < \delta$ gives us $M(f, \bvec a, r) - m(f, \bvec a, r) < \varepsilon$ (with $r > 0$). But then since $M(f, \bvec a, r) \ge f(\bvec x)$ and $m(f, \bvec a, r) \le f(\bvec x)$ for all $\bvec x$ with $\norm{\bvec x - \bvec a} < r$, we must have $\abs{f(\bvec x) - f(\bvec a)} < \varepsilon$ for all $\bvec x$ with $\norm{\bvec x - \bvec a} < r$. Thus, $f$ is continuous.

This notion of oscillation allows us to prove useful results — for example, the following results formalises our intuition that you can't just have an isolated point at which the function is continuous by showing that any set of "sufficiently discontinuous" points must be closed.

##### _proposition:_ sufficiently discontinuous sets are closed

If $f : A \to \bb R$ is a bounded function (and $A$ is a closed subset of $\bb R^n$), then for any $\varepsilon > 0$ $V = \set{\bvec x \in A : o(f, \bvec x) \ge \varepsilon}$ is closed.

###### _proof:_

Let $U = \bb R^n \setminus V$. At each point $\bvec x \in U$ we have $o(f, \bvec x) < \varepsilon$ (or $\bvec x \notin A$, and then there is an open rectangle around it since $\bb R^n \setminus A$ is open).

Since $o(f, \bvec x) < \varepsilon$, there exists some $\delta$ such that $M(f, \bvec x, \delta) - m(f, \bvec x, \delta) < \varepsilon$. This defines an open $\delta$-neighbourhood around $\bvec x$. Inside this neighbourhood, any point $\bvec y$ has $M(f, \bvec y, \delta') - m(f, \bvec y, \delta') < \varepsilon$ as long as the $\delta'$-neighbourhood of $\bvec y$ is contained inside the $\delta$-neighbourhood of $\bvec x$. Thus, all these $\bvec y$ give us $o(f, \bvec y) < \varepsilon$.

Thus, this $\delta$-neighbourhood (and the open rectangle inside it) are a subset of $U$ containing $\bvec x$ — $U$ is open, and thus, $V$ is closed.


