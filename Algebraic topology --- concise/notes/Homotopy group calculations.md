---
tags:
- math-147
- concise
- uc-2026
- alg-top
---

From relatively few computational tools, and some computations on basic spaces, we can compute quite a lot of [[Algebraic topology --- concise/notes/The fundamental group#_definition _ fundamental group|fundamental groups]]! Many of these properties apply to [[Algebraic topology --- concise/notes/Higher homotopy groups#_definition _ $n$th homotopy group of a space|higher homotopy groups]] as well, so we state them in that generality when possible,

### Properties of homotopy groups

First, for nice enough $X$, we can forget the base point.

##### _proposition:_ homotopy groups are invariant on path components

Suppose $X$ is a topological space with $p, q \in X$ connected by a [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path|path]] $\alpha : [0, 1] \to X$. Then $\alpha$ determines an isomorphism $\alpha_{\pi_{n}} : \pi_{n}(X, p) \to \pi_{n}(X, q)$. 

If $\pi_{1}(X, p)$ is abelian, then $\alpha_{\pi_{1}} = \alpha'_{\pi_{1}}$ for any two paths $\alpha, \alpha'$ connecting $p$ and $q$.

###### _proof sketch:_

We only give the proof for the case of $\pi_{1}$. Suppose $\alpha(0) = p$ and $\alpha(1) = q$. Then it defines $\pi_{1}(X, p) \to \pi_{1}(X, q)$ by $[\gamma] \mapsto [\alpha]^{-1} [\gamma] [\alpha]$. See the [[Topology --- math-147/attachments/homework/hw 9/hw 9.pdf#page=4|homework]] for why this is an isomorphism.

Suppose $\pi_{1}(X, p)$ is abelian. Then
$$
\begin{align}
\alpha_{\pi_{1}}(\gamma) \alpha_{\pi_{1}}'(\gamma)^{-1} & = [\alpha]^{-1} [\gamma] [\alpha] ([\alpha']^{-1} [\gamma] [\alpha'])^{-1} \\
 & = [\alpha]^{-1} [\gamma] [\alpha \alpha'^{-1}] [\gamma]^{-1} [\alpha'] \\
 & = [\alpha]^{-1}[\alpha \alpha'^{-1}] [\gamma][\gamma]^{-1} [\alpha'] \\
 & = [\alpha']^{-1} [\alpha'] \\
 & = e.
\end{align}
$$

---

As a corollary, we have canonical homotopy groups of a [[Topology --- math-147/notes/Connectedness and path-connectedness#_definition _ path-connected|path-connected]] space $X$. We denote these $\pi_{n}(X)$.

The most important properties are that the homotopy groups are [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ (covariant, contravariant) functors|functorial]] and [[Algebraic topology --- concise/notes/Homotopy#_definition _ homotopy equivalence|homotopy]]-invariant.

##### _proposition:_ homotopy groups are functorial

For each continuous map of pointed spaces $f : X, x \to Y, y$ there is a functorial homomorphism of homotopy groups $f_{*} : \pi_{n}(X, x) \to \pi_{n}(Y, y)$ for each $n$.

###### _proof sketch:_

The homomorphism is given by $f_{*}[\gamma] = [f \circ \gamma]$. For proof that this is well-defined on homotopy classes, we can use the [[Simplicial homology and random walks --- math-145/notes/Loops and homotopies#_theorem _ pushforward homotopy|pushforward homotopy]]. For proof that this is a group homomorphism, see the [[Topology --- math-147/attachments/homework/hw 10/hw 10.pdf#page=3|homework]].

---

##### _proposition:_ homotopy groups are homotopy invariant

Any two homotopic maps $f, g : X, x \to Y, y$ induce the same maps $f_{*} = g_{*} : \pi_{n}(X, x) \to \pi_{n}(Y, y)$ on homotopy, for each $n$.

More generally, for any two homotopic maps $f, g : X \to Y$ (not necessarily respecting the base point) and the path $\alpha$ from $f(x)$ to $g(x)$ determined by the homotopy, the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& \pi_{1}(X, x) \ar[ld, "f_{*}"] \ar[rd, "g_{*}"] \\
		\pi_{1}(Y, f(x)) \ar[rr, "\alpha_{\pi_{1}}"] && \pi_{1}(Y, g(x))
	\end{tikzcd}
\end{document}
```

###### _proof sketch:_

Note that the first follows from the second in the case that $f(x) = g(y)$ by choosing $\alpha$ to be the constant path. Suppose $f \simeq g$ is witnessed by the homotopy $H : X \times [0, 1] \to Y$. Let $[\gamma] \in \pi_{1}(X, x)$. Then $\alpha_{\pi_{1}}(f_{*}[\gamma]) = [\alpha ^{-1}][f \circ \gamma][\alpha]$ and $g_{*}[\gamma] = [g \circ \gamma]$. 

We already have a homotopy between $f \circ \gamma$ and $g \circ \gamma$ by $H \circ (f, \operatorname{id}_{[0, 1]})$ but it is not a path homotopy (it is not relative to $\{ 0, 1 \}$). We also know $\alpha(t) = H(0, t) = H(1, t)$. We can think of this as a square with $f \circ \gamma$ along the bottom edge, $g \circ \gamma$ along the top edge, and $\alpha$ along the side edges. We can replace $g \circ \gamma$ with $[e_{g(x)}][g \circ \gamma][e_{g(x)}]$ where $e_{g(x)}$ is the constant map at $g(x)$. Then, we can bend this new square again, so that $g \circ \gamma$ is along the top, the constant maps are on the sides, and the bottom is now $[\alpha ^{-1}][f \circ \gamma][\alpha]$ as desired.

---

As a corollary, we get that homotopy groups are homotopy equivalence invariant.

##### _corollary:_ homotopy groups are homotopy equivalence invariant

Suppose $X, Y$ are homotopy equivalent spaces. Then $\pi_{n}(X) \cong \pi_{n}(Y)$ for all $n$.

---

We also have a nice algebraic property.

##### _proposition:_ homotopy groups preserve products

Suppose $X, x$ and $Y, y$ are two path-connected spaces. Then
$$
\pi_{1}(X \times Y, (x, y)) \cong \pi_{1}(X, x) \times \pi_{1}(Y, y).
$$

###### _proof sketch:_

The isomorphism is the product of the pushforwards of the projections $X \times Y \to X$ and $X \times Y \to Y$. Then everything follows component-wise (including the homotopies). For details, see the [[Topology --- math-147/attachments/homework/hw 10/hw 10.pdf#page=1|homework]].

---

### Concrete calculations

Now we can compute some fundamental groups!

##### _proposition:_ Euclidean space is simply connected

For each $n$, $\pi_{1}(\mathbb{R}^n) = 0$.

###### _proof:_

Any two continuous functions $[0, 1] \to \mathbb{R}^n$ are [[Algebraic topology --- concise/notes/Homotopy#_example _ the straight line homotopy|homotopic]]. Equivalently $\mathbb{R}^n$ is homotopy equivalent to the one point space, and so $\pi_{1}(\mathbb{R}^n) \cong \pi_{1}( * ) = 0$.

---

By stereographic projection, this implies $\pi_{1}(S^{2} \setminus \{ * \}) = 0$. In fact, we can extend this to the whole sphere.

##### _proposition:_ the $2$-sphere is simply connected

$\pi_{1}(S^{2}) = 0$.

###### _proof:_

Write $S^{2} = U \cup V$ with $U, V \cong \mathbb{R}^{2}$ via stereographic projection from opposite poles.

---

The calculation of $\pi_{1}(S^1)$ is a first example of the general idea of a covering space. For this, we fulfil our promise that some technical lemmas about paths and path homotopies would be useful.

![[Algebraic topology --- concise/notes/The fundamental group#_lemma _ paths can be understood locally|The fundamental group]]

![[Algebraic topology --- concise/notes/The fundamental group#_lemma _ path homotopies can be understood locally|The fundamental group]]

##### _proposition:_ fundamental group of the circle

$\pi_{1}(S^1) = \mathbb{Z}$.

###### _proof:_

We use the regular embedding $S^1 \subseteq \mathbb{C}$ and choose $*$ to be the base point $1 \in \mathbb{C}$

Let $f : \mathbb{R} \to S^1$ be given by $f(t) = e^{2 \pi i t}$. Write, for each $a \in [0, 1)$ and $n \in \mathbb{Z}$, the open interval $U_{a, n} = (a + n, a + n + 1)$. $f$ is a homeomorphism on each $U_{a, n}$, mapping it onto the open set $V_{a} = S^1 \setminus \{ e^{2 \pi i a} \}$. We claim that for each (path homotopy class of) $\gamma : [0, 1] \to S^1$, there is a unique (path homotopy class of) $\widetilde{\gamma} : [0, 1] \to \mathbb{R}$ such that $\widetilde{\gamma}(0) = 0$ and $\gamma = f \circ \widetilde{\gamma}$. We say such a $\widetilde{\gamma}$ is a **lift** of $\gamma$.

Consider the open covers $\{ U_{a, n} \}$ of $\mathbb{R}$ and $\{ V_{a} \}$ of $S^1$. Divide $[0, 1]$ into $k$ subintervals $I_{i}$ such that each $I_{i}$ has $\gamma^\text{img}(I_{i}) \subseteq V_{a_{i}}$. Choose the unique pre-image $U_{a_{1}, n_{1}} = f^\text{pre}(V_{a_{1}})$ with $0 \in U_{a_{1}, n_{1}}$ and choose $\widetilde{\gamma}_{\mid I_{1}} = f^{-1}_{\mid U_{a_{1}, n_{1}}} \circ \gamma_{\mid I_{1}}$. Inductively choose the unique pre-image $U_{a_{i + 1}, n_{i + 1}}$ containing $\widetilde{\gamma}_{\mid I_{i}}(i / k)$ and choose $\widetilde{\gamma}_{\mid I_{i + 1}} = f^{-1}_{\mid U_{a_{i + 1}, n_{i + 1}}} \circ \gamma_{\mid I_{i + 1}}$. Note that this path is unique on the nose (not just up to homotopy).

If $\gamma \simeq \gamma'$, do the same thing to lift the homotopy $H$ witnessing it to a homotopy $\widetilde{H}$ witnessing $\widetilde{\gamma} \simeq \widetilde{\gamma}'$. One can check that this is a a homotopy relative to the endpoints — $H(0, t) = f(0)$ can be thought of as a constant path at $f(0)$. Thus, it lifts uniquely to the constant path at $0 \in \mathbb{R}$. Similarly for the other end point. 

Consider $\varphi : \mathbb{Z} \to \pi_{1}(S^1)$ by $n \mapsto [\gamma_{n}]$, where $\gamma_{n}(t) = e^{2 \pi i n t}$. It's easy to see this is really a homomorphism — $[\gamma_{m}][\gamma_{n}] = [\gamma_{m + n}]$. $\varphi$ is injective — for distinct $m, n \in \mathbb{Z}$, $\gamma_{m}$ and $\gamma_{n}$ admit distinct lifts with $\widetilde{\gamma_{m}}(1) = m \neq n \neq \widetilde{\gamma_{n}}(1)$. $\varphi$ is also surjective. Consider $[\gamma] \in \pi_{1}(S^1)$ lifting to $\widetilde{\gamma}$ with $\widetilde{\gamma}(1) = n$. In $\mathbb{R}$, [[Algebraic topology --- concise/notes/The fundamental group#_example _ any two paths in $ mathbb{R} n$ with the same endpoint are homotopic|any two paths with the same endpoint are homotopic]]. Thus, $\widetilde{\gamma} \simeq \widetilde{\gamma_{n}}$. This [[Algebraic topology --- concise/notes/Homotopy#_example _ pushforward homotopy|pushes forward]] to a homotopy $\gamma \simeq \gamma_{n}$.

---

### Applications

With the fact that $\pi_{1}(S^1) \cong \mathbb{Z}$, we can prove some very neat theorems.

##### _lemma:_ the disc does not retract to the circle

Let $i : S^1 \to B^{2}$ be the inclusion of the circle into the disc. There is no continuous map $r : B^{2} \to S^1$ such that $r \circ i = \operatorname{id}_{S^1}$.

###### _proof:_

Any continuous map $r : B^{2} \to S^1$ gives a composite homomorphism $r_{*} \circ i_{*} : \pi_{1}(S^1) \to \pi_{1}(B^{2}) \to \pi_{1}(S^1)$. Since $\pi_{1}(B^{2}) = 0$, this map must be the trivial map. Thus, $r_{*} \circ i_{*} \neq \operatorname{id}_{S^1, *}$ and $r \circ i \neq \operatorname{id}_{S^1}$.

---

##### _theorem:_ the Brouwer fixed point theorem

Any continuous map $f : B^{2} \to B^{2}$ has a fixed point $x$ with $f(x) = x$.

###### _proof:_

Suppose, by way of contradiction, that $f$ has no fixed points. Then we can define a continuous function $r : B^{2} \to S^1$ by $r(x) = x + \lambda(x) (f(x) - x)$. Here $\lambda : B^{2} \to \mathbb{R}$ is a continuous function scaling so that $r(x)$ is the intersection of the ray from $x$ to $f(x)$ with the circle. But then $r \circ i = \operatorname{id}_{S^1}$ contradicting the previous lemma.

---

We can also give a different, topological proof of the fundamental theorem of algebra!

##### _definition:_ degree

The (topological) **degree** of a continuous map $f : S^1 \to S^1$ is the integer $\deg f \in \mathbb{Z}$, the image of the generator $1 \in \pi_{1}(S^1, *)$ under the map $\pi_{1}\gamma \circ f_{*} : \pi_{1}(S^1, *) \to \pi_{1}(S^1, f(*)) \to \pi_{1}(S^1, *)$ (where $\gamma$ is a path from $*$ to $f(*)$).

---

Note, by our result about invariance of base point and the fact that $\pi_{1}(S^1) \cong \mathbb{Z}$ is abelian, the definition of degree does not depend on a choice of $\gamma$, nor on $*$, $f$, or $f(*)$.

##### _theorem:_ the fundamental theorem of algebra

Any non-constant polynomial $p : \mathbb{C} \to \mathbb{C}$ has a root.

###### _proof:_

Since $p$ is non-constant we can always find some embedding of the circle into $\mathbb{C}$ where $p$ has no roots. Without loss of generality, assume this is the unit circle. Then we can define $f : S^1 \to S^1$ by $f(z) = p(z) / \lvert p(z) \rvert$. 

If $p(z) \neq 0$ for all $z$ with $\lvert z \rvert < 1$, then there is a homotopy between the constant map $f(0)$ and $f$. Specifically, $H(z, t) = f(tz)$ is this homotopy. Thus, if $p$ doesn't vanish on the disc, $\deg f = 0$.

Let $\deg p = n$ be the polynomial degree of $p$. If $p(z) \neq 0$ for all $z$ with $\lvert z \rvert > 1$, then there is a homotopy between the map $f_{n}(z) = z^n$ and $f$. Specifically, write $H'(z, t) = t^n p(z / t)$ and write $H(z, t) = H'(z, t) / \lvert H'(z, t) \rvert$. 

---

Similarly, we can find the number of roots in the unit disc using $\pi_{1}(S^1)$.

##### _theorem:_ counting roots in the unit disc

Suppose $p : \mathbb{C} \to \mathbb{C}$ is a polynomial with no roots on $S^1$. Then $p$ has $\deg f$ (topological degree) roots (counting multiplicities) $z$ with $\lvert z \rvert < 1$ for $f(z) = p(z) / \lvert p(z) \rvert$.

---