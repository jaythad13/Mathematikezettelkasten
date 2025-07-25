---
tags:
- vsrp
- s-k-roushan
- alg-top
---

##### _definition:_ homotopy equivalence

Let $X, Y$ be topological spaces with $f : X \to Y$ and $g : Y \to X$ [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous maps]] between them. $X$ and $Y$ are homotopy equivalent (or have the same homotopy type) if $f \circ g$ is [[Topology --- math-147/notes/Homotopy#_definition _ homotopic, homotopy, homotopic relative to|homotopic]] to the identity $\operatorname{id}_{Y}$ on $Y$ and similarly $g \circ f \simeq \operatorname{id}_{X}$.

##### _example:_ mapping cylinder, strong deformation retract

For a continuous map $f : X \to Y$ the mapping cylinder $M_{f}$ is the space $X \times I \sqcup Y / \sim$ where $\sim$ identifies the top of the cylinder $X \times \{ 1 \}$ with the images of the corresponding points under $f$. That is $(x, 1) \sim f(x)$. Then $Y \to M_{f}$ is an inclusion and together with $M_{f} \to Y$ by $(x, t) \mapsto f(x)$ gives a homotopy equivalence (just slide everything down the cylinder). 

Since $Y \subseteq M_{f}$ and the homotopy is [[Topology --- math-147/notes/Homotopy#_definition _ homotopic, homotopy, homotopic relative to|relative to]] $Y$, this is a strong deformation retract. Other examples of strong deformation retract are the contractions of $\mathbb{D}^n$ to a single point, or the right angled triangle to two lines (which has homology invariance given by [[Simplicial homology and random walks --- math-145/notes/Whitehead equivalence#_definition _ elementary collapse, elementary expansion|elementary collapse]] for simplicial complexes).

### CW-complexes and Whitehead equivalence

##### _definition:_ (finite) CW-complex

Let $K^0$ be any discrete set. An $n$-dimensional CW-complex $X$ with $0$-skeleton $K_{0}$ is defined by induction as
$$
X = K^n = \left( K^{n - 1} \cup \bigcup_{\alpha} I_{\alpha}^n \right) / \sim
$$
where each $I_{\alpha}^n \cong [0, 1]^n$ and comes with an attaching map $\varphi_{\alpha}^n : \partial I_{\alpha}^n \to K^{n - 1}$, $\sim$ identifies $\operatorname{img} \varphi_{\alpha}^n$ and $\partial I_{\alpha}^n$, and $\alpha$ varies over a finite indexing set.

Each $I_{\alpha}^k \subseteq X$ is called a $k$-cell.

We can define 

##### _definition:_

##### _definition:_ simple homotopy equivalence

A continuous map $f : X \to Y$ is a simple homotopy equivalence if it is homotopic to a Whitehead equivalence.

We want to know if any Whitehead equivalence of CW-complexes 

##### _example:_ Bing's house with two rooms

Construct the house as three discs with holes cut out appropriately. Then fill the holes with wax. Now you're homotopy equivalent to a cylinder. Since this gives the house with two rooms as a strong deformation retract of the cylinder, a contractible space, the house with two rooms is contractible as well.

We can reduce checking homotopy equivalences to checking them on mapping cylinders.

##### _proposition:_ checking simple homotopy equivalences on mapping cylinders

If $f : X \to Y$ is cellular, then $f$ is a simple homotopy equivalence if and only if $X \to M_{f}$ is a simple homotopy equivalence.

This allows us to restrict to the case of maps $f : X \to Y$ with $Y \subseteq X$ and now we do all the actual algebraic topology.