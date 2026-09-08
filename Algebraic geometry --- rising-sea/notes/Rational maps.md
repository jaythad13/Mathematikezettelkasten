---
tags:
- rising-sea/7/5
- alg-geo
---

Let $S$ be a base scheme. Let $X$ be a *reduced* scheme and $Y$ be any scheme, all over $S$.

A rational map $X \dashrightarrow Y$ is the data of a map from almost all of $X$ to $Y$, up to equality on almost all of $X$. We will assume the domain $X$ is [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ reduced (schemes)|reduced]] and only define rational maps in this case. They are important because they give:
- a very useful weaker notion than scheme isomorphism
- an equivalence of categories between irreducible $\mathbb{F}$-varieties and finitely generated $\mathbb{F}$-algebras that are fields
- an extension of the classical technique of finding $\mathbb{Q}$-points on a conic by drawing lines
to name just a few applications.

##### _definition:_ rational map, dominant map, composition of dominant maps

A **rational map** $\pi : X \dashrightarrow Y$ from a (reduced) scheme $X$ to a scheme $Y$ is the equivalence class of a [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ morphism of schemes|morphism]] $\alpha : U \to Y$ from a dense open subscheme $U \subseteq X$ under the equivalence relation $\alpha \sim \beta$ (for $\beta : V \to Y$) if there is a dense open $W \subseteq U \cap V$ such that $\alpha_{|W} = \beta_{\mid W}$.

We denote the set of all rational maps $X \dashrightarrow Y$ by $\operatorname{Rat}(X, Y)$.

---

##### _example:_ rational maps between affine and projective spaces

There is a rational map $\mathbb{P}^n \to \mathbb{P}^{n - 1}$ corresponding to [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_example _ affine $(n + 1)$-space covers projective $n$-space|the map we know]] $D_+(x_n) \setminus \{ 0 \} = \mathbb{A}^n \setminus \{ 0 \} \dashrightarrow \mathbb{P}^{n - 1}$.

The morphism $\mathbb{A}^n \to \mathbb{P}^n$ defines a rational map. Also, the morphism $D_{+}(x_{n}) = \mathbb{A}^n \to \mathbb{A}^n$ defines a rational map in the opposite direction. We will see that this is somehow a "rational inverse" and makes $\mathbb{A}^n$ and $\mathbb{P}^n$ "birationally equivalent".

---

It isn't always immediately clear what the largest domain of definition is.

##### _example:_ the Cremona transform

Work over a base field $\mathbb{F}$. Write $U = D_{+}(xyz) \subseteq \mathbb{P}^2$. Consider the morphism $\pi : U \to \mathbb{P}^2$ by $(x : y : z) \mapsto (1 / x : 1 / y : 1 / z)$ in homogeneous coordinates. The **Cremona transform** is its rational equivalence class $\mathbb{P}^2 \dashrightarrow \mathbb{P}^2$.

Note, we can actually extend $\pi$ beyond $U$. Specifically, $xyz$ is non-vanishing on $U$, so [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_example _ some maps to projective space|we can scale the coordinates]] of $\pi$ by $xyz$. On $U$, $\pi$ agrees with $(x : y : z) \mapsto (yz : zx : xy)$. This morphism extends to $D_{+}(yz) \cup D_{+}(zx) \cup D_{+}(xy)$. This is strictly bigger, since it contains each term in the union, each of which is bigger than $D_{+}(xyz)$.

---

##### _proposition:_ rational maps to $\mathbb{A}^1$ represent rational functions

Suppose $X$ is an [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ integral scheme|integral]] scheme. There is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural isomorphism]] of functors $X \mapsto \operatorname{Rat}(X, \mathbb{A}^1)$ and $X \mapsto K(X)$.

###### _proof:_

We work over $\mathbb{Z}$ and just give the bijection. 

