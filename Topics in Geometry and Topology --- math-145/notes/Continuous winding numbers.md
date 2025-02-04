---
tags:
- math-145/2
- alg-top
- top
---

##### _theorem:_ the winding number theorem

There exists a function $w$ that sends loops $f$ on $\mathbb{R}^{2} \setminus \{ 0 \}$ to integers $w(f, 0)$ that is homotopy invariant (if $f \simeq g$, $w(f, 0) = w(g, 0)$) and agrees with the [[Topics in Geometry and Topology --- math-145/notes/Discrete winding numbers#_definition _ winding number (of a $1$-chain)|discrete winding number]].

###### _proof sketch:_

We can approximate the loop $f$ by a [[Topics in Geometry and Topology --- math-145/notes/Discrete winding numbers#_definition _ (directed) polygon|polygon]] $\gamma$ with short edges. Note that there is a minimum $m = \min \lvert f(t) \rvert$ — since $[0, 1]$ is compact, [[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ the image of a compact set has a maximum and minimum|there is a minimum]]. There is also a $\delta > 0$ such that $\lvert t_{1} - t_{2} \rvert < \delta$ forces $\lvert f(t_{1}) - f(t_{2}) \rvert < m$ — since $[0, 1]$ is compact, $f$ is [[Mathematical Analysis I --- math-131/notes/Uniform continuity#_proposition _ continuity and uniform continuity are equivalent on compact sets|uniformly continuous]]. Then, choosing a partition $T$ such that $0 = t_{0} < t_{1} < \dots < t_{n} = 1$ such that $t_{i + 1} - t_{i} < \delta$ always, the $1$-cycle
$$
f_{T} = \sum_{i = 1}^{n} \overline{f(t_{i - 1}), f(t_{i})}.
$$

Making the edges shorter doesn't make any difference — in particular, refining the parition doesn't change the winding number. You can check this in the case of exactly one additional point. Using the fact that $0$ is away from the triangle that $f(t_{k}), f(u), f(t_{k + 1})$ form, one can see that this is true. Then use the [[Calculus --- spivak/notes/Integration over closed rectangles#_corollary _ any upper sum is greater than any lower sum|partition trick]] from analysis, show that any two approximations have the same winding number.

You can do the same partitioning trick with $[0, 1] \times [0, 1]$ divided into a grid of squares of side length less than $\delta$. Essentially, the homotopy of curves induces a homotopy of a bunch of polygons. More explicitly, you could think of this as inducing a cycle on $[0, 1] \times [0, 1]$ and do things explicitly.

Since the loop is homotopic to the approximating polygon and homotopy is an equivalence relation, the winding number is homotopy invariant.