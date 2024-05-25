---
tags:
- spivak
- anal
- calc
- self-study
---

There are many ideas of what the $n$-dimensional volume of a subset $A \subset \mathbb{R}^n$ should be, but the one that best captures it is measure. We can't really go into all of the details of measure theory here, but we do need to be able to talk about when a $A \subset \mathbb{R}^n$ has ($n$-dimensional) measure $0$.

##### _definition:_ measure $0$

A subset $A \subset \mathbb{R}^n$ has ($n$-dimensional) measure $0$ if, for every $\varepsilon > 0$ there is some cover of $A$ by closed rectangles, $\{ U_{1}, U_{2}, \dots \}$, such that $\sum_{i = 1}^\infty v(U_{i}) < \varepsilon$.

Note that this definition is unchanged in meaning if closed rectangles are replaced by open rectangles.

It is easy to show that any countable set has measure $0$. 

##### _proposition:_ countable sets have measure $0$

Any countable subset $A \subset \mathbb{R}^n$ has measure $0$.

###### _proof:_

Let the bijection between $A$ and $\mathbb{N}$ be given by writing
$$
A = \{ \mathbf{a}_{1}, \mathbf{a}_{2}, \dots \}.
$$
Suppose we have $\varepsilon > 0$. Then, for each $\mathbf{a}_{i}$ choose $U_{i}$ to be a closed set with volume less than $\varepsilon/2^i$. Thus, $\mathcal{O} = \{ U_{i} : i \in \mathbb{N} \}$ is the desired "closed cover" with
$$
\begin{split}
\sum_{i = 1}^\infty v(U_{i}) &< \sum_{i = 1}^\infty \frac{\varepsilon}{2^i} \\
& = \varepsilon
\end{split}
$$
giving us the required inequality.

An obvious corollary is that $\mathbb{Q}$ has measure $0$ in $\mathbb{R}$.

A more strict notion of a set not having volume is content $0$.

##### _definition:_ content $0$

A subset $A \subset \mathbb{R}^n$ has ($n$-dimensional) content $0$ if, for every $\varepsilon > 0$ there is some finite cover of $A$ by closed rectangles, $\{ U_{1}, \dots, U_{n} \}$, such that $\sum_{i = 1}^n v(U_{i}) < \varepsilon$.

Again, the definition is unchanged if we use open rectangles instead of closed rectangles.

We can sanity check our definitions to make sure that they don't just make any set have content $0$.

##### _proposition:_ closed intervals have positive content

If $a < b$ then $[a, b]$ does not have content $0$. Further, if $\{ U_{1}, \dots U_{n} \}$ is a finite cover of $[a, b]$ by closed intervals, then $\sum_{i = 1}^n v(U_{i}) \ge b - a$.

###### _proof:_

Note that if there is any $U_{i}$ such that $U_{i} \not \subset [a, b]$, then either $[a, b] \subset U_{i}$ and then we have the desired inequality, or we are reduced to showing that the result is true for a smaller interval — $[a, b] \setminus U_{i}$.

Thus, we can assume without loss of generality that all $U_{i} \subset [a, b]$. Let $a < t_{0} < \dots < t_{m} < b$ be the endpoints of all of the $U_{i}$. Note that for each $U_{i}$ we can write
$$
\begin{split}
v(U_{i}) & = t_{k} - t_{l} \\
& = \sum_{j = l + 1}^k t_{j} - t_{j - 1}.
\end{split}
$$

For all $j \in \mathbb{N}_{m}$, we also have $[t_{j - 1}, t_{j}] \subset U_{i}$ for at least one $U_{i}$. Thus,
$$
\begin{split}
\sum_{i = 1}^n v(U_{i}) & \ge \sum_{i = 1}^m t_{j} - t_{j - 1} \\
& = b - a
\end{split}
$$
giving us the desired inequality.

Finally, the equivalence of open and closed rectangle definitions of measure and content $0$ give us a trivial way to show that measure $0$ and content $0$ are the same for [[Topological considerations#_definition _ compact|compact]] sets. This tells us that $[a, b]$ obviously does not have measure $0$, ensuring that our definition of measure is sane too.

##### _proposition:_ measure $0$ compact sets have measure $0$

If $A \subset \mathbb{R}^n$ is compact and has measure $0$, then $A$ has content $0$ as well.

###### _proof:_

If $A$ has measure $0$ then, for any $\varepsilon > 0$, we have a countable open cover $\mathcal{O}_{\varepsilon}$ with
$$
\sum_{U \in \mathcal{O}_{\varepsilon}} v(U) < \varepsilon.
$$

Since $A$ is compact, we can reduce $\mathcal{O}_{\varepsilon}$ to a finite sub-cover $\bar{\mathcal{O}_{\varepsilon}}$ with
$$
\sum_{U \in \bar{\mathcal{O}_{\varepsilon}}} v(U) \le \sum_{U \in \mathcal{O}_{\varepsilon}} v(U) < \varepsilon
$$
giving us that $A$ has content $0$. 

Note that compactness is definitely necessary for this result since we can have non-compact, dense, measure $0$ subsets.

##### _example:_ compactness is necessary for measure $\iff$ content

Consider the set $A = \mathbb{Q} \cap [0, 1]$. It has measure $0$ since it is countable, but it is not compact. Since it is dense in $[0, 1]$, any finite cover of $A$ must cover $[0, 1]$ as well, and thus, will give the sum of the volumes of its intervals as greater than or equal to $1 - 0 = 1$.