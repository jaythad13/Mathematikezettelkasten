---
tags:
- alg-top
- uc-2026/alg-top/10
- uc-2026/alg-top/11
- uc-2026/alg-top/12
- peter-may
---

Let $\operatorname{Vect}_{G}$ the contravariant vector bundle functor $\mathsf{Top} \to \mathsf{Set}$ by $X \mapsto \operatorname{Vect}_{G} X$. Then for $f : X \to Y$ we have pullback of vector bundles $f^* : \operatorname{Vect}_{G} Y \to \operatorname{Vect}_{G} X$.

##### _definition:_ characteristic class

Let $E^\bullet$ be a cohomology theory. A **characteristic class** with values in $E^\bullet$ is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of ($\mathsf{Set}$-valued) functors $\operatorname{Vect}_{G} \to E^\bullet$.

---

Note we are purposely vague about $G$ because this works for any $G$.

By the [[UChicago --- uc-2026/notes/Classifying spaces#_definition _ classifying space|classification of vector bundles]] and [[Algebraic geometry --- rising-sea/notes/Yoneda's lemma#_lemma _ Yoneda's fanciest lemma|Yoneda's lemma]] it suffices to understand cohomology of $BG$.

##### _proposition:_ characteristic classes are classified by cohomology of $BG$

The set of characteristic classes valued in $E^\bullet$ is in bijection with $E^\bullet(BG)$.

###### _proof:_

Work in the homotopy category $\mathsf{hTop}$. $\operatorname{Vect}_{G}$ is naturally isomorphic to the [[Algebraic geometry --- rising-sea/notes/Functors#_example _ the functor of points and its opposite|functor of points]] $h^{BG}$ by definition of $BG$. Characteristic classes are then natural transformations $h^{BG} \to E^\bullet$. But then, by Yoneda these are in bijection with $E^\bullet(BG)$.

---

### Chern classes

We can classify complex vector bundles over $X$ by $B\mathrm{U}$ where $\mathrm{U}$ is the colimit of all unitary groups $\mathrm{U}_{n}$. Thus, the cohomology of $B\mathrm{U}_{n}$ gives us characteristic classes. 

We will compute homology of $V_{k}(\mathbb{C}^n)$ for each $k, n$ with the fibration
$$
S^{2(n - k) - 1} = V_{1}(\mathbb{C}^{n - k}) \to V_{k}(\mathbb{C}^n) \to V_{k - 1}(\mathbb{C}^n).
$$
Note $V_{n}(\mathbb{C}^n)$ is just $\mathrm{U}_{n}$, so in the nice situation of coefficients over a field, we get to recover what we want.

We claim $H^{\bullet}(V_{k}(\mathbb{C}^n))$ is the [[UChicago --- uc-2026/notes/Grading and algebras for algebraic topology#_definition _ exterior algebra|exterior algebra]] over $\mathbb{Z}$ with generators $x_{2(n - k) + i}$ for $i$ odd in $[1, 2n]$. We can verify this by hand for $k = 1$. Then, by induction, the Serre spectral sequence only has transgressions as non-zero differentials. Thus, we just jump up by $2$ in the grading. In particular, we see that $H^\bullet(\mathrm{U}_{n}) = H^\bullet(V_{n}(\mathbb{C}^n))$ is the exterior algebra with generators in all odd degrees $i \in [1, 2n]$.

Finally, we claim that using the fibration $\mathrm{U}_{n} \to E\mathrm{U}_{n} \to B\mathrm{U}_{n}$ that $H^\bullet(B \mathrm{U}_{n}, \mathbb{Z}) = \mathbb{Z}[y_{2}, \dots, y_{2n}]^\text{ext}$ — the polynomial algebra with generators in all even degrees $[1, 2n]$. This is seen by choosing the spectral sequence with $E^2$ page $\mathbb{Z}[y_{2}, \dots, y_{2n}] \otimes \mathbb{Z}[x_{1}, x_{3}, \dots, x_{2n - 1}]^\text{ext}$. Then using the fact that $E \mathrm{U}_{n}$ is contractible, you can induct backwards from infinity to see that this spectral sequence and the Serre spectral sequence for the fibration above are the same. Thus, $H^\bullet(B\mathrm{U}_{n}, \mathbb{Z})$ is as desired.

Thus, up to choosing canonical generators of $H^\bullet(B\mathrm{U}_{n}, \mathbb{Z})$ we have shown. We just need aa way to show that they are nice.

##### _theorem, definition:_ Chern classes

There exist $c_{i} \in H^{2i}(B\mathrm{U}_{n}, \mathbb{Z})$ giving natural transformations $c_{i} : \operatorname{Vect}_{\mathrm{U}_{n}} \to H^\bullet(-, \mathbb{Z})$ such that
1) $c_{0} = 1$, $c_{i} = 0$ if $i > n$
2) if $n = 1$, then $c_{1}$ is the canonical generator of $H^\bullet(B\mathrm{U}_{1}, \mathbb{Z}) = H^\bullet(\mathbb{C} \mathbb{P}^\infty, \mathbb{Z}) \cong \mathbb{Z}[x_{2}]$.
3) $c_{i}(\mathscr{V} \oplus \mathscr{V}) = c_{i}(\mathscr{V})$ for any bundle $\mathscr{V}$
4) $c_{i}(\mathscr{V} \oplus \mathscr{W}) = \sum_{j + k = i} c_{j}(\mathscr{V}) c_{k}(\mathscr{W})$ where the ranks of $\mathscr{V}$ and $\mathscr{W}$ sum to $n$.

These are the **Chern classes**.

###### _proof sketch:_

Consider the $n$-torus $\mathbb{T}^n$. We have a fibration $\mathrm{U}_{n} / \mathbb{T}^n \to B \mathbb{T}^n = (\mathbb{C} \mathbb{P}^\infty)^n \to B \mathrm{U}_{n}$. The cohomology of $\mathrm{U}_{n} / \mathbb{T}^n$ is a finitely generated module over any coefficient ring $A$. Thus, the map in cohomology $H^\bullet(B \mathrm{U}_{n}, \mathbb{F}) \to H^\bullet(\mathbb{C} \mathbb{P}^\infty, \mathbb{F})$ is an isomorphism for any field $\mathbb{F}$, including $\mathbb{Q}$. Thus, we get canonical coefficients by considering $H^\bullet(\mathbb{C} \mathbb{P}^\infty, \mathbb{F})^{\mathfrak{S}_{n}}$ — the $\mathfrak{S}_{n}$-fixed parts of the cohomology of $(\mathbb{C} \mathbb{P}^\infty)^n$. The rest follows formally.

---

### Stieffel–Whitney classes

For this section, let all (co)homology be with $\mathbb{F}_{2}$ coefficients.

Similarly, there is a Thom isomorphism that gives a canonical presentation $H^\bullet(B\mathrm{O}_{n}) = \mathbb{F}_{2}[w_{1}, \dots, w_{n}]$ with $w_{i}$ of degree $i$. There is also an inclusion $(B\mathbb{Z} / 2)^n \subseteq B\mathrm{O}_{n}$ giving an isomorphism $H^\bullet(B\mathrm{O}_{n}) \to H^\bullet(\mathbb{R} \mathbb{P}^\infty)^{\mathfrak{S}_{n}}$. 

Further, $H^\bullet(B\mathrm{SO}_{n}) = \mathbb{F}_{2}[w_{2}, \dots, w_{n}]$ with a map $H^\bullet(B\mathrm{O}_{n}) \to H^\bullet(B\mathrm{SO}_{n})$ by $w_{1} \mapsto 0$. Thus, $w_{1}$ represents the obstruction to an $\mathrm{O}_{n}$-vector bundle being an orientable $\mathrm{SO}_{n}$-bundle.

##### _theorem, definition:_ Stieffel–Whitney classes

There exist $w_{i} \in H^{i}(B\mathrm{O}_{n}, \mathbb{Z})$ giving natural transformations $w_{i} : \operatorname{Vect}_{\mathrm{O}_{n}} \to H^\bullet(-, \mathbb{Z})$ such that
1) $c_{0} = 1$, $c_{i} = 0$ if $i > n$
2) if $n = 1$, then $c_{1}$ is the canonical generator of $H^\bullet(B\mathrm{U}_{1}, \mathbb{Z}) = H^\bullet(\mathbb{C} \mathbb{P}^\infty, \mathbb{Z}) \cong \mathbb{Z}[x_{2}]$.
3) $c_{i}(\mathscr{V} \oplus \mathscr{V}) = c_{i}(\mathscr{V})$ for any bundle $\mathscr{V}$
4) $c_{i}(\mathscr{V} \oplus \mathscr{W}) = \sum_{j + k = i} c_{j}(\mathscr{V}) c_{k}(\mathscr{W})$ where the ranks of $\mathscr{V}$ and $\mathscr{W}$ sum to $n$.

These are the **Stieffel–Whitney classes**.

---

These classes are genuinely very useful — for example, $w_{0}(\mathscr{T}_{X} \oplus \mathscr{N}_{X}) = 1$ for any embedding of a manifold $X \subseteq \mathbb{R}^{N}$.xx1x1x2

##### _lemma:_ homotopy groups and homology of $V_{k}(\mathbb{R}^n)$

$V_{k}(\mathbb{R}^n)$ is $(n - k - 1)$-connected with
$$
\begin{cases}
\pi_{n - k}(V_{k}(\mathbb{R}^n)) = \begin{cases}
\mathbb{Z} / 2 & k = n \text{ or } n - k \text{ odd} \\
\mathbb{Z}
\end{cases}
\end{cases}
$$
and
$$
H^\bullet(V_{k}(\mathbb{R}^n)) = \mathbb{F}_{2}[x_{n - k}, \dots, x_{n - 1}]^\text{coalg}
$$
with $\deg x_{i} = i$.

---xx