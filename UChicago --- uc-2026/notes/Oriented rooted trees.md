---
tags:
- uc-2026/random-graphs/1
- uc-2026/random-graphs/2
- comb
- graph
- prob
- ewain-gwynne
---

### Oriented rooted trees and walk excursions

If we want to understand [[Superdiscrete --- math-55A/notes/Special graphs#_definition _ tree|trees]], we have two tricks — we can add extra data to create finer isomorphism classes, and we can put them in bijection with objects that are simpler to understand. Here, we do both.

##### _definition:_ walk excursion

A **walk excursion** of size $2n$ is a function $f : \{ 0, \dots, 2n \} \to \mathbb{N}_{0}$ such that $f(2n) = f(0) = 0$ and $f(j) - f(j - 1) \in \{ \pm 1 \}$ for all $j$.

---

##### _definition:_ oriented rooted trees

An **oriented rooted tree** is a tree with a root vertex $e_{0}$ and a cyclic ordering for all of its branches.

We also call the orientation a plane structure on the tree because we can think of it as a tree embedded in $\mathbb{R}^{2}$ up to oriented homeomorphisms of the plane.

---

##### _theorem:_ oriented rooted plane trees are just walk excursions

Oriented plane trees with $n$ edges are in bijection with walk excursions of size $2n$.

###### _proof sketch:_

If $v_{0}, \dots, v_{n}$ is the sequence of vertices for the unique depth first search indicated by the plane structure on the tree $T$, then send $T, \sigma$ to the **contour function** with $f(j) = d(v_{j}, v_{0})$. In the other direction, fold the graph. (If we didn't have the extra data of an orientation and root, this would be highly non-injective).

---

##### _theorem:_ the number of rooted plane trees

There are $\binom{2n}{n}/(n + 1)$ rooted oriented plane trees (rooted trees with a distinguished edge from the root, and a cyclic ordering of edges) with $n$ edges.

###### _proof sketch:_

It suffices to count walk excursions of length $2n$. Constructing a walk-excursion involves choosing which of the $n$ differences $f(j) - f(j - 1)$ are $1$ and setting the rest to $-1$. There are $\binom{2n}{n}$ such choices. However, an arbitrary function constructed in this way may take values in $\mathbb{Z} \setminus \mathbb{N}_{0}$.

To get rid of these, we want to find the number of functions that hit $-1$. Let $f$ be such a function and let $k$ be the minimum integer such that $f(k) = -1$. Let $\widetilde{f} : \{ 0, \dots, 2n \} \to \mathbb{Z}$ have $\widetilde{f}_{\mid [0, k]} = -2 - f_{\mid [0, k]}$ and $\widetilde{f}_{\mid [k, 2n]} = f_{\mid [k, 2n]}$. It turns out that $f \mapsto \widetilde{f}$ is a bijection between the possibly negative walk excursions that hit $-1$ and functions $f : \{ 0, 2n \} \to \mathbb{Z}$ with $f(0) = -2$, $f(2n) = 0$, and $f(j) - f(j - 1) \in \{ \pm 1 \}$. But there are obviously $\binom{2n}{n + 1}$ of these. Some binomial identities give that
$$
\binom{2n}{n} - \binom{2n}{n + 1} = \frac{1}{n + 1} \binom{2n}{n}
$$
as desired.

---

### Brownian motion and Brownian excursion

We wanted to understand what a typical large rooted plane tree looks like. This is of course the same thing as understanding what the typical contour function looks like for large $2n$. If we remove the constraint that the contour function need be non-negative and return to $0$ at time $2n$, then we can see these contour functions as a subset of [[Simplicial homology and random walks --- math-145/notes/Random walks|random walks]] on $\mathbb{Z}$, restricted to $[0, 2n]$. 

The uniform distribution on these assigns probability $2^{-2n}$ to each random walk $X : [0, 2n] \cap \mathbb{Z} \to \mathbb{Z}$ satisfying $X(j) - X(j - 1) = \pm 1$. Thus, the conditional distribution on the subset of these random walks satisfying $X(2n) = 0$ and $X(j) \geq 0$ is just the uniform distribution on walk excursions. We know something about the distribution on random walks as $n \mapsto \infty$, so we know something about the uniform distribution on walk excursions too!

Brownian motion gives a typical continuous function. Some trivia — it is nowhere differentiable, $\alpha$-Hölder continuous for all $\alpha < 1 / 2$.

##### _definition:_ Brownian motion

A random continuous function $B : [0, \infty) \to \mathbb{R}$ with $B(0) = 0$ is said to have **Brownian motion** if, for all $s \leq t$, the increment $B(t) - B(s) \sim N(0, t - s)$ is normally distributed, and for all $t_{1} \leq \dots \leq t_{n}$ the distinct increments $B(t_{j}) - B(t_{j - 1})$ are independent.

---

##### _theorem:_ rescaled random walks converge to Brownian motion

Let $X$ be a random walk on $\mathbb{Z}$. Then as $n \to \infty$, the function $t \mapsto n^{-1 / 2} X(\lfloor nt \rfloor)$ converges in distribution to Brownian motion with respect to the topology of uniform convergence.

---

We have an analogue of this for our walk excursions. We can't quite condition Brownian motion to $B(1) = 0$ since this is a zero probability event. However, we can condition on $B(1) < \varepsilon$ and consider the limit as $\varepsilon \to 0$. We call this (with Brownian motion restricted to $[0, 1]$ and conditioned on $B(t) \geq 0$ for all $t$) **Brownian excursion**.

##### _theorem:_ rescaled random walk excursions converge to Brownian excursion

Let $X_{n}$ be a uniform random walk excursion with $2n$ steps. Consider the function $x_{n} : [0, 1] \to [0, \infty)$ by $t \mapsto (2n)^{1 / 2} X_{n}(2n t)$ converges in distribution to Brownian motion with respect to the topology of uniform convergence.

---

The probability that $x$ is in an open set of the continuous functions converges to the probability that $B$ is in that open set. In the topology of uniform convergence, the open sets are generated by the basis of $\varepsilon$-tubes around continuous functions.

### The typical large oriented rooted tree

Our hope is that we can now describe the limit of a random oriented rooted tree with $n$ edges as $n \to \infty$. The idea is to fold Brownian excursions (or any continuous function) in the same way that we folded walk excursions.

Below we use $[s, t]$ as a shorthand for whichever of $[s, t]$ and $[t, s]$ makes sense.

##### _definition:_ tree distance function

Let $f : [0, 1] \to [0, \infty)$ be a continuous function with $f(0) = f(1) = 0$. Then the **tree distance function** of $f$ is $\Delta_{f} : [0, 1] \times [0, 1] \to [0, \infty)$ with
$$
\Delta_{f}(s, t) = f(s) + f(t) - 2 \min_{u \in [s, t]} f(u).
$$

---

This exactly mimics the graph distance we get by folding walk excursions — we go down on $f(s)$ until we're just below the graph, and then we go back up to $f(t)$.

##### _proposition:_ the tree distance function is a pseudometric

$\Delta_{f}$ is a **pseudometric** on $[0, 1]$ (satisfying all the properties of a [[Analysis --- math-131/notes/Metric spaces#_definition_ metric space, metric|metric]] except positive definiteness).

$\Delta_{f}(s, t) = 0$ if and only if $f(s), f(t) < f(u)$ for all $u \in [s, t]$.

---

Note that $\Delta_{f}(s, t) = 0$ if and only if we would have identified $s$ and $t$ in the rooted tree anyway. Thus, if we quotient our by the equivalence relation $\Delta_{f}(s, t)$.

##### _definition:_ oriented rooted tree of a function

The **oriented rooted tree** associated to a continuous function $f$ (satisfying hypotheses above) is the metric space on the set $[0, 1] / \sim$ (where $s \sim t$ exactly when $\Delta_{f}(s, t)$) and the metric $d(s, t) = \Delta_{f}(s, t)$.

---

This is a standard construction to get a metric space from a pseudometric.