A rational map $X \dashrightarrow \mathbb{A}^1$ is determined by the rational equivalence class of a morphism $U \to \mathbb{A}^1$ which [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_proposition _ morphisms to affine schemes|is determined by]] the equivalence class of $f \in \mathscr{O}_{U}(U) = \mathscr{O}_{X}(U)$ (the image of $x \in \mathbb{Z}[x]$) upto identification on open dense sets, which is exactly the equivalence class of $f \in \mathscr{O}_{X, \eta}$ where $\eta$ is the generic point of $X$, which is exactly a choice of rational function.

---

### Dominant and birational maps

Rational maps are most interesting when they have dense image. This topological definition is surprisingly algebraic — we will see that in nice situations these maps are in bijection with maps of [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ rational functions, function field|function fields]] in the opposite direction.

##### _definition:_ dominant map, composition of dominant maps

A rational map $\pi : X \dashrightarrow Y$ is **dominant** if, for some (and hence each) representative $U \to Y$, the image of the map is dense in $Y$.

The **composition of dominant maps** $\pi : X \dashrightarrow Y$ and $\rho : Y \dashrightarrow Z$ represented by $\alpha : U \to Y$ and $\beta : V \to Z$ is the $\rho \circ \pi : X \dashrightarrow Z$, the map represented by $\beta_{\mid V \cap \operatorname{img} \alpha} \circ \alpha$. Note, it is dominant. 

---

##### _lemma:_ dominant maps preserve generic points

A dominant map of integral schemes $\pi : X \dashrightarrow Y$ sends the generic point of $X$ to the generic point of $Y$.

###### _proof:_

Let $X, Y$ have generic points $\eta_{X}, \eta_{Y}$ respectively. Suppose $\pi$ is represented by a morphism $\alpha : U \to Y$. Suppose $\pi(\eta_{X}) = q \in Y$ and let $\overline{\{ q \}}$ be its closure. Then $\pi^\text{pre}(\overline{\{ q \}})$ is a closed set containing $\eta_{X}$, and thus, $X$. Thus, $\overline{\{ q \}}$ is a closed set containing the open dense $\operatorname{img} \alpha$, and thus, containing all of $Y$. That is, $q = \eta_{Y}$.

---

##### _corollary:_ dominant maps induce opposite maps of function fields

A dominant map of integral schemes $\pi : X \dashrightarrow Y$ induces an opposite map $\pi^\sharp : K(Y) \to K(X)$.

###### _proof:_

