---
tags:
- math-131/16
- math-131/17
- math-131/18
- anal
- top
- metric
---

For this note, let $(X, d_{X})$, $(Y, d_{Y})$, and $(Z, d_{Z})$ be metric spaces.

A function is continuous if it is its [[Mathematical Analysis I --- math-131/notes/Limits#_definition _ limit|limit]].

##### _definition:_ continuity

For $E \subset X$, we say that $f : E \to Y$ is continuous at $x_{0}$ if $\lim_{ x \to x_{0} } f(x) = x_{0}$.

We say $f$ is continuous on $E$ if $f$ is continuous at every $x_{0} \in E$.

Obviously we can reinterpret this in terms of sequences in the metric space —

##### _proposition:_ $\varepsilon$-$\delta$ continuity is equivalent to sequential continuity

For $E \subset X$, a function $f : E \to Y$ is continuous at $x$, if and only if, for every sequence $x_{n} \to x$, we have $f(x_{n}) \to f(x)$.

###### _proof:_

This follows from [[Mathematical Analysis I --- math-131/notes/Limits#_proposition _ limits of functions are limits of functions on sequences|the corresponding result for limits]].

However, even more useful is a reformulation strictly in terms of the topology of $X$ and $Y$.

##### _proposition:_ $\varepsilon$-$\delta$ continuity is equivalent to topological continuity

A function $f : X \to Y$ is continuous if and only if $f^\text{pre}(V)$ is open whenever $V$ is open in $Y$.

###### _proof:_

Suppose $f$ is $\varepsilon$-$\delta$ continuous. Let $V$ be open in $Y$. If $f^\text{pre}(V)$ is empty, it is open. Thus, we only need consider the case that it is non-empty. If $x_{0} \in f^\text{pre}(V)$, we have some $f(x_{0}) \in V$, and thus, we have a neighbourhood $N_{\varepsilon}(f(x_{0})) \subset V$. But then, by $\varepsilon$-$\delta$ continuity, there exists some $\delta > 0$ such that 
$$
f^\text{img}(N_{\delta}(x_{0})) \subset N_{\varepsilon}(f(x_{0})) \subset V.
$$
Thus, $N_{\delta}(x_{0}) \subset f^\text{pre}(V)$, and thus, the pre-image is open. 

Suppose $f$ satisfies topological continuity. For any $x_{0} \in X$, consider the open set $V = N_{\varepsilon}(f(x_{0}))$in $Y$. By topological continuity, $f^\text{pre}(V) = U$ is an open set, and we know it must contain $x_{0}$. Thus, there is some $\delta > 0$ such that $N_{\delta}(x_{0}) \subset U$ giving us $f^\text{img}(N_{\delta}(x_{0})) \subset V$. This is just $\varepsilon$-$\delta$ continuity!

This has some really nice applications!

### Continuity and compactness and connectedness

Continuity preserves all the nice things you'd want it to!

##### _theorem:_ continuity preserves [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compactness]]

Suppose $f : X \to Y$ is continuous. Then if $K \subset X$ is compact, then $f^\text{img}(K)$ is compact.

###### _proof:_

Suppose $\mathcal{O} = \{ V_{\alpha} \}$ is an open cover of $f^\text{img}(K)$. Then, $\mathcal{O}_{f^\text{pre}} = \{ f^\text{pre}(V_{\alpha}) \}$ is an open cover of $K$ (every $x \in K$ has some $f(x) \in V_{\alpha} \subset f^\text{img}(K)$) and reduces to a finite subcover $\mathcal{O}_{f^\text{pre}}' = \{ f^\text{pre}(V_{1}), \dots, f^\text{pre}(V_{n}) \}$. But, then $\mathcal{O}' = \{ V_{1}, \dots, V_{n} \}$ must cover $f^\text{img}(K)$.

##### _corollary:_ the image of a compact set has a maximum and minimum

If $f : X \to \mathbb{R}$ is continuous and $K \subset X$ is compact, then $f^\text{img}(K)$ has a maximum and a minimum.

###### _proof sketch:_

$f^\text{img}(K)$ is compact, and thus, closed and bounded. Thus, it contains its supremum and infimum which are the maximum and minimum respectively.

##### _theorem:_ continuous bijections on compact sets have continuous inverses

If $K \subset X$ is compact and $f : K \to Y$ is injective, then $f^{-1} : f^{\text{img}}(K) \to K$ is continuous.

###### _proof:_

Obviously, considering the restriction of codomain $f : K \to f^{\text{img}}(K)$ gives us that $f$ is a bijection. Note that $f^\text{img}(K)$ is compact.

Suppose $y = f(x)$. Choose a sequence $y_{n} \to y$ and $y_{n} = f(x_{n})$. Since $K$ is compact, there must be some convergent subsequence $x_{n_{i}} \to x'$ for some $x' \in X$. By continuity $f(x_{n_{i}}) \to f(x')$. However, we know that $f(x_{n_{i}}) = y_{n_{i}}$, and $y_{n_{i}} \to y = f(x)$. Thus, $f(x') = f(x)$ and by injectivity $x' = x$. Since every subsequence of $x_{n}$ converges to $x$, $x_{n} \to x$. But $x_{n} = f^{-1}(y_{n})$, and now we  have $f^{-1}(y_{n}) \to f^{-1}(y)$ for every convergent sequence $y_{n} \to y$. Thus, $f^{-1}$ is continuous.

Note that continuous functions do not generally have continuous inverses.

##### _example:_ ripping the circle apart

Consider $f : [0, 2 \pi) \to \mathbb{C}$ by $\theta \mapsto e^{i \theta}$. This wraps the half-open interval around into the circle. That is $f^\text{img}([0, 2 \pi)) = S^1$. $f$ is clearly continuous. However $f^{-1} : S^1 \to [0, 2\pi)$ is not continuous because no matter how close you choose them, pairs of points above and below the positive real axis get mapped far away.

##### _theorem:_ continuity preserves [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connectedness]]

If $f : X \to Y$ and $X$ is connected, then $f^\text{img}(X)$ is connected.

###### _proof:_

Suppose by way of contradiction that $f^\text{img}(X)$ were disconnected. Then, there exist disjoint open sets $A, B$ that cover $f^\text{img}(X)$. But then $f^\text{pre}(A)$ and $f^\text{pre}(B)$ are disjoint open sets that cover $X$, making $X$ disconnected which is a contradiction.

##### _corollary:_ intermediate value theorem

If $f : [a, b] \to \mathbb{R}$ is continuous, then for any $c$ with $f(a) \le c \le f(b)$, there exists some $x \in [a, b]$ with $f(x) = c$.

A cleverer application of this shows that there is no homeomorphism from $[0, 1] \times [0, 1]$ to $[0, 1]$, and similarly that there is no homeomorphism from the sphere $S^2$ to the circle $S^1$.

##### _example:_ homeomorphism preserve dimension (?)

If $f$ is a homeomorphism $S^2 \to S^1$, remove two points from $S^2$ and now consider the restriction of $f$ to $S^2$ without the two points. The restriction should still be continuous from a connected space, but now the image of $S^2$ under the restriction is the circle without two points which is disconnected.

### Continuity theorems

##### _proposition:_ continuity of operations on the complex numbers

If $f, g : X \to \mathbb{C}$ are continuous, then $f + g$, $fg$ and $f / g$ (where $g \neq 0$) are continuous.

###### _proof:_

Again, this follows from [[Mathematical Analysis I --- math-131/notes/Limits#_proposition _ limits of operations on the complex numbers|the corresponding result for limits]].

##### _proposition:_ continuous composition

If $f : X \to Y$ and $g : Y \to Z$ are continuous, then $g \circ f : X \to Z$ is continuous.

###### _proof sketch:_

Pull back twice.