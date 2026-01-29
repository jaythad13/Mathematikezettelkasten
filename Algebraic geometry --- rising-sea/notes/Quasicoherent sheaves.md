---
tags:
- rising-sea/4/1
- rising-sea/6
- alg-geo
- comm-alg
---

Let $A$ be a ring, $M$ be an $A$-module, and let $X$ be a scheme.

We can construct $\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-modules]] on affine schemes $\operatorname{Spec} A$ from $A$-modules $M$ in much the same way that we construct the structure sheaf $\mathscr{O}_{\operatorname{Spec} A}$. Quasicoherent sheaves are really nice because they are glued together from these building blocks, and satisfy good abstract nonsense properties.

### Quasicoherent sheaves on affine schemes

Let $X = \operatorname{Spec} A$ be an [[Algebraic geometry --- rising-sea/notes/Affine schemes#_definition _ affine scheme|affine scheme]]. We claim that we can describe an $\mathscr{O}_{X}$-module corresponding to each module $M$.

##### _definition:_ affine quasicoherent sheaf, twiddlification

The **twiddlification** of $M$ is the **affine quasicoherent sheaf** $\widetilde{M}$ on $\operatorname{Spec} A$ defined on the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ the distinguished open sets form the distinguished open base|base of distinguished opens]] by $\widetilde{M}(D(f)) = M_{f}$. 

---

Of course, we need to show that this really is a sheaf

##### _proposition:_ twiddlification really forms a sheaf

The assignment $\widetilde{M}(D(f)) = M_{f}$ satisfies [[Algebraic geometry --- rising-sea/notes/Sheaves on a base#_definition _ sheaves on a base, presheaves on a base|base identity and gluability]], and thus, defines a sheaf on $\operatorname{Spec} A$.

###### _proof:_

We show the exactness of
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r] & \prod_{i \in \mathcal{I}} N_{f_{i}} \ar[r] & \prod_{i \neq j \in \mathcal{I}} N_{f_{i} f_{j}}
	\end{tikzcd}
\end{document}
```
(as $A$-modules) for any $A$-module $N$, and any collection of $f_{i}$ such that $(f_{i})_{i \in \mathscr{I}} = A$. Here $N_{f_{i}} \to N_{f_{i} f_{j}}$ is the localisation map and $N_{f_{j}} \to N_{f_{i} f_{j}}$ is the negative of the localisation map. We take their sum.

Choosing $N = M_{f}$, we get that if $D(f) = \bigcup_{i \in \mathscr{I}} D(f_{i})$, then
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \widetilde{M}(D(f)) \ar[r] & \prod_{i \in \mathcal{I}} \widetilde{M}(D(f_{i})) \ar[r] & \prod_{i \neq j \in \mathcal{I}} \widetilde{M}(D(f_{i} f_{j}))
	\end{tikzcd}
\end{document}
```
is exact. [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ intersections of distinguished opens are distinguished|Note that]] $D(f_{i}) \cap D(f_{j}) = D(f_{i} f_{j})$. This is exactly base identity and gluability (for the same reason that there is an [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|exactness criterion for sheaf identity and gluability]] in general). 

