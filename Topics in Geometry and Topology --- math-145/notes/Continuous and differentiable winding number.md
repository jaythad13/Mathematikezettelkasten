---
tags:
- math-145/2
- math-145/3
- alg-top
- top
---

We want to extend our results about polygons and curves to continuously curvy things.

### Continuous winding number

##### _theorem:_ the continuous winding number theorem

There exists a function $w$ that sends loops $f$ on $\mathbb{R}^{2} \setminus \{ 0 \}$ to integers $w(f, 0)$ that is homotopy invariant (if $f \simeq g$, $w(f, 0) = w(g, 0)$) and agrees with the [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ winding number (of a $1$-chain)|discrete winding number]].

###### _proof sketch:_

We can approximate the loop $f$ by a [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ (directed) polygon|polygon]] $\gamma$ with short edges. Note that there is a minimum $m = \min \lvert f(t) \rvert$ — since $[0, 1]$ is compact, [[Mathematical Analysis I --- math-131/notes/Continuity#_corollary _ the image of a compact set has a maximum and minimum|there is a minimum]]. There is also a $\delta > 0$ such that $\lvert t_{1} - t_{2} \rvert < \delta$ forces $\lvert f(t_{1}) - f(t_{2}) \rvert < m$ — since $[0, 1]$ is compact, $f$ is [[Mathematical Analysis I --- math-131/notes/Uniform continuity#_proposition _ continuity and uniform continuity are equivalent on compact sets|uniformly continuous]]. Then, choosing a partition $T$ such that $0 = t_{0} < t_{1} < \dots < t_{n} = 1$ such that $t_{i + 1} - t_{i} < \delta$ always, the $1$-cycle
$$
f_{T} = \sum_{i = 1}^{n} \overline{f(t_{i - 1}), f(t_{i})}.
$$

Making the edges shorter doesn't make any difference — in particular, refining the parition doesn't change the winding number. You can check this in the case of exactly one additional point. Using the fact that $0$ is away from the triangle that $f(t_{k}), f(u), f(t_{k + 1})$ form, one can see that this is true. Then use the [[Calculus --- spivak/notes/Integration over closed rectangles#_corollary _ any upper sum is greater than any lower sum|partition trick]] from analysis, show that any two approximations have the same winding number.

You can do the same partitioning trick with $[0, 1] \times [0, 1]$ divided into a grid of squares of side length less than $\delta$. Essentially, the homotopy of curves induces a homotopy of a bunch of polygons. More explicitly, you could think of this as inducing a cycle on $[0, 1] \times [0, 1]$ and do things explicitly.

Since the loop is homotopic to the approximating polygon and homotopy is an equivalence relation, the winding number is homotopy invariant.

On the [[Topics in Geometry and Topology --- math-145/attachments/homework/hw 2/hw 2.pdf#page=5|homework]], we use this result to prove the [[Complex Analysis --- math-135/notes/Cauchy integral formula#_theorem _ the fundamental theorem of algebra|fundamental theorem of algebra]].

### Angles for continuous curves

Similarly, we also want to be able to extend the [[Topics in Geometry and Topology --- math-145/notes/Discrete winding number#_definition _ angle cocycle (of a $1$-chain)|angle cocycle]] to [[Topics in Geometry and Topology --- math-145/notes/Loops and homotopies#_definition _ loop, curves|curves]]. The angle of a curve $f$ around $0$ should measure something like $2 \pi$ times the number of times it winds around $0$ plus the angle subtended by its end points $f(0)$ and $f(1)$. We do this the same way we did it for the continuous winding number theorem.

##### _definition:_ angle cocycle of a curve

Given a curve $f$ in $\mathbb{R}^{2} \setminus \{ 0 \}$, there is a subdivision cycle $f_{T}$ [[Topics in Geometry and Topology --- math-145/notes/Loops and homotopies#_definition _ homotopy|homotopic]] to $f$. The angle cocycle of $f$ about $x$ not in its support is
$$
\theta(f, x) = \theta(f_{T}, x).
$$


The proof that this is well-defined is essentially the same as the proof of the continuous winding number theorem above.

### Differentiable winding number

What if $f$ is not just a curve, but also piecewise differentiable. Will our formula for $\theta$ also be differentiable? Yes, essentially, for a piecewise differentiable curve $\gamma$, we can define continuous winding number as

![[Complex Analysis --- math-135/notes/The argument principle and winding number#_definition _ winding number|The argument principle and winding number]]

or equivalently, in real coordinates,
##### _definition:_ winding number

The winding number of a piecewise differentiable curve $\gamma$ about $0$ is
$$
w(\gamma, 0) = \int_{\gamma} \frac{x \, dy - y \, dx}{x^{2} + y^{2}}.
$$