---
tags:
- math-131/16
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

### Continuity

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

##### _theorem:_ continuity preserves [[Mathematical Analysis I --- math-131/notes/Compactness#_definition _ compact|compactness]]


Suppose $f : X \to Y$ is continuous. Then if $K \subset X$ is compact, then $f^\text{img}(K)$ is compact.

###### _proof:_

Suppose $\mathcal{O} = \{ V_{\alpha} \}$ is an open cover of $f^\text{img}(K)$. Then, $\mathcal{O}_{f^\text{pre}} = \{ f^\text{pre}(V_{\alpha}) \}$ is an open cover of $K$ (every $x \in K$ has some $f(x) \in V_{\alpha} \subset f^\text{img}(K)$) and reduces to a finite subcover $\mathcal{O}_{f^\text{pre}}' = \{ f^\text{pre}(V_{1}), \dots, f^\text{pre}(V_{n}) \}$. But, then $\mathcal{O}' = \{ V_{1}, \dots, V_{n} \}$ must cover $f^\text{img}(K)$.

##### _corollary:_ the image of a compact set has a maximum and minimum

If $f : X \to \mathbb{R}$ is continuous and $K \subset X$ is compact, then $f^\text{img}(K)$ has a maximum and a minimum.

###### _proof:_

Just recall that

##### _theorem:_ continuity preserves [[Mathematical Analysis I --- math-131/notes/Connectedness#_definition _ connectedness|connectedness]]



