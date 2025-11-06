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

---