$\pi^\sharp$ is the [[Algebraic geometry --- rising-sea/notes/Morphisms of ringed spaces#_definition _ induced stalk morphism|induced stalk morphism]].

---

##### _definition:_ birational maps, rational inverse, rational scheme

A rational map $\pi : X \dashrightarrow Y$ is **birational** if it is dominant and there is a **rational inverse** $\rho : Y \dashrightarrow X$ such that $\rho \circ \pi = \operatorname{id}_{X} \in \operatorname{Rat}(X, X)$ and $\pi \circ \rho = \operatorname{id}_{Y} \in \operatorname{Rat}(Y, Y)$.

If $\pi$ is birational, we say $X$ and $Y$ are **birationally equivalent** or **birational** to each other. An integral, finite type $\mathbb{F}$-scheme $X$ is **rational** if it is birational to $\mathbb{A}^n_{\mathbb{F}}$ (or equivalently $\mathbb{P}^n_{\mathbb{F}}$).

---

##### _proposition:_ birational integral schemes are isomorphic almost everywhere

Suppose $X, Y$ are integral schemes. Then $X$ and $Y$ are birational if and only if there are open dense subschemes $U \subseteq X$ and $V \subseteq Y$ such that $U \cong V$.

###### _proof:_

The existence of isomorphic open dense subschemes automatically gives a birational morphism (just the isomorphism of the open subschemes).

The idea to go in the opposite direction is to just cut out everywhere that the maps are not actually inverses, and then notice that everything is still open dense not included in the morphisms in either direction. 

Suppose $\pi : X \dashrightarrow Y, \rho : X \dashrightarrow Y$ are represented by $\alpha : U_{1} \to Y$ and $\beta : V_{1} \to X$. Then, on an open dense $U_{2} \subseteq \alpha^\text{pre}(V_{1})$, $\beta \circ \alpha_{\mid U_{2}} : U_{2} \to X$ is a morphism rationally equivalent to $\operatorname{id}_{X}$. In particular, there is some open dense $U_{3} \subseteq U_{2}$ such that $(\beta \circ \alpha_{\mid U_{2}})_{\mid U_{3}} = \operatorname{id}_{X \mid U_{3}}$.

Consider $V_{3} = \beta^\text{pre}(U_{3})$. Then $\alpha_{\mid U_{3}} \circ \beta_{\mid V_{3}} : V_{3} \to Y$ is a morphism rationally equivalent to $\operatorname{id}_{Y}$. Thus, for some open dense $V_{4} \subseteq V_{3}$ we can write $(\alpha_{\mid U_{3}} \circ \beta_{\mid V_{3}})_{\mid V_{4}} = \operatorname{id}_{X \mid V_{4}}$. Let $\alpha^\text{pre}(V_{4}) = U_{4} \subseteq U_{3}$. Then $\alpha_{\mid U_{4}}$ and $\beta_{\mid V_{4}}$ compose to the identity on both sides.

---

### Rational maps of irreducible varieties

In the case of varieties (and in fact, we will prove this even for non-separated schemes), rational maps really are just homomorphisms of function fields.

##### _proposition:_ function field homomorphisms come from dominant maps

Suppose $X$ is an integral $\mathbb{F}$-scheme and $Y$ is an integral [[Algebraic geometry --- rising-sea/notes/Schemes over a base#_definition _ locally of finite type, finite type|finite type]] $\mathbb{F}$-scheme. For each extension of $\mathbb{F}$-algebras $K(Y) \to K(X)$, there is a dominant rational map of $\mathbb{F}$-schemes $\pi : X \dashrightarrow Y$ such that $\pi^\sharp = \varphi$.

---

Further, each finitely generated field extension of $\mathbb{F}$ arises as the function field of a variety. This gives an equivalence between the category of irreducible affine $\mathbb{F}$-varieties with dominant rational maps (defined over $\mathbb{F}$) and the opposite category of finitely generated field extensions of $\mathbb{F}$ with $\mathbb{F}$-algebra homomorphisms between them.

##### _proposition:_ function fields come from varieties

Each finitely generated $\mathbb{F}$-algebra is the function field of an irreducible affine $\mathbb{F}$-variety.

---

### Rational points from rational maps

We can find (all) $\mathbb{Q}$-points on curves and surfaces using rational maps to things where we already understand the $\mathbb{Q}$-points (we avoid the phrase rational solutions because the two ideas don't seem to be related). For this section we work in the category of $\mathbb{Q}$-schemes.

##### _example:_ Pythagorean triples

We can use a rational map to give a "formula" describing all Pythagorean triples.

We want to find $\mathbb{Q}$-solutions to $x^{2} + y^{2} = 1$. Let $C = \operatorname{Spec} A = \operatorname{Spec} \mathbb{Q}[x, y] / (x^{2} + y^{2} - 1)$. We have at least one point $p = (1, 0) \in C(\mathbb{Q}) \subseteq \mathbb{A}^2(\mathbb{Q})$. For any other $q = (q_{1}, q_{2}) \in C(\mathbb{Q})$ we have a line $p q$ and we can consider its slope $\lambda_{q} = q_{2} / (q_{1} - 1) \in \mathbb{Q}$. Conversely, for each $\lambda \in \mathbb{Q}$, the rational line of slope $\lambda$, through $p$ intersects $C$ at one more point $q_{\lambda} = (\lambda^{2} - 1 / (\lambda^{2} + 1), 2 \lambda / (\lambda^{2} + 1))$.

This gives maps $C(\mathbb{Q}) \to \mathbb{A}^1(\mathbb{Q})$ and $\mathbb{A}^1(\mathbb{Q}) \to C(\mathbb{Q})$ that come from rational maps. $C \dashrightarrow \mathbb{A}^1$ is represented by a morphism $D(x - 1) \to \mathbb{A}^1$. The morphism corresponds to $\mathbb{Q}[z] \to A[(x - 1)^{-1}]$ with $f(z) \mapsto f(y / (x - 1))$ on rings. $\mathbb{A}^1 \dashrightarrow C$ is defined on $D(z^{2} + 1)$. It corresponds to the homomorphism $A \to \mathbb{Q}[z, (z^{2} + 1)]$ by $f(x, y) \mapsto f(z^{2} - 1 / (z^{2} + 1), 2z / (z^{2} + 1))$.

We can extend $C \dashrightarrow \mathbb{A}^1$ to a rational map $C \dashrightarrow \mathbb{P}^1$ in the obvious way. As a [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_example _ some maps to projective space|morphism to projective space]], it can be described by the choice of $y, x - 1$ as a pair of functions, not vanishing simultaneously on $D(x - 1) \subseteq C$. However, this map is actually equivalent to an honest morphism of schemes $C \to \mathbb{P}^1$. This is a special case of a general theorem extending morphisms from punctured curves to the whole curve.

---

Here, the formula came first and then we interpreted it as coming from a birational map. However, there are many natural ways to get a birational map to $\mathbb{P}^n$. Finding all the $\mathbb{Q}$-points is just a matter of understanding the inverse map and dealing with the locus where it is not defined.

##### _example:_ rational points on a nodal cubic elliptic curve

We can find all $\mathbb{Q}$-points on $C = \operatorname{Spec} A = \operatorname{Spec} \mathbb{Q}[x, y] / (y^{2} - x^{3} - x^{2})$ by giving a birational map $C \dashrightarrow \mathbb{A}^1$ by projecting from a point again.

---

###### _example:_ rational points on a quadric surface

Similarly, we can find all $\mathbb{Q}$-points on the quadric surface $Q \subseteq \mathbb{P}^3$ given by $\operatorname{Proj} S_{\bullet} = \operatorname{Proj} \mathbb{Q}[x, y, z, w] / (x^{2} + y^{2} - w^{2} - z^{2})$.

---

### Infinite descent and non-rational curves

An interesting fact is that there exist curves $C$ over $\mathbb{C}$ with no non-constant rational maps $\mathbb{P}^1 \dashrightarrow C$. In some sense, this is saying that all the $\operatorname{Spec} \mathbb{C}(t)$-points of $C$ actually factor through $\operatorname{Spec} \mathbb{C}$ — they are all closed points.

If we were to replace $\mathbb{C}(t)$ with $\mathbb{Q}$, these are deep number-theoretic questions. This is a first taste of the parallelism between number fields and function fields of curves. For this section, we work in the category of $\mathbb{C}$-schemes.

##### _example:_ function field Fermat's last theorem

Suppose $n > 2$. Let $C = V(x^n + y^n - z^n) \subseteq \mathbb{P}^{2}$. Then $\mathbb{P}^1$ has no dominant rational maps to $C$.

---

This gives an example of two smooth complex curves with no isomorphic open subschemes.

##### _example:_ $\mathbb{C}(t)$-points of an elliptic curve

Suppose $C = \operatorname{Spec} \mathbb{C}[x, y] / (y^{2} - f(x))$ where $f(x) = (x - a)(x - b)(x - c)$ and $a, b, c$ are three distinct complex numbers. Then all $\mathbb{C}(t)$-points $\operatorname{Spec} \mathbb{C}(t) \to C$ factor through $\operatorname{Spec} \mathbb{C}$.

---

Once we know what genus is and thoroughly understand it, we will see that these theorems are really just the fact that the genus $0$ curve $\mathbb{P}^1$ has no maps to higher genus curves.