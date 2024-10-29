---
tags:
- math-131/16
- math-131/17
- anal
- top
---

For this note, let $(X, d_{X})$, $(Y, d_{Y})$, and $(Z, d_{Z})$ be metric spaces.

A function is continuous if it is its [[Mathematical Analysis I --- math-131/notes/Limits#_definition _ limit|limit]].
##### _definition:_ continuity

For $E \subset X$, we say that $f : E \to Y$ is continuous at $x_{0}$ if $\lim_{ x \to x_{0} } f(x) = x_{0}$.

We say $f$ is continuous on $E$ if $f$ is continuous at every $x_{0} \in E$.

Obviously we can reinterpret this in terms of sequences in the metric space. However, even more useful is a reformulation strictly in terms of the topology of $X$ and $Y$.

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

##### _theorem:_ continuity preserves [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connectedness]]

If $f : X \to Y$ and $X$ is connected, then $f^\text{img}(X)$ is connected.

###### _proof:_

Suppose by way of contradiction that $f^\text{img}(X)$ were disconnected. Then, there exist disjoint open sets $A, B$ that cover $f^\text{img}(X)$. But then $f^\text{pre}(A)$ and $f^\text{pre}(B)$ are disjoint open sets that cover $X$, making $X$ disconnected which is a contradiction.

##### _corollary:_ intermediate value theorem

If $f : [a, b] \to \mathbb{R}$ is continuous, then for any $c$ with $f(a) \le c \le f(b)$, there exists some $x \in [a, b]$ with $f(x) = c$.

A cleverer application of this shows that there is no homeomorphism from $[0, 1] \times [0, 1]$ to $[0, 1]$, and similarly that there is no homeomorphism from the sphere $S^2$ to the circle $S^1$.

##### _example:_ homeomorphism preserve dimension (?)

If $f$ is a homeomorphism $S^2 \to S^1$, remove two points from $S^2$ and now consider the restriction of $f$ to $S^2$ without the two points. The restriction should still be continuous from a connected space, but now the image of $S^2$ under the restriction is the circle without two points which is disconnected.

### Contin

##### _proposition:_ the continuity of operations on the complex numbers

If $f, g : X \to \mathbb{C}$ are continuous, then $f + g$, $fg$ and $f / g$ (where $g \neq 0$) are continuous.

###### _proof:_

Use [[Mathematical Analysis I --- math-131/notes/Limits#_proposition _ limits of functions are limits of functions on sequences|sequences]], and the [[Mathematical Analysis I --- math-131/notes/Sequences and convergence#_proposition _ the convergence of operations on the complex numbers|convergence of these operations on them]].

##### _proposition:_ continuous composition

If $f : X \to Y$ and $g : Y \to Z$ are continuous, then $g \circ f : X \to Z$ is continuous.

###### _proof sketch:_

Pull back twice.