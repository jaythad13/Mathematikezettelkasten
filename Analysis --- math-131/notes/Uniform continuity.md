---
tags:
- math-131/18
- math-131/19
- anal
- top
- metric
---

For this note, let $(X, d_{X})$, $(Y, d_{Y})$, and $(Z, d_{Z})$ be metric spaces.

Uniform continuity gives us a stronger condition than [[Analysis --- math-131/notes/Continuity#_definition _ continuity|continuity]] that preserves more properties.

##### _example:_ $x^{2}$

The function $f : \mathbb{R} \to \mathbb{R}$ by $x \mapsto x^{2}$ is continuous everywhere — at each $a$, for every $\varepsilon > 0$ there is a $\delta > 0$ such that $\lvert a - x \rvert < \delta$ forces $\lvert a^{2} - x^{2} \rvert < \varepsilon$. However, as $a$ gets bigger, the same $\varepsilon$ demands smaller and smaller $\delta$ around $a$ to force $\lvert a^{2} - x^{2} \rvert < \varepsilon$.

##### _definition:_ uniform continuity

A function $f : X \to Y$ is uniformly continuous on $X$ if given $\varepsilon > 0$, there exists a uniform $\delta > 0$ (not dependent on $x$) such that $d_{X}(x_{1}, x_{2}) < \delta$ forces $d_{Y}(f(x_{1}), f(x_{2})) < \varepsilon$.

As always, [[Analysis --- math-131/notes/Compactness#_definition _ compact|compact sets]] are really nice —

##### _proposition:_ continuity and uniform continuity are equivalent on compact sets

Suppose $K \subset X$ is compact. If $f : X \to Y$ is continuous on $K$, then $f$ is uniformly continuous on $K$.

###### _proof:_

Consider any $\varepsilon > 0$. At each $x \in K$, by continuity we can choose $\delta_{x}$ such that $f^\text{img}(N_{\delta_{x}}(x)) \subset N_{\varepsilon / 2}(f(x))$. But then the collection of all $N_{\delta_{x} / 2}(x)$ covers $K$. By compactness, there is a finite subcover —
$$
K \subset N_{\delta_{x_{1}} / 2}(x_{1}) \cup \dots \cup N_{\delta_{x_{n}} / 2}(x_{n}).
$$
Choose $\delta < \min \{ \delta_{x_{1}} / 2, \dots, \delta_{x_{n}} / 2 \}$.

For any $x \in K$, we have $x \in N_{\delta_{x_{j}}/2}(x_{j})$ for some $j$. Then since $\delta < \delta_{x_{j}} / 2$, we have $N_{\delta}(x) \subset N_{\delta_{x_{j}}}(x_{j})$. Now, for any $x' \in N_{\delta}(x)$, we have $d_{Y}(f(x'), f(x_{j})), d_{Y}(f(x), f(x_{j})) < \varepsilon / 2$. Applying the triangle inequality, we get
$$
d_{Y}(f(x'), f(x)) \le d_{Y}(f(x'), f(x_{j})) + d_{Y}(f(x_{j}), f(x)) < \varepsilon
$$
as desired.
