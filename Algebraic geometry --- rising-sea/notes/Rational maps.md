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