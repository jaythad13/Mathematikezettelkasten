---
tags:
- cat-th
- rising-sea/1/4
---

>[!missing]
>lots of details

Just as [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal properties]] determine an object up to unique isomorphism (if it exists), adjoints determine a functor up to [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural isomorphism]] (if it exists). 

##### _definition:_ adjoint functors, left adjoint, right adjoint, adjoint pair

Two covariant functors $F : \mathscr{A} \to \mathscr{B}$ and $G : \mathscr{B} \to \mathscr{A}$ are **adjoint** if there is a natural bijection $\tau_{AB} : \operatorname{Mor}_{\mathscr{B}}(F(A), B) \to \operatorname{Mor}_{\mathscr{A}}(A, G(B))$ for all $A \in \mathscr{A}$ and $B \in \mathscr{B}$. It is natural in that for each $f : A \to A'$ the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(F(A'), B) \ar[r, "h_{B}(F f)"] \ar[d, "\tau_{A' B}"] & \mathrm{Mor} (F(A), B) \ar[d, "\tau_{AB}"] \\
		\mathrm{Mor}(A', G(B)) \ar[r, "h_{G(B)}(f)"] & \mathrm{Mor}(A, G(B))
	\end{tikzcd}
\end{document}
```
and for all $g : B \to B'$ the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(F(A), B) \ar[r, "h^{F(A)}(g)"] \ar[d, "\tau_{A B}"] & \mathrm{Mor} (F(A), B') \ar[d, "\tau_{A B'}"] \\
		\mathrm{Mor}(A, G(B)) \ar[r, "h^A(G g)"] & \mathrm{Mor}(A, G(B'))
	\end{tikzcd}
\end{document}
```
That is, $A \mapsto \tau_{AB}$ is a [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] of the functors $h_{B} \circ F$ and $h_{G(B)}$ for each $B \in \mathscr{B}$. Similarly, we require that $B \to \tau_{AB}$ is a natural transformation of the functors $h^{F(A)}$ and $h^{A} \circ G$ for each $A \in \mathscr{A}$.

We say $(F, G)$ are an **adjoint pair** with $F$ the **left adjoint** and $G$ the **right adjoint**.

The adjoint-defining bijection can be obtained by factoring through the composition of the functors.

##### _proposition:_ adjoint-defining maps factor through composition of functors

For each $A$ there is a map $\eta_{A} : A \to GF(A)$ such that for each $g : F(A) \to B$ the corresponding $\tau_{AB}(g) : A \to G(B)$ is given by the composition $Gg \circ \eta_{A}$.
 
Similarly, for each $B$, there is a map $\varepsilon_{B} : FG(B) \to B$ so that for each $f : A \to G(B)$ the corresponding map $\tau_{AB}^{-1}(f) : F(A) \to B$ is gven by the composition $\varepsilon_{B} \circ Ff$.

###### _proof:_

>[!warning]
>incomplete

Note that for each $g : F(A) \to B$ the following diagram must commute
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Mor}(F(A), F(A)) \ar[r, "h^{F(A)}(g)"] \ar[d, "\tau_{A F(A)}"] & \mathrm{Mor}(F(A), B) \ar[d, "\tau_{AB}"] \\
		\mathrm{Mor}(A, GF(A)) \ar[r, "h^A(Gg)"] & \mathrm{Mor}(A, G(B))
	\end{tikzcd}
\end{document}
```

##### _example:_ tensor-Hom adjunction

The functors $\mathsf{Mod}_{A} \to \mathsf{Mod}_{A}$ by $M \mapsto M \otimes_{A} N$ and $h^N : M \mapsto \operatorname{Hom}_{A}(N, M)$ are adjoint. In particular, for $A$-modules $M, N, P$ a bijection 
$$
\operatorname{Hom}_{A}(M \otimes_{A} N, P) \to \operatorname{Hom}_{A}(M, \operatorname{Hom}_{A}(N, P))
$$
is given as follows. Recall that $\alpha \in \operatorname{Hom}_{A}(M \otimes_{A} N, P)$ is equivalent to the data of a bilinear map $M \times N \to P$, and thus, for each $m \in M$ a homomorphism $\alpha_{m} : N \to P$ by $n \mapsto \alpha(m \otimes n)$. Denote $m \mapsto \alpha_{m}$ by $\alpha_{-}$. Note then that for any $\varphi : M \to M'$ and $\psi : P \to P'$, the following diagrams commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Hom}(M' \otimes N, P) \ar[r, "h_{P}(\varphi_{*})"] \ar[d, "\tau_{M' P}"] & \mathrm{Hom}(M \otimes N, P) \ar[d, "\tau_{M P}"] \\
		\mathrm{Hom}(M', \mathrm{Hom}(N, P)) \ar[r, "h_{\mathrm{Hom}(N, P)}(\varphi)"] & \mathrm{Hom}(M, \mathrm{Hom}(N, P))
	\end{tikzcd}
\end{document}
```

