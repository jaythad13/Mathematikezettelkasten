---
tags:
- rising-sea/2/2
- alg-geo
- alg-top
---

Let $X$ and $Y$ be topological spaces.

Pushforwards transport a [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf|(pre)sheaf]] along a continuous map in the obvious way.

##### _definition:_ pushforward/direct image presheaves and sheaves

Suppose $\pi : X \to Y$ is a continuous map and $\mathscr{F}$ is a (pre)sheaf on $X$. Then **the pushforward of $\mathscr{F}$ under $\pi$** is $\pi_{*} \mathscr{F}$, a (pre)sheaf on $Y$ defined by $\pi_{*} \mathscr{F}(U) = \mathscr{F}(\pi^\text{pre}(U))$. The restriction maps $\operatorname{res}_{U, V}$ are just the restriction maps $\operatorname{res}_{\pi^\text{pre}(U), \pi^\text{pre}(V)}$.

---

It is necessary to verify that this really is a presheaf, and a sheaf when $\mathscr{F}$ is.

Since the restriction maps are the same, they commute as desired, and so $\pi_{*} \mathscr{F}$ is a presheaf.

Suppose $\mathscr{F}$ is a sheaf on $X$. Then $s_{i} \in \mathscr{F}(U_{i})$ agreeing on intersections glue to a unique $s \in U = \mathscr{F}(\bigcup_{i} U_{i})$. Suppose we have $V_{i} \subseteq Y$ with preimages $U_{i} \subseteq X$ and $s_{i} \in \pi_{*} \mathscr{F}(V_{i}) = \mathscr{F}(U_{i})$ agreeing on restriction to intersections $V_{i} \cap V_{j}$. Then the $s_{i}$ agree on restrictions to $U_{i} \cap U_{j} = \pi^\text{pre}(V_{i} \cap V_{j})$. Thus, they glue to a unique $s \in \mathscr{F}\left( \bigcup_{i} U_{i} \right)$. But since $\bigcup_{i} U_{i} = \pi^\text{pre}\left( \bigcup_{i} V_{i} \right)$, we have $s \in \pi_{*} \mathscr{F}\left( \bigcup_{i} V_{i} \right)$. Since the restriction maps commute with $\pi^\text{pre}$, the $s_{i}$ still glue to $s$ in the pushforward sheaf.

One abstract nonsense proof (once we've defined the [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves|category of sheaves]] on a space) is that $\pi_{*} : \mathscr{F} \to \pi_{*} \mathscr{F}$ is a [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|right adjoint functor]] (to the inverse image functor) from sheaves on $X$ to sheaves on $Y$. Since [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ right adjoints preserve limits|right adjoints preserve limits]], they preserve the limit —
$$
\lim_{ j \in \mathscr{J} } \mathscr{F}_{\mid U_{j}} = \mathscr{F}_{\mid U} \implies \lim_{j \in \mathscr{J}} \pi_{*} \mathscr{F}_{V_{j}} = \pi_{*} \mathscr{F}_{\mid V}.
$$

---
##### _example:_ the skyscraper sheaf is a pushforward

Really [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ skyscraper sheaves|the skyscraper sheaf]] is a combination of the ideas of a constant sheaf and an inverse image sheaf. It is the pushforward of the constant sheaf $\underline{S}$ on the one point space $\{ p \}$ under the inclusion $i_{p} : \{ p \} \to X$. Hence the horrendous notation $i_{p, *} \underline{S}$.

---

##### _proposition:_ pushforwards induce morphisms of stalks

Suppose $\pi : X \to Y$ is continuous with $\pi(p) = q$ and $\mathscr{F}$ is a sheaf on $X$. Then there is a natural morphism of [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|stalks]] $\pi_{*} \mathscr{F}_{q} \to \mathscr{F}_{p}$.

###### _proof:_