First we show that $N \to \prod_{i \in \mathscr{I}} N_{f_{i}}$ is injective. Suppose $n \mapsto 0$ in all $N_{f_{i}}$. That is, there is some $m_{i}$ such that $f_{i}^{m_{i}} n = 0$. Choose some finite subcollection of $i \in I \subseteq \mathscr{I}$ so that we still have $(f_{1}, \dots, f_{n}) = A$ (recall [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_corollary _ every affine scheme is quasicompact|quasicompactness of affine schemes]]). We claim $(f_{1}^{m_{1}}, \dots, f_{n}^{m_{n}}) = A$ still. This is because each $D(f_{i}^{m_{i}}) = D(f_{i})$ (each principal ideal [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets#_proposition _ containment of distinguished opens|is contained in the radical of the other]]). But then, write $1 = \sum a_{i} f_{i}^{m_{i}}$, and thus, $n \left( \sum a_{i} f_{i}^{m_{i}} \right) = 0$ implies $n = 0$.

Now we show that the sequence is a complex at $\prod_{i \in \mathscr{I}} N_{f_{i}}$. For each $(n)_{i \in \mathscr{I}}$ coming from some $n \in N$, we have $n \mapsto n$ and $n \mapsto -n$ under the positive and negative localisation maps. Thus, $(n)_{i \in \mathscr{I}} \mapsto (n - n)_{i \neq j \in \mathscr{I}} = 0$.

Finally, we show that the sequence is exact at $\prod_{i \in \mathscr{I}} N_{f_{i}}$. We first show this in the case that $\mathscr{I}$ is some finite set $I$. Suppose $(n_{i} / f_{i}^{m_{i}})_{i \in I} \mapsto 0$. Considering $g_{i} = f_{i}^{m_{i}}$ and $D(g_{i}) = D(f_{i}^m)$, we get $n_{i} / f_{i} = n_{i} / g_{i}$ on each $D(g_{i})$ such that they agree on the overlaps. That is, we have
$$
(g_{i} g_{j})^{m_{ij}} (n_{i} g_{j} - n_{j} g_{i}) = 0
$$
for some $m_{ij}$, for each pair $i \neq j$. Choose $m = \max \{ m_{ij} \}$, and then we have
$$
(g_{i} g_{j})^m (n_{i} g_{j} - n_{j} g_{i}) = 0
$$
for all $i \neq j$. We can equivalently write this as
$$
(n_{i} g_{i}^m) g_{j}^{m + 1} - (n_{j} g_{j}^m) g_{i}^{m + 1} = 0.
$$
This allows us to simplify further — choose $n'_{i} = n_{i} g_{i}^m$ and write $h_{j} = g_{j}^{m + 1}$ so that $D(h_{j}) = D(g_{j})$. Then we have sections $n_{i}' / h_{i}$ on each $D(h_{i})$ that agree simply on intersections — we have a simple compatibility condition $n_{i}' h_{j} - n_{j}' h_{j}$. 

We can write $1 = \sum a_{i} h_{i}$. Then consider $n = \sum a_{j} n_{j}'$. We claim this restricts to $n_{i}' / h_{i}$ on each $D(h_{i})$. This follows since we have the cross product
$$
\frac{n_{i}'}{h_{i}} - n = \frac{n_{i}' - \sum a_{j} n_{j}' h_{i}}{h_{i}} = \frac{n_{i}' - (\sum a_{j} h_{j}) n_{j}'}{h_{i}} = 0
$$
Here, the second equality follows because each $n_{j}' h_{i} = n_{i}' h_{j}$ .

Now suppose $\mathscr{I}$ is infinite. Choose a finite subset $I = \{ 1, \dots, n \}$ and apply the result above to get $n$ restricting to the correct section $n_{i}$ on each $D(f_{i})$. We claim that if $j \in \mathscr{I} \setminus I$, then $n$ restricts to $n_{j}$ on $D(f_{j})$. Consider $J = I \cup \{ j \}$ and apply the result above to get some $n'$ restricting to $n_{j}$ on $D(f_{j})$ and to $n_{i}$ on each $i \in I$. But then by base identity, $n' = n$. Thus, $n$ also restricts to $n_{j}$ on $D(f_{j})$.

---

The stalks are exactly what you think they should be.

##### _proposition:_ stalks of affine quasicoherent sheaves

Suppose $\mathfrak{p} \in \operatorname{Spec} A$. There is a canonical isomorphism $\widetilde{M}_{\mathfrak{p}} \to M_{\mathfrak{p}}$ between the stalk and localisation.

###### _proof:_

Localisation at $\mathfrak{p}$ [[Algebraic geometry --- rising-sea/notes/Limits and colimits#_proposition _ localisation is a colimit|is the colimit]] of all $M_{f}$ for all $f \not\in \mathfrak{p}$. The stalk $\widetilde{M}_{\mathfrak{p}}$ [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ stalks, germs|is the colimit]] of all $\widetilde{M}(D(f))$ with $D(f)$ containing $\mathfrak{p}$. But these $f$ are exactly the $f \not\in \mathfrak{p}$. Thus, the stalk and the localisation are canonically isomorphic.

---

This allows us to define the notion of the support of a module.

##### _definition:_ support of a module

The **support of an $A$-module** $M$ is the support of the sheaf $\widetilde{M}$ on $\operatorname{Spec} A$. That is,
$$
\operatorname{Supp} M = \{ \mathfrak{p} \in \operatorname{Spec} A \mid M_{\mathfrak{p}} \neq 0 \} \subseteq \operatorname{Spec} A
$$

---

Finally, the morphisms between these special sheaves are exactly $A$-module morphisms. This can be said more fancily.

##### _proposition:_ morphisms of affine quasicoherent sheaves are $A$-linear maps

There is a functor $\mathsf{Mod}_{A} \to \mathsf{Mod}_{\mathscr{O}_{\operatorname{Spec} A}}$ expressing $\mathsf{Mod}_{A}$ as a [[Algebraic geometry --- rising-sea/notes/Functors#_definition _ faithful, full, fully faithful|full]] [[Algebraic geometry --- rising-sea/notes/Categories#_definition _ subcategory|subcategory]].

###### _proof:_

Suppose we have a morphism of $A$-modules $\varphi : M \to N$. Then by the functoriality of localisation, we have maps $\varphi_{f} : M_{f} \to N_{g}$ for any $f, g \in A$. We claim the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M_{f} \ar[r, "\varphi_{f}"] \ar[d] & N_{f} \ar[d] \\
		M_{fg} \ar[r, "\varphi_{fg}"] & N_{fg}
	\end{tikzcd}
\end{document}
```
$\varphi_{fg}(m) = \varphi_{f}(m)$ for all $m$ in $M_{f}$ and $N_{f} \to N_{fg}$ also has $n \mapsto n$ for any $n \in N_{f}$, so the diagram commutes. This is exactly the diagram to show that $\widetilde{\varphi}(D(f)) = \varphi_{f}$ defines a morphism of sheaves on a base, [[Algebraic geometry --- rising-sea/notes/Sheaves on a base#_proposition _ a morphism of sheaves on a base induces a sheaf morphism|morphism of sheaves on a base, and thus]], a [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|morphism of sheaves]] $\widetilde{\varphi} : \widetilde{M} \to \widetilde{N}$.

By the functoriality of localisation, the maps commute with composition on each distinguished open, and thus, also as morphisms of sheaves. That is, $(\varphi \circ \psi)_{f} = \varphi_{f} \circ \psi_{f}$, so we also have $\widetilde{\varphi \circ \psi} = \widetilde{\varphi} \circ \widetilde{\psi}$.

Any morphism of sheaves $\widetilde{\varphi} : \widetilde{M} \to \widetilde{N}$ has the following diagram commute (writing $M_{f}$ for $\widetilde{M}(D(f))$ and $\varphi$ for $\widetilde{\varphi}(\operatorname{Spec} A)$)
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M \ar[r, "\varphi"] \ar[d] & N \ar[d] \\
		M_{f} \ar[r, "\widetilde{\varphi}(D(f))"] & N_{f}
	\end{tikzcd}
\end{document}
```
We want to show that $\widetilde{\varphi}(D(f)) = \varphi_{f}$. By the [[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_proposition _ the universal property of localisation|universal property of localisation]], $\widetilde{\varphi}(D(f))$ is the unique map that $M \to N \to N_{f}$ factors through. $\varphi_{f}$ is also this map, so they are the same map.

We have shown that every sheaf morphism $\widetilde{M} \to \widetilde{N}$ comes from a module morphism $M \to N$, so the functor $\mathsf{Mod}_{A} \to \mathsf{Mod}_{\mathscr{O}_{\operatorname{Spec} A}}$ is full.

---

### Quasicoherent sheaves

Quasicoherent sheaves are then the obvious globalisation of these $\widetilde{M}$. In fact, we can define the whole category of quasicoherent sheaves in one go.

##### _definition:_ quasicoherent sheaves, $\mathsf{QCoh}_{X}$

A **quasicoherent sheaf** on $X$ is an $\mathscr{O}_{X}$[[Algebraic geometry --- rising-sea/notes/Ringed spaces#_definition _ $ mathscr{O}_{X}$-modules|-module]] $\mathscr{F}$ such that, for each affine open $\operatorname{Spec} A \subseteq X$, we have $\mathscr{F}_{\mid \operatorname{Spec} A} \cong \widetilde{M}$, for some $A$-module $M$.

The **category of quasicoherent sheaves on $X$** is $\mathsf{QCoh}_{X}$, consisting of all quasicoherent sheaves as objects and all [[Algebraic geometry --- rising-sea/notes/Morphisms of sheaves#_definition _ morphism of sheaves|sheaf morphisms]] between them as morphisms.

---

##### _example:_ silly but important example

$\mathscr{O}_{X}$ is a quasicoherent sheaf on $X$ since $\mathscr{O}_{X \mid \operatorname{Spec} A} \cong \mathscr{O}_{\operatorname{Spec} A} \cong \widetilde{A}$ for each affine open $\operatorname{Spec} A \subseteq X$.

---

Note that there are non-quasicoherent $\mathscr{O}_{X}$-modules!

##### _example:_ a non-quasicoherent sheaf

Let $X = \operatorname{Spec} \mathbb{F}[x]$. Let $\mathscr{F}$ be the [[Algebraic geometry --- rising-sea/notes/Sheaves#_example _ skyscraper sheaves|skyscraper sheaf]] supported at the origin $(x)$, taking value $\mathbb{F}(x)$ with the usual $\mathbb{F}[x]$-module structure. Since $0$ is an $A$-module for every ring, $\mathscr{F}(U)$ is an $\mathscr{O}_{X}(U)$-module for every $U$ not containing $(x)$. 

The open $U$ containing $(x)$ are all $X \setminus \{ p_{1}, \dots, p_{m} \}$ for some finite set $S = \{ p_{1}, \dots, p_{m} \}$ not containing $(x)$ and not containing the generic point. Writing $p_{i} = (x - a_{i})$, these can be thought of as $D\left( \prod_{i = 1}^m (x_{i} - a_{i}) \right)$. Thus, they have $\mathscr{O}_{X}(U) = \mathbb{F}[x]_{f}$, and $\mathbb{F}(x)$ is an $\mathbb{F}[x]_{f}$-module.

However, $0$ is not the localisation of $\mathbb{F}(x)$ away from $x$ — that is $\mathscr{F}(D(x)) = 0 \neq \mathbb{F}(x)_{x}$, and so $\mathscr{F}$ is not quasicoherent.

---

However, if we alter this to be a skyscraper sheaf at a generic point, it works fine.

##### _example:_ a quasicoherent skyscraper sheaf

Still with $X = \operatorname{Spec} \mathbb{F}[x]$, now choose the skyscraper sheaf supported at the generic point $(0)$, taking value $\mathbb{F}(x)$. This is the same as the constant sheaf $\underline{\mathbb{F}(x)}$ ([[Algebraic geometry --- rising-sea/notes/Affine schemes#_proposition _ generic points are near exactly the points of their closure|every non-empty open contains the generic point]]). This in turn is the same as the $\mathscr{O}_{X}$-module $\widetilde{\mathbb{F}(x)}$ — a quasicoherent sheaf. This is because $\mathbb{F}(x)$ is the [[Commutative algebra --- math-189AA/notes/Localisation of a ring#_definition _ localisation of a ring, localisations at a prime, fraction field|fraction field]] of $\mathbb{F}[x]$, so localising to distinguished opens doesn't change $\mathbb{F}(x)$ at all. That is, $\widetilde{\mathbb{F}(x)}(D(f)) = \mathbb{F}(x)_{f} = \mathbb{F}(x)$.

---

As usual, when we don't want to have to check quasicoherence on every affine open, we hope that quasicoherence is [[Algebraic geometry --- rising-sea/notes/Affine-locality and affine communication#_lemma, definition _ affine communication lemma, affine-local|affine-local]]. It is!

##### _proposition:_ quasicoherence is affine-local

Quasicoherence is an affine-local property. Specifically, for $f_{1}, \dots, f_{n}$ generating $A$ and an $\mathscr{O}_{\operatorname{Spec} A}$-module $\mathscr{F}$ the following implications hold.
1) If $\mathscr{F} \cong \widetilde{M}$ for some $A$-module $M$, then $\mathscr{F}_{\mid D(f_{i})} = \widetilde{M_{f_{i}}}$.
2) If each $\mathscr{F}_{\mid D(f_{i})} \cong \widetilde{M_{i}}$ for $A_{f_{i}}$-modules $M_{i}$, then $\mathscr{F} = \widetilde{M}$ for some $A$-module $M$.

###### _proof:_

The first hypothesis follows almost by definition — note that the distinguished opens of $D(f) = \operatorname{Spec} A_{f}$ are also distinguished in $\operatorname{Spec} A$. That is, for $g = g' / f^m \in A_{f}$ we have
$$
\begin{align}
\widetilde{M_{f_{}}}(D_{A_{f}}(g)) & = (M_{f_{}})_{g}  \\
& = M_{f_{} g'}  \\
& = \widetilde{M}(D_{ }(f_{} g))  \\
& = \widetilde{M}(D_{A}(f_{}) \cap D_{A}(g'))  \\
& = \widetilde{M}_{\mid D_{A}(f)}(D_{A_{f}}(g'))  \\
& = \widetilde{M}_{\mid D_{A}(f)}(D_{A_{f}}(g)).
\end{align}
$$

Now suppose we have $\mathscr{F}_{\mid D(f_{i})} \cong \widetilde{M_{i}}$ with $M_{i}$ an $A_{f_{i}}$-module. Since we have isomorphisms $\widetilde{M_{i}}_{\mid D(f_{i}) \cap D(f_{j})} \cong \widetilde{M_{j}}_{\mid D(f_{i}) \cap D(f_{j})}$  satisfying the cocycle condition, we have isomorphisms $\varphi_{ij} : (M_{i})_{f_{j}} \to (M_{j})_{f_{i}}$ (we will call this module $M_{ij}$) also satisfying the cocycle condition.

We claim that for $M = \mathscr{F}(\operatorname{Spec} A)$, we have $\mathscr{F} \cong \widetilde{M}$. By definition of $M$ the sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M \ar[r] & \prod_{i} M_{i} \ar[r, "\gamma"] & \prod_{i \neq j} M_{ij}
	\end{tikzcd}
\end{document}
```
is exact (with $\gamma$ on $M_{i} \to M_{ij}$ given by $m \mapsto m$ and on $M_{j} \to M_{ij}$ given by $m \mapsto -m$). But then since localisation is exact, we have
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M_{f_{1}} \ar[r] & \prod_{i} (M_{i})_{f_{1}} \ar[r, "\gamma_{f_{1}}"] & \prod_{i \neq j} (M_{ij})_{f_{1}}
	\end{tikzcd}
\end{document}
```
exact. That is, $M_{f_{1}}$ is the kernel of $\gamma_{f_{1}}$. We claim that $M_{1}$ is also the kernel of $\gamma_{f_{1}}$, giving an isomorphism $M_{f_{1}} \cong M_{1}$. This follows because we can rewrite each $(M_{i})_{f_{1}}$ as $(M_{1})_{f_{i}}$ and get an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M_{1} \ar[r] & \prod_{i} (M_{1})_{f_{i}} \ar[r, "\gamma_{f_{1}}"] & \prod_{i \neq j} (M_{1})_{f_{i} f_{j}}
	\end{tikzcd}
\end{document}
```
by the sheafiness of $\widetilde{M_{1}}$.

Note that to get $\widetilde{M} \cong \mathscr{F}$ it suffices to show isomorphisms $\widetilde{M}_{\mid D(f_{i})} \cong \mathscr{F}_{\mid D(f_{i})}$ on a cover of $\operatorname{Spec} A$ (now all values of the sheaf on open sets $U$ can be given by limits of other open sets already shown to be equal). However, it is nice to have the cocycle condition. That is, we want the diagram below to commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& M_{f_{i} f_{j}} \ar[rd, "\beta"] \ar[ld, "\alpha"'] \\
		(M_{i})_{f_{j}} \ar[rr, "\varphi_{ij}"] & & (M_{j})_{f_{i}}
	\end{tikzcd}
\end{document}
```

$\beta$ is the unique isomorphism expressing $M_{f_{i} f_{j}}$ as the kernel of the exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & (M_{j})_{f_{i}} \ar[r] & (\prod_{k} (M_{j})_{f_{k}})_{f_{i}} \ar[r, "\gamma_{f_{j}}"] & (\prod_{k \neq \ell} (M_{j})_{f_{k} f_{\ell}})_{f_{i}}
	\end{tikzcd}
\end{document}
```
But then, we can bring all the localisations away from $f_{i}$ into the $M_{j}$ to get a commutative diagram as below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & (M_{i})_{f_{j}} \ar[r] \ar[d, "\varphi_{ij}"] & (\prod_{k} (M_{i})_{f_{k}})_{f_{j}} \ar[r, "\gamma_{f_{i}}"] \ar[d, "\varphi_{ij}"] & (\prod_{k \neq \ell} (M_{i})_{f_{k} f_{\ell}})_{f_{j}} \ar[d, "\varphi_{ij}"] \\
		0 \ar[r] & (M_{j})_{f_{i}} \ar[r] & (\prod_{k} (M_{j})_{f_{k}})_{f_{i}} \ar[r, "\gamma_{f_{j}}"] & (\prod_{k \neq \ell} (M_{j})_{f_{k} f_{\ell}})_{f_{i}}
	\end{tikzcd}
\end{document}
```
This tells us that $\varphi_{ij}$ expresses $(M_{i})_{f_{j}}$ as the kernel of the $(M_{j})_{f_{i}}$ sequence and thus, that $\varphi_{ij} \circ \alpha$ expresses $M_{f_{i} f_{j}}$ as the kernel of the $(M_{j})_{f_{i}}$ sequence. This implies $\varphi_{ij} \circ \alpha = \beta$ as desired.

---

There are various ways to characterise quasicoherent sheaves by restricting attention to some open subsets of $X$.

##### _proposition:_ quasicoherence in terms of distinguished inclusions

Suppose $\mathscr{F}$ is an $\mathscr{O}_{X}$-module. Then $\mathscr{F}$ is quasicoherent if and only if, for each distinguished inclusion $\operatorname{Spec} A_{f} \subseteq \operatorname{Spec} A$ into an affine open of $X$, the factorisation
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{F}(\mathrm{Spec} \, A) \ar[rr, "\mathrm{res}"] \ar[rd] && \mathcal{F}(\mathrm{Spec} \, A_{f}) \\
		& \mathcal{F}(\mathrm{Spec} \, A)_{f} \ar[ru, "\alpha"]
	\end{tikzcd}
\end{document}
```
given by the universal property of localisation is given by an isomorphism $\alpha$.

###### _proof:_

Suppose $\mathscr{F}$ is quasicoherent. Then this follows from the definition.

Suppose $\mathscr{F}$ has $\alpha$ an isomorphism in the diagram above. Then each restriction $\mathscr{F}_{\mid \operatorname{Spec} A}$ agrees with some $\widetilde{M}$ on the [[Algebraic geometry --- rising-sea/notes/The base of distinguished open sets|the base of distinguished open sets]] of $\operatorname{Spec} A$. But then that's the definition of quasicoherence.

---

##### _example:_ the ideal sheaf of nilpotents

For any $f \in A$, there is an isomorphism of $A$-modules and $A_{f}$-modules $(\mathfrak{N}_{A})_{f} \cong \mathfrak{N}_{A_{f}}$. If $a^n = 0$ in $A$, then $a^n = 0$ in $A_{f}$ as well. That is, $a \in \mathfrak{N}_{A}$ implies $a / f \in \mathfrak{N}_{A_{f}}$. If $(a / f)^n = 0$ in $A_{f}$, then $f^m a^n = 0$ in $A$ and so $a f \in \mathfrak{N}_{A}$. We can write $a / f = af / f^{2} \in \mathfrak{N}_{A_{f}}$. 

Then, to define the quasicoherent **ideal sheaf of nilpotents** by $\mathfrak{N}_{X}(\operatorname{Spec} A) = \mathfrak{N}_{A}$ on any scheme $X$, we just need to check that this is compatible under gluing. This is just an application of [[Algebraic geometry --- rising-sea/notes/Affine-locality and affine communication#_lemma _ Nike's lemma|Nike's lemma]].

---

##### _example:_ the quasicoherent tensor product

Suppose $\mathscr{F}, \mathscr{G}$ are quasicoherent sheaves. The assignment $\mathscr{F} \otimes \mathscr{G}(U) = \mathscr{F}(U) \otimes \mathscr{G}(U)$ is not a sheaf. However, there is a unique quasicoherent sheaf defined by $\mathscr{F} \otimes \mathscr{G}(\operatorname{Spec} A) = \mathscr{F}(\operatorname{Spec} A) \otimes \mathscr{G}(\operatorname{Spec} A)$ and by the restrictions $\mathscr{F} \otimes \mathscr{G}(\operatorname{Spec} A) \to \mathscr{F} \otimes \mathscr{G}(D_{A}(f))$ given by localisation.

This satisfies the universal property of the tensor product, not only in $\mathsf{QCoh}_{X}$, but also in $\mathsf{Mod}_{\mathscr{O}_{X}}$. 

---

##### _lemma:_ the qcqs lemma

Suppose $X$ is a [[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#Qcqs|qcqs]] scheme, $\mathscr{F}$ is a quasicoherent sheaf on $X$ and $f \in \mathscr{O}_{X}(X)$ is a global function. Let $X_{f}$ be the locus where $f$ doesn't vanish. Then the restriction map $\operatorname{res}_{X_{f} \subseteq X}  : \mathscr{F}(X) \to \mathscr{F}(X_{f})$ is exactly localisation.

###### _proof:_

[[Algebraic geometry --- rising-sea/notes/Topological properties of schemes#_proposition _ characterising qcqs schemes|Since]] $X$ is qcqs, there exists a finite cover of $X$ by affine opens $U_{i} = \operatorname{Spec} A_{i}$ such that all pairwise intersections $U_{ij}$ are covered by finitely many affine opens $U_{ijk} = \operatorname{Spec} A_{ijk}$. Since there are finitely many of each affine cover, we can turn the products in the [[Algebraic geometry --- rising-sea/notes/Sheaves#_definition _ sheaf, separated presheaf|sheaf exact sequence]] into direct sums. That is,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{F}(X) \ar[r] & \bigoplus_{i} \mathcal{F}(U_{i}) \ar[r] & \bigoplus_{i, j, k} \mathcal{F}(U_{ijk})
	\end{tikzcd}
\end{document}
```
is exact. Since localisation [[Algebraic geometry --- rising-sea/notes/Exact functors#_example _ localisation is exact|is exact]] and [[Algebraic geometry --- rising-sea/notes/Localisation, categorically#_proposition _ localisation commutes with finite products and all coproducts|commutes with direct sums]], we see that
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathcal{F}(X)_{f} \ar[r] & \bigoplus_{i} \mathcal{F}(U_{i})_{f} \ar[r] & \bigoplus_{i, j, k} \mathcal{F}(U_{ijk})_{f}
	\end{tikzcd}
\end{document}
```
is exact. But then, since the $U_{i}$ and the $U_{ijk}$ are affine, by definition $\mathscr{F}(D_{U_{i}}(f)) = \mathscr{F}(U_{i})_{f}$. Also, these $D_{U_{i}}(f)$ are just the locus of $U_{i}$ where $f$ doesn't vanish, and thus, form a cover of $X_{f}$. The $D_{U_{ijk}}(f)$ also clearly form a cover of their pairwise intersections. But that means $\mathscr{F}(X)_{f}$ and $\mathscr{F}(X_{f})$ are both the kernel of the map $\bigoplus_{i} \mathscr{F}(U_{i})_{f} \to \bigoplus_{i, j, k} \mathscr{F}(U_{ijk})_{f}$. Thus, $\mathscr{F}(X)_{f} \cong \mathscr{F}(X_{f})$.

By the [[Algebraic geometry --- rising-sea/notes/Sheaves#_proposition _ identity and gluability axioms as a limit|limit property of sheaves]], the restriction is $\mathscr{F}(X) \to \mathscr{F}(X_{f})$ is the unique map that all the restriction maps $\mathscr{F}(X) \to \mathscr{F}(D_{U_{i}}(f))$ factor through. Since $f$ is invertible on these, they already factor through the localisation map. Thus, the restriction is exactly the localisation map.

---

### Torsion

Recall the definitions of torsion free modules and the torsion submodule of a module $M$ over a ring $A$. Recall that over an integral domain $A$, $M$ is torsion if and only if $M \otimes_{A} Q(A) = 0$. Quasicoherent sheaves allow us to extend this notion to sheaves.

##### _definition:_ torsion-free, torsion 

An $\mathscr{O}_{X}$-module $\mathscr{F}$ is **torsion-free** if $\mathscr{F}_{p}$ is a torsion-free $\mathscr{O}_{X, p}$-module for each $p \in X$.

A quasicoherent sheaf on a [[Algebraic geometry --- rising-sea/notes/Reduced and integral schemes#_definition _ reduced (schemes)|reduced scheme]] is **torsion** if its stalk at the generic point of every irreducible component is $0$.

---