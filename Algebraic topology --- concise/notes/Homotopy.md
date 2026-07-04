---
tags:
- math-147
- top
- alg-top
- uc-2026/alg-top/3
---

In algebraic topology, our goal is to classify (nice) spaces up to [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphism]]. In practice, this is really difficult to do. While we have seen many homeomorphism invariants (like say, [[Topology --- math-147/notes/Compactness#_proposition _ compactness is preserved by continuous functions|compactness]] and [[Topology --- math-147/notes/Connectedness and path-connectedness#_proposition _ continuous functions preserve connectedness|connectedness]]) they aren't enough alone. For example, the $2$-sphere and the torus are both compact, connected, metrisable, [[Topology --- math-147/notes/Size restrictions#_definition _ second countable|second countable]] but we can see that they are not homeomorphic. On the other hand, directly checking homeomorphism is very difficult as well. Thus, we define a weaker notion of equivalence and invariants that come along with it in homotopy.

Homotopy captures the notion of being able to deform a map into another continuously. Considering these deformations allows a wider class of spaces to be considered equivalent, and makes computations easier. 

##### _definition:_ homotopic, homotopy, homotopic relative to

If $f, g : X \to Y$ are [[Topology --- math-147/notes/Continuous functions#_definition _ continuity|continuous maps]] of topological spaces, then $f$ is **homotopic to** $g$, denoted $f \simeq g$ if there is a continuous function $H : X \times [0, 1] \to Y$ such that $H(x, 0) = f(x)$ and $H(x, 1) = g(x)$ for all $x \in X$.

$H$ is called a **homotopy witnessing $f \simeq g$**.

For any $A \subseteq X$ the two continuous functions $f, g$ are **homotopic relative to $A$** if there is a homotopy $H$ witnessing $f \simeq g$ with $t \mapsto H(a, t)$ constant for each $a \in A$ (that is, $H(a, t) = f(a) = g(a)$ for each $t$).

---

##### _example:_ the straight line homotopy

Any two continuous functions $f, g : X \to \mathbb{R}^n$ are homotopic by the straight line homotopy $H : X \times [0, 1] \to \mathbb{R}^n$ by
$$
H(x, t) = (1 - t) f(x) + t g(x).
$$

---

Homotopically trivial maps are those that can be deformed into a constant function.

##### _example:_ every map is homeomorphic to itself

Use the constant homotopy $H(x, t) = f(x)$ for all $t$.

---

##### _definition:_ null homotopic

If $f : X \to Y$ is homotopic to a constant function $X \to Y$, then $f$ is **null-homotopic**.

---

##### _example:_ every map into $\mathbb{R}^n$ is null-homotopic

Just apply the straight line homotopy.

---

We should verify that this notion of deformation really deserves the $\simeq$ symbol, and really does carry enough information for us to achieve our goal of classifying nice spaces.

##### _example:_ pushforward homotopy

Perhaps the most important example of a homotopy is the **pushforward homotopy** which allows us to turn homotopies of maps $X \to Y$ to homotopies of maps $X \to Y \to Z$. 

Suppose $f, g : X \to Y$ are homotopic with homotopy witnessed by $H$. Then, for any $h : Y \to Z$ there is a homotopy $h \circ H$ between $h \circ f$ and $h \circ g$.

---

##### _proposition:_ homotopy forms an equivalence relation

Given topological spaces $X, Y$ and $A \subseteq X$, then homotopy relative to $A$ is an equivalence relation on the set of continuous functions $X \to Y$. Note, by choosing $A = \text{Ø}$ we get that 

###### _proof sketch:_

Let $f, g, h : X \to Y$ be continuous maps.

We've already seen that $f \simeq f$. If $f \simeq g$ is witnessed by $H$, then $g \simeq f$ is witnessed by $(x, t) \mapsto H(x, 1 - t)$. 

Finally, suppose $f \simeq g$ is witnessed by $H$ and $g \simeq h$ is witnessed by $G$. Since $[0, 1]$ is homeomorphic to $[1, 2]$, we have equivalently, $G' : X \times [1, 2] \to Y$ with $G'(x, 1) = g(x)$ and $G'(x, 2) = h(x)$. Apply the [[Topology --- math-147/notes/Continuous functions#_lemma _ the gluing lemma|gluing lemma]] to get $F : X \times [0, 2] \to Y$ with $F(x, 0) = f(x)$ and $F(x, 2) = h(x)$ and finally use the homeomorphism between $[0, 1]$ and $[0, 2]$ to get $F' : X \times [0, 1] \to Y$ witnessing $f \simeq h$. Since $F$ is always equal to either $H$ or $G$, it inherits the property of fixing $a \in A$ from them.

---

All of this allows us to define a relaxation of the notion of [[Topology --- math-147/notes/Homeomorphisms#_definition _ homeomorphism|homeomorphism]] of spaces.

##### _definition:_ homotopy equivalence

Two spaces are **homotopy equivalent**, denoted $X \simeq Y$ if there are maps $f : X \to Y$ and $g : Y \to X$ such that $f \circ g \simeq \operatorname{id}_{Y}$ and $g \circ f \simeq \operatorname{id}_{X}$.

---

##### _example:_ straight line homotopy

The straight line homotopy is really giving a homotopy equivalence between $\mathbb{R}^n$ and the one point space. It suffices to give a homotopy between $\operatorname{id}_{\mathbb{R}^n}$ and the constant map at $0$. There is such a homotopy given by $H : \mathbb{R}^n \times [0, 1] \to \mathbb{R}^n$ with $H(x, t) = (1 - t) x$.

---