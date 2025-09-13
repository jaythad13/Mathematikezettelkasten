---
tags:
- hom-alg
- cat-th
- rising-sea/1/5/9
- rising-sea/1/5/12
- rising-sea/1/5/16
---

Let $\mathscr{A}$ and $\mathscr{B}$ be [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian categories]].

Exact functors preserve (certain) exact sequences.

##### _definition:_ right-exact, left-exact, exact

Let $F : \mathscr{A} \to \mathscr{B}$ be an [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ additive category, homomorphism, additive functor|additive]] covariant functor.

$F$ is **right-exact** if the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A_{1} \ar[r] & A_{2} \ar[r] & A_{3} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
implies the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		F(A_{1}) \ar[r] & F(A_{2}) \ar[r] & F(A_{3}) \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

$F$ is **left-exact** if the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A_{1} \ar[r] & A_{2} \ar[r] & A_{3}
	\end{tikzcd}
\end{document}
```
implies the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & F(A_{1}) \ar[r] & F(A_{2}) \ar[r] & F(A_{3}).
	\end{tikzcd}
\end{document}
```

$F$ is **exact** if it is left and right exact.

---

##### _reality check:_ exact functors preserve short exact sequences

If $F : \mathscr{A} \to \mathscr{B}$ is exact, then the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A_{1} \ar[r] & A_{2} \ar[r] & A_{3} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
implies the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & F(A_{1}) \ar[r] & F(A_{2}) \ar[r] & F(A_{3}) \ar[r] & 0
	\end{tikzcd}
\end{document}
```

---

One example of an exact functor we've seen before is tensoring —

![[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensoring is functorial and right-exact|Tensor products, categorically]]

Localisation is even better — it's exact on the nose!

##### _example:_ localisation is exact

Suppose $M$ is an $A$-module and $S \subseteq A$ is multiplicative. Then $\mathsf{Mod}_{A} \to \mathsf{Mod}_{S^{-1} A}$ is an exact functor. Note that it suffices to show that exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M_{1} \ar[r, "\varphi_{1}"] & M_{2} \ar[r, "\varphi_{2}"] \ar[r] & M_{3}
	\end{tikzcd}
\end{document}
```
implies exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		S^{-1} M_{1} \ar[r, "\varphi_{1, *}"] & S^{-1} M_{2} \ar[r, "\varphi_{2, *}"] & S^{-1} M_{3}
	\end{tikzcd}
\end{document}
```
(with no need for the first/last map to be injective/surjective). It's easy to see that $\operatorname{img} \varphi_{1, *} \subseteq \ker \varphi_{2, *}$. We show the opposite inclusion. 

Suppose $\varphi_{2, *}(m_{2} / s_{2}) = 0$. Then $\varphi(m_{2}) / s_{2} = 0$, and so $s \varphi_{2}(m_{2}) = 0 = \varphi_{2}(s m_{2})$ for some $s \in S$. It follows that $\varphi_{1}(m_{1}) = sm_{2}$ for some $m_{1} \in M_{1}$. Thus, $\varphi_{1, *}(m_{1} / s s_{2}) = m_{2} / s_{2}$ as desired.

---

The [[Algebraic geometry --- rising-sea/notes/Functors#_example _ the functor of points and its opposite|functor of points and its opposite]] are left-exact in a general abelian category. However, here we only prove it over the category of $A$-modules. Let $M$ be an $A$-module.

##### _example:_ $h^M$ is (covariant) left-exact

The covariant functor $h^M : \mathsf{Mod}_{A} \to \mathsf{Mod}_{A}$ by $N \mapsto \operatorname{Hom}(M, N)$ is left exact.

---

##### _example:_ $h_{M}$ is (contravariant) left-exact

The contravariant functor $h_{N} : \mathsf{Mod}_{A} \to \mathsf{Mod}_{A}$ by $M \mapsto \operatorname{Hom}(M, N)$ is left-exact. Note that we want to show that if
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M_{1} \ar[r, "\varphi_{1}"] & M_{2} \ar[r, "\varphi_{2}"] \ar[r] & M_{3} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact, then
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathrm{Hom}(M_{3}, N) \ar[r, "\varphi_{2}^*"] & \mathrm{Hom}(M_{2}, N) \ar[r, "\varphi_{1}^*"] & \mathrm{Hom}(M_{1}, N)
	\end{tikzcd}
\end{document}
```
It's easy to show that $\varphi_{2}^*$ is injective, and that $\operatorname{img} \varphi_{2}^* \subseteq \ker \varphi_{1}^*$ since we have
$$
\varphi_{1}^*(\varphi_{2}^*(\psi_{3})) = \psi_{3} \circ \varphi_{2} \circ \varphi_{1} = 0
$$
because $\varphi_{2} \circ \varphi_{1} = 0$ by exactness of the original sequence.