commutes since the map obtained by $\alpha \in \operatorname{Hom}_{A}(M' \otimes_{A} N, P)$ gives $m : n \mapsto \alpha(\varphi(m) \otimes n)$ either way. That is $\alpha \mapsto \alpha_{-} \mapsto \alpha_{-} \circ \varphi$ or $\alpha \mapsto \alpha \circ \varphi \mapsto (\alpha \circ \varphi)_{-}$. But $\alpha_{-} \circ \varphi(m)(n) = \alpha_{\varphi(m)}(n) = \alpha(\varphi(m) \otimes n)$  and $(\alpha \circ \varphi_{*})_{m}(n) = \alpha \circ \varphi_{*}(m \otimes n) = \alpha(\varphi(m) \otimes n)$ so they are equal. 

Similarly,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Hom}(M \otimes N, P) \ar[r, "h^{M \otimes N}(\psi)"] \ar[d, "\tau_{M P}"] & \mathrm{Hom}(M \otimes N, P') \ar[d, "\tau_{M P'}"] \\
		\mathrm{Hom}(M, \mathrm{Hom}(N, P)) \ar[r, "h^M(h^N(\psi))"] & \mathrm{Hom}(M, \mathrm{Hom}(N, P'))
	\end{tikzcd}
\end{document}
```
commutes since $\alpha \in \operatorname{Hom}_{A}(M \otimes_{A} N, P)$ gives $m : n \mapsto \psi(\alpha(m \otimes n))$ either way.

##### _example:_ module base ring change adjunction

Suppose $\varphi :B \to A$ is a ring homomorphism. If $M$ is an $A$-module, it can now be considered as a $B$-module $M_{B}$ with $b m = \varphi(b) m$. This gives a functor $\mathsf{Mod}_{A} \to \mathsf{Mod}_{B}$ by $M \mapsto M_{B}$. This functor is right adjoint to [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensoring with a ring is a base-ring change functor|the functor]] $N \mapsto N \otimes_{B} A$. Specifically, there is a bijection
$$
\operatorname{Hom}_{A}(N \otimes_{B} A, M) \to \operatorname{Hom}_{B}(N, M_{B})
$$
by $\alpha \mapsto \beta$ where $\alpha(n \otimes \varphi(b)) = m$ translates to $\beta(b n) = m$.

Suppose $\psi : N \to N'$ is a homomorphism (of $B$-modules). Let $\psi_{*}$ be the corresponding morphism $N \otimes_{B} A \to N' \otimes_{B} A$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Hom}_{A}(N' \otimes_{B} A, M) \ar[r, "h_{M}(\psi_{*})"] \ar[d, "\tau_{N' M}"] & \mathrm{Hom}_{A}(N \otimes_{B} A, M) \ar[d, "\tau_{N M}"] \\
		\mathrm{Hom}_{B}(N', M_{B}) \ar[r, "h_{M_{B}}(\psi)"] & \mathrm{Hom}_{B}(N, M_{B})
	\end{tikzcd}
\end{document}
```
Thus, some $\alpha' : n' \otimes \varphi(b) \mapsto \beta'(b n') = m$ is sent to some $\beta : b n \mapsto \beta'(b \psi(n))$ in both ways. Similarly, suppose $\psi : M \to M'$ is an $A$-module homomorphism and $\psi_{*} : M_{B} \to M_{B}'$ is the corresponding $B$-module morphism. We can track $\alpha : n \otimes \varphi(b) \mapsto m$ to a morphism $\beta' : N \to M_{B}'$ by $bn \mapsto \psi(m)$ in both ways.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathrm{Hom}_{A}(N \otimes_{B} A, M) \ar[r, "h^{N \otimes_{B} A}(\psi)"] \ar[d, "\tau_{N M}"] & \mathrm{Hom}_{A}(N \otimes_{B} A, M') \ar[d, "\tau_{N M'}"] \\
		\mathrm{Hom}_{B}(N, M_{B}) \ar[r, "h^{N}(\psi_{*})"] & \mathrm{Hom}_{B}(N, M'_{B})
	\end{tikzcd}
\end{document}
```

### Left adjoints of forgetful functors

Adjoints come up most commonly when we have a [[Algebraic geometry --- rising-sea/notes/Functors#Faithfulness and fullness|forgetful functor]]. The left adjoint to a forgetful functor reconstructs the structure "forgotten".

##### _example:_ groupification as adjoint to forgetting

An abelian semigroup is a set with a associative commutative binary operation. If you count closure under the group operation as an axiom, a semigroup satisfies two of the four group axioms. Morphisms of semigroups are functions that preserve the operation. For example, the natural numbers with ($\mathbb{N}_{0}$) or without ($\mathbb{N}$) the identity $0$ are an abelian semigroup under addition. They are both groupified to the integers. $\mathbb{N}$ under multiplication groupifies to the positive rationals. 

Specifically, the **groupification** of an abelian semigroup $S$ is an abelian group $G$ with a choice of semigroup morphism $\pi : S \to G$ such that any semigroup morphism $S \to G'$ factors uniquely through $\pi$ (if it exists).

Clearly, the groupification of an abelian group is just itself with the identity.

We can always construct the groupification $H(S)$ of an abelian semigroup $S$ as the set of formal differences $\{ (a - b) \mid a, b \in S \} / \sim$ with $(a - b) \sim (c - d)$ if and only if $a + d + e= b + c + e$ for some $e \in S$. Here addition is defined by $(a - b) + (c - d) = (a + c) - (b + d)$, the identity is $(a - a)$ and the inverse of $(a - b)$ is $(b - a)$. Then the canonical semigroup morphism $S \to H(S)$ is given by $a \mapsto (a + b) - b$.

The adjoint defining bijection $\tau_{SG} : \operatorname{Hom}_{\mathsf{Ab}}(H(S), G) \to \operatorname{Mor}_{\mathsf{Semi}}(S, F(G))$ is defined by sending $\varphi : \pi(s) \mapsto g$ to $\tau_{GS}(\varphi) : s \mapsto g$.

##### _example:_ localisation as adjoint to forgetting

### Adjoints and limits

If $F, G$ are an adjoint pair of functors, then the left-adjoint $F$ commutes with colimits and $G$ commutes with limits. We prove this [[Algebraic geometry --- rising-sea/notes/Exact functors#_proposition _ right adjoints preserve limits|here]].

### The table of adjoint functors

It's useful to know the adjointness of the following functors

| Name                                                          | $\mathscr{A}$        | $\mathscr{B}$       | Left adjoint $\mathscr{A} \to \mathscr{A}$ | Right adjoint $\mathscr{B} \to \mathscr{A}$ |
| ------------------------------------------------------------- | -------------------- | ------------------- | ------------------------------------------ | ------------------------------------------- |
| tensor-Hom adjunction                                         | $\mathsf{Mod}_{A}$   | $\mathsf{Mod}_{A}$  | $M \mapsto M \otimes N$                    | $M \mapsto \operatorname{Hom}(N, M)$        |
| base-ring change adjunction with $B \to A$                    | $\mathsf{Mod}_{B}$   | $\mathsf{Mod}_{A}$  | $N \mapsto N \otimes_{B} A$                | $M \mapsto M_{B}$ (restriction of scalars)  |
| sheafification on a topological space $X$                     | presheaves on $X$    | sheaves on $X$      | sheafification                             | forgetful                                   |
| (abelian) groupification                                      | (abelian) semigroups | (abelian) groups    | groupification                             | forgetful                                   |
| transfer of sheaves by open embeddings $\pi : U \to Y$        | sheaves on $U$       | sheaves on $Y$      | $\pi_{!}$                                  | $\pi ^{-1}$                                 |
| transfer of quasicoherent sheaves by $\pi : X \to Y$          | $\mathsf{QCoh}_{Y}$  | $\mathsf{QCoh}_{X}$ | $\pi^*$                                    | $\pi_{*}$                                   |
| transfer of quasicoherent sheaves by affine $\pi : X \to Y$   | $\mathsf{QCoh}_{X}$  | $\mathsf{QCoh}_{Y}$ | $\pi_{*}$                                  | $\pi^{!?}$                                  |
| ring theoretic transfer of quasicoherent sheaves by $B \to A$ | $\mathsf{Mod}_{A}$   | $\mathsf{Mod}_{B}$  | $M \mapsto M_{B}$                          | $N \mapsto \operatorname{Hom}_{B}(A, N)$    |


