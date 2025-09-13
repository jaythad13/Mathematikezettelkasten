---
tags:
- rising-sea/1/5
- cat-th
- hom-alg
---

Let $\mathscr{C}$ be any [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ abelian categories|abelian category]] and all objects be objects of it. In particular, let $f : A \to B$ be a morphism. The following lemmas hold in any such $\mathscr{C}$ and are useful for proving theorems about general abelian categories.

### Facts about [[Algebraic geometry --- rising-sea/notes/A little about abelian categories#_definition _ kernels, cokernels|kernels and cokernels]]

##### _lemma:_ kernels are monomorphisms and cokernels are epimorphisms

The kernel map $i : \ker f \to A$ is a [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#_definition _ monomorphisms, epimorphisms|monomorphism]]. Dually, the cokernel map is an epimorphism.

###### _proof:_

Suppose $\mu_{1}, \mu_{2} : K' \to \ker f$ agree on composition to $A$. Then, since $i \circ \mu_{1} = i \circ \mu_{2}$, we have $\mu = \mu_{2} - \mu_{1}$ with $i \circ \mu = 0$. Thus, $f \circ i \circ \mu : K' \to B$ is also just $0$. By the universal property of a kernel, $i \circ \mu : K' \to A$ factors uniquely through $\ker f$ as $i \circ \mu'$. Since $i \circ \mu = i \circ 0$, we must have $\mu = 0$, and thus, $\mu_{1} = \mu_{2}$.

---

##### _lemma:_ monomorphisms have $0$ kernel and epimorphisms have $0$ cokernel

The kernel of a monomorphism $f : A \to B$ is $0$. Dually, the cokernel of an epimorphism is also $0$.

###### _proof:_

Clearly $0$ has a map into the diagram
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& 0 \ar[d] \\
		A \ar[r, "f"] & B
	\end{tikzcd}
\end{document}
```
Suppose $K'$ has map $i' : K' \to A$ into the diagram. Then $i' \circ f = 0 = 0 \circ f$. Since $f$ is monic, $i' = 0$.

---

##### _corollary:_ kernels of kernels and cokernels of cokernels

The kernel of the kernel and the cokernel of the cokernel are $0$.

---

### Facts about images

##### _lemma:_ morphisms factor through images, or cokernel and kernel commute

There is a unique isomorphism $\operatorname{coker} \ker f \cong \operatorname{img} f = \ker \operatorname{coker} f$ such that $f$ factors as $A \to \operatorname{coker} \ker f \to \operatorname{img} f \to B$.

---

### Facts about morphisms of [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|exact sequences]]

Note that a morphism of exact sequences $A^\bullet$ and $B^\bullet$ is exactly a [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ morphisms of complexes|morphism of them as complexes]] — morphisms $A^i \to B^i$ for each $i$ so that the obvious square commutes.

##### _lemma:_ the snake lemma

Suppose we have a morphism of [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|short exact sequences]]
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r] \ar[d, "\alpha"] & B \ar[r] \ar[d, "\beta"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
		0 \ar[r] & D \ar[r] & E \ar[r] & F \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Then there is an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \alpha \ar[r] & \ker \beta \ar[r] & \ker \gamma \ar[r] & \mathrm{coker} \, \alpha \ar[r] &  \mathrm{coker} \, \beta \ar[r] & \mathrm{coker} \, \gamma \ar[r] & 0
	\end{tikzcd}
\end{document}
```

---

##### _lemma:_ the five lemma

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		A \ar[r] \ar[d, "\alpha"] & B \ar[r] \ar[d, "\beta"] & C \ar[r] \ar[d, "\gamma"] & D \ar[r] \ar[d, "\delta"] & E \ar[d, "\varepsilon"] \\
		F \ar[r] & G \ar[r] & H \ar[r] & I \ar[r] & J
	\end{tikzcd}
\end{document}
```
is a morphism of exact sequences and $\alpha, \beta, \delta, \varepsilon$ are all isomorphisms. Then $\gamma$ is an isomorphism.