---
tags:
- math-135/18
- anal
- top
---

For this note, let $(X, d_{X})$, $(Y, d_{Y})$, and $(Z, d_{Z})$ be metric spaces.

##### _example:_ $x^{2}$

The function $f : \mathbb{R} \to \mathbb{R}$ by $x \mapsto x^{2}$ is continuous everywhere — at each $a$, for every $\varepsilon > 0$ there is a $\delta > 0$ such that $\lvert a - x \rvert < \delta$ forces $\lvert a^{2} - x^{2} \rvert < \varepsilon$. However, as $a$ gets bigger, the same $\varepsilon$ demands smaller and smaller $\delta$ around $a$ to force $\lvert a^{2} - x^{2} \rvert < \varepsilon$.

##### _definition:_ uniform continuity

A function $f : X \to Y$ is uniformly continuous on $X$ if given $\varepsilon > 0$, there exists a uniform $\delta > 0$ (not dependent on $x$) such that $d_{X}(x_{1}, x_{2}) < \delta$ forces $d_{Y}(f(x_{1}), f(x_{2})) < \varepsilon$.