$\pi_{*} \mathscr{F}_{q}$ is the colimit of all $\pi_{*} \mathscr{F}(V) = \mathscr{F}(U)$ with $U = \pi^\text{pre}(V)$ and $p \in V$ (with the restriction maps between them). $\mathscr{F}_{p}$ is the colimit of all $\mathscr{F}(U)$, and thus, has maps from all $\pi_{*}\mathscr{F}(V)$ commuting with the restriction maps between them. The natural morphism is the one given by the universal property of the colimit. 

The maps sends a germ $s_{q} \in \pi_{*} \mathscr{F}_{q}$ corresponding to some $s \in \pi_{*} \mathscr{F}(V) = \mathscr{F}(U)$  to the equivalence class of $s$ in $\mathscr{F}_{p}$. Note that the equivalence classes in $\mathscr{F}_{p}$ are smaller since there are more conditions imposed by the more $\mathscr{F}(U)$s than $\pi_{*} \mathscr{F}(V)$s.

---

Since sheaves on $X$ (with values in a particular category) [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves|form a category of their own]], we can make sense of the fact that pushforward is functorial.

##### _proposition:_ pushforward is functorial

Suppose $\pi : X \to Y$ is continuous. Then pushforward of (pre)sheaves (with value in $\mathscr{C}$) gives a functor $\pi_{*} : \mathscr{C}_{X} \to \mathscr{C}_{Y}$.

###### _proof sketch:_

$\pi_{*}$ is defined on objects by $\mathscr{F} \mapsto \pi_{*} \mathscr{F}$. Suppose $\varphi : \mathscr{F} \to \mathscr{G}$ is a morphism of (pre)sheaves. Then we can define a (pre)sheaf morphism $\pi_{*} \varphi : \pi_{*} \mathscr{F} \to \pi_{*} \mathscr{G}$ by $\pi_{*} \varphi(V) = \varphi(U)$ for $\pi^\text{pre}(V) = U$. For $V_{1} \subseteq V_{2}$ with pre-images $U_{1} \subseteq U_{2}$ the [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|relevant diagram]] commutes — the two morphisms are the same $\pi_{*} \mathscr{F}(V_{2}) \to \pi_{*}\mathscr{G}(V_{1})$ because they are exactly the two morphism $\mathscr{F}(U_{2}) \to \mathscr{G}(U_{1})$ which agree.

---

In fact, when the sheaves are valued in an abelian category $\mathscr{C}$, this functoriality is fairly nice.

##### _proposition:_ pushforward is left-exact

Suppose $\pi : X \to Y$ is a continuous map. Then $\pi_{*}$ is a [[Algebraic geometry --- rising-sea/notes/Exact functors#_definition _ right-exact, left-exact, exact|left-exact]] functor $\mathscr{C}_{X} \to \mathscr{C}_{Y}$.

###### _proof:_

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{F} \ar[r, "\varphi"] & \mathcal{G} \ar[r, "\psi"] & \mathcal{H}
	\end{tikzcd}
\end{document}
```
is an exact sequence in $\mathscr{C}_{X}$. We want to show
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \pi_{*}\mathcal{F} \ar[r, "\pi_{*}\varphi"] & \pi_{*}\mathcal{G} \ar[r, "\pi_{*}\psi"] & \pi_{*}\mathcal{H}
	\end{tikzcd}
\end{document}
```
is an exact sequence in $\mathscr{C}_{Y}$.

Suppose $V \subseteq Y$ has preimage $U$ under $\pi$. Then $\pi_{*}\varphi(V) = \varphi(U)$ and $\pi_{*}\psi(V) = \psi(U)$. But $\varphi(U) : \mathscr{F}(U) \to \mathscr{G}(U)$ is exactly the kernel of $\psi(U)$. Equivalently, $\pi_{*} \varphi(V)$ is the kernel of $\pi_{*} \psi(V)$, [[Algebraic geometry --- rising-sea/notes/Sheaves valued in abelian categories#_proposition _ presheaf kernel is a sheaf and a kernel|so]] $\pi_{*} \varphi$ is the kernel of $\pi_{*} \psi$.

---