The opposite inclusion is, as always, more involved. Suppose $\varphi_{1}^*(\psi_{2}) = \psi_{2} \circ \varphi_{1} = 0$ for some $\psi_{2} \in \operatorname{Hom}(M_{2}, N)$. Thus, $\ker \varphi_{2} = \operatorname{img} \varphi_{1} \subseteq \ker \psi_{2}$. By the surjectivity of $\varphi_{2}$, $M_{2} / \ker \varphi_{2} = M_{3}$. Thus, $\psi_{2}$ descends to a map $\overline{\psi}_{2} : M_{2} / \ker \varphi_{2} = M_{3} \to N$ such that $\psi_{2} = \overline{\psi}_{2} \circ \varphi_{2}$. This is the desired $\psi_{3} \in \operatorname{Hom}(M_{3}, N)$ such that $\psi_{2} = \varphi_{2}^*(\psi_{3})$.

---

Exact functors are useful to prove (say) that $A$-linear morphisms of modules are essentially the same as $S^{-1} A$-linear morphisms of their localisations away from $S$.

##### _example:_ localisation commutes with $\operatorname{Hom}$

Suppose $M$ is a finitely-presented $A$-module (and thus) fitting in an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A^{\oplus q} \ar[r] & A^{\oplus p} \ar[r] & M \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
Then by the left exactness of $h_{M}$, there is an isomorphism
$$
S^{-1} \operatorname{Hom}_{A}(M, N) \cong \operatorname{Hom}_{S^{-1} A}(S^{-1} M, S^{-1} N).
$$
Specifically, 

This doesn't work without the finitely-presented hypothesis. For $S = \mathbb{Z} \setminus \{ 0 \}$, we have $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Q}, \mathbb{Z}) = 0$ (a $\mathbb{Z}$-linear $\mathbb{Q} \to \mathbb{Z}$ is equivalent to the [[Commutative algebra --- math-189AA/notes/Modules#_examples and non-examples _ modules|impossibility]] of giving $\mathbb{Z}$ a $\mathbb{Q}$-module structure) and so $S^{-1} \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Q}, \mathbb{Z}) = 0$. Meanwhile $\operatorname{Hom}_{\mathbb{Q}}(\mathbb{Q}, \mathbb{Q}) \cong \mathbb{Q}$.

---

The most wide-reaching generalisation of exact functors preserving exact sequences is the FernbahnhoF theorem, so named because it can take you far! We may not prove this yet.

##### _theorem:_ the $F$ernba$H$n$H$o$F$ theorem

Suppose $F : \mathscr{A} \to \mathscr{B}$ is a covariant functor of abelian categories and $A^\bullet$ is a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|complex]] in $\mathscr{A}$.
1) If $F$ is right-exact, there is a natural morphism $F H^\bullet \to H^\bullet F$. That is, for each $i$, there is a natural morphism $F H^i(A^\bullet) \to H^i(F A^\bullet)$.
2) If $F$ is right-exact, there is a natural morphism $F H^\bullet \xleftarrow{} H^\bullet F$. That is, for each $i$, there is a natural morphism $F H^i(A^\bullet) \xleftarrow{} H^i(F A^\bullet)$.
3) If $F$ is exact, then the morphisms above are inverses and isomorphisms.

---

### Interaction with limits

One generalisation of exactness is the interaction of functors with limits and colimits. Since kernels are limits and cokernels are colimits, functors that commute with limits (like right-adjoints) are left-exact and functors that commute with colimits (like left-adjoints) are right-exact. In fact, we can think of limits and colimits themselves as functors. We will show that limits commute with limits and similarly for colimits, so limits are left exact and colimits are right exact.

Note however, that the converse isn't true — while commuting with colimits implies right-exactness, right-exactness doesn't imply commuting with colimits. For example, double-dual is right-exact but does not commute with infinite direct sums.

The following is an example of limits commuting with limits, very concretely.

##### _example:_ kernels commute with limits

Suppose $\mathscr{I} \to \mathscr{C}$ by $i \mapsto A_{i}$ and $i \mapsto B_{i}$ are two [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ diagram indexed by a category, index category|diagrams]] in $\mathscr{C}$ indexed by $\mathscr{I}$. If $h_{i} : A_{i} \to B_{i}$ describes a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of the functors and $h : \lim A_{i} \to \lim B_{i}$ the resultant morphism. 

Then $i \mapsto \ker h_{i}$ is another diagram $\mathscr{I} \to \mathscr{C}$ and there is a canonical isomorphism giving $\lim \ker h_{i} \cong \ker h$, assuming all limits exist.

---

##### _proposition:_ limits commute with limits (and colimits commute with colimits)

Suppose each $D^j : \mathscr{I} \to \mathscr{A}$ by $i \mapsto A_{i}^j$ et c. is a diagram in $\mathscr{A}$. Suppose also that there are diagrams $D_{i} : \mathscr{J} \to \mathscr{A}$ for each $i$, giving morphisms $d_{i}^{j j'} : A_{i}^j \to A^{j'}_{i}$ that also describe natural transformations $D^j \to D^{j'}$. Then each $j \mapsto \lim_{\mathscr{I}} A_{i}^j$ is a diagram $\mathscr{J} \to \mathscr{A}$ and each $i \mapsto \lim_{\mathscr{J}} A^j_{i}$ is a diagram $\mathscr{I} \to \mathscr{A}$.

There is a canonical isomorphism giving
$$
\lim_{\mathscr{I}} \lim_{\mathscr{J}} A_{i}^j = \lim_{\mathscr{J}} \lim_{\mathscr{I}} A_{i}^j.
$$

It follows dually that colimits commute with colimits.

---

##### _proposition:_ right adjoints preserve limits

Suppose $F : \mathscr{A} \to \mathscr{B}$ and $G : \mathscr{B} \to \mathscr{A}$ are an adjoint pair of functors with $G$ right-adjoint. If the [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_definition _ diagram indexed by a category, index category|diagram]] $D : \mathscr{I} \to \mathscr{B}$ is a diagram $i \mapsto B_{i}$ with limit $\lim B_{i}$, then $G(\lim B_{i})$ is the limit of $G \circ D$ in $\mathscr{A}$.

It follows dually that left adjoints preserve colimits.

---

This abstract nonsense is useful to prove some general statement about exactness of limits or colimits. For example —

##### _example:_ filtered colimits are exact in $\mathsf{Mod}_{A}$

---

##### _example:_ filtered colimits commute with homology in $\mathsf{Mod}_{A}$

---

##### _example:_ exact sequences of limits

Suppose 
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& \vdots \ar[d] & \vdots \ar[d] & \vdots \ar[d] \\
		0 \ar[r] & A_{n + 1} \ar[r] \ar[d] & B_{n + 1} \ar[r] \ar[d] & C_{n + 1} \ar[r] & 0 \\
		0 \ar[r] & A_{n} \ar[r] \ar[d] & B_{n + 1} \ar[r] \ar[d] & C_{n + 1} \ar[r] \ar[d] & 0 \\
		& \vdots \ar[d] & \vdots \ar[d] & \vdots \ar[d] \\
		0 \ar[r] & A_{0} \ar[r] & B_{0} \ar[r] & \ar[r] C_{0} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is a commutative diagram in $\mathsf{Mod}$ (over some ring) with exact rows and $A_{n + 1} \to A_{n}$ always surjective. Then the limit
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \lim A_{n} \ar[r] & \lim B_{n} \ar[r] & \lim C_{n} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is exact.

---

### Dreaming of derived functors

While left-exact functors cut a beautiful exact sequence like
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A_{1} \ar[r] & A_{2} \ar[r] & A_{3} \ar[r] & 0
	\end{tikzcd}
\end{document}
```
short, and just leave us with
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & F(A_{1}) \ar[r] & F(A_{2}) \ar[r] & F(A_{3}),
	\end{tikzcd}
\end{document}
```
they leave us free to dream. We might imagine that the sequence continues, and that there is some sequence of functors $R^i F$ such that $R^0 F = F$ and the $R^i F$s give an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & F(A_{1}) \ar[r] & F(A_{2}) \ar[r] & F(A_{3}) \ar[r] & R_{1}F(A_{1}) \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```
Similarly, we might hope for some way to continue the exact sequences given by left-exact functors. In good situations, we can, using derived functors.