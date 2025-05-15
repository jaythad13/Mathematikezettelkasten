---
tags:
- vsrp/2025/1
- siddhartha-bhattacharya
- diff-eq
---

We want to be able to show that the earth revolves around the sun without technology — no telescopes, satellites, or anything else you couldn't find in ancient Greece (?).

### Flows

##### _definition:_ flow

A flow is an [[Abstract Algebra I --- math-171/notes/Group actions#_definition _ (left) group action|group action]] of $\mathbb{R}$ (the additive reals) on a set $X$.

A flow is continuous if $X$ is a [[Topology --- math-147/notes/Topologies#_definition _ topology, open sets, topological space|topological space]] and $\mathbb R \times X \to X$ is continuous, smooth if $X$ is a smooth manifold and the map is smooth, et c.

For example, $\mathbb{R}$ can act on itself by addition, or on $S^1$ by $(t, z) \mapsto e^{2 \pi i t} z$, or on any real vector space by scaling by $e^t$ which gives expansion as $t$ goes from $-\infty$ to $\infty$. A less obvious example is the $n$-body problem.

##### _example:_ the $n$-body problem

Suppose we have $n$ point masses in $\mathbb{R}^3$. Let $X$ be $\mathbb{R}^{6n} = (\mathbb{R}^3)^n \times (\mathbb{R}^3)^n$, with each point giving the position and velocity of each particle. 

Given an initial state $x$, let $t \cdot x$ be the resultant state at time $t$, where we only consider gravitation between pairs of particles. If we consider $\alpha_{x}(t) = t \cdot x$, then $\alpha_{x}$ satisfies the obvious differential equation.

This isn't related to what we want to do, but it's nice to note that we can turn second order differential equations on a manifold into first order ODEs on the tangent bundle.

In general, if $M$ is a compact manifold and $(t, x) \to \alpha_{x}(t)$ gives a smooth flow, then $x \to \alpha_{x}'(0)$ is a smooth vector field $M \to \mathrm{T}M$. In fact the correspondence between vector fields and flows is bijective so we can go from a smooth vector field to a smooth flow as well! This is just the [[Differential Equations --- math-82/notes/Existence and uniqueness|existence and uniqueness theorem]] for ODEs.

### The direction of a star


We need to calculate the obvious data — given a point $p$ on earth, we want to see how the angle to a star changes. Since we can, lets pick $p$ on the equator. We'll set a coordinate system as well — let the $x$-axis be the east-west direction, let the $y$-axis be the north-south direction, and let the up-down direction be on the $z$-axis. 

Then, for a star $\star$ and a time $t$, let $D_{\star}(t) \in S^{2}$ be the observed direction of $\star$ at time $t$. We claim this is a smooth flow on $S^{2}$. We want to calculate it. We'll allow an error margin of $10^{-5}$ radians (so $3$ arcseconds).

But there's a problem. Really, the axis of rotation is rotating in a circle around a particular point — so maybe we should consider flows around $S^{2} \times S^1$. But actually, the way that movement occurs isn't quite smooth, so we should consider $S^{2} \times \mathbb{T}^2$, and really if you want to understand the effect of the moon as well, you should consider $S^{2} \times \mathbb{T}^3$.

We can ignore the moon with our error margin, so we just consider the flow on $S^{2} \times S^1$. Then we notice that the flow $D_{\star}(t)$ moves up on $S^{2}$ during the summer solstice and down during the winter solstice. Since this isn't an isometry, it cannot be the result of any arrangement where the earth is at rest, and thus, the earth revolves around the sun.

### The rope trick

Galileo introduced the rope trick to be able to see things that are $8$ arcseconds small like the shift in the direction of the star. The idea is that if you have a rope that is too far away for you to determine where it is, and then you look during the night, then you can more accurately determine where a star is by seeing when the rope covers it.