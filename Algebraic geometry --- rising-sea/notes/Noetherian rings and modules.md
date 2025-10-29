---
tags:
- alg-geo
- comm-alg
- rising-sea/3/6
---

Let $A$ be a ring.

It turns out that almost every example of an affine scheme we have seen so far is the spectrum of a Noetherian ring. Noetherian rings generalise [[Abstract algebra --- math-171/notes/Factorisation in special rings#_definition _ principal ideal domain|principal ideal domains]] in the following sense — in a PID any increasing chain of ideals stabilises (see the [[Abstract algebra --- math-171/notes/Factorisation in special rings#_theorem _ Every PID is a UFD|proof that PIDs are UFDs]]). Noetherian rings just have this property.

##### _definition:_ Noetherian rings

$A$ is a **Noetherian ring** if every ascending chain of ideals is eventually constant.

That is, for any chain $\mathfrak{i}_{1} \subseteq \mathfrak{i}_{2} \subseteq \cdots$, there is some $r$ such that $\mathfrak{i}_{r} = \mathfrak{i}_{r + k}$ for all $k \in \mathbb{N}$.

---

These really do generalise PIDs — an equivalent definition of Noetherianness is that all ideals are finitely generated. We prove this by proving the more general statement for modules in the next section.

##### _proposition:_ Noetherian rings have all ideals finitely generated

$A$ is Noetherian if and only if all ideals $\mathfrak{i} \subseteq A$ are finitely generated.

---

Note that this implies that $\mathbb{Z}$, fields, PIDs, et c. are all Noetherian.

Many basic facts about preservation of Noetherianness are easy to prove (and we will prove them in the section on modules). For example, Noetherianness is preserved under quotients and localisation.

However, the following result is specifically about rings and relatively non-trivial.

##### _theorem:_ the Hilbert basis theorem

If $A$ is Noetherian, then so is $A[x]$.

###### _proof:_

We show that any ideal $\mathfrak{i} \subseteq A[x]$ is finitely generated. 

We produce a list of generators inductively. If $\mathfrak{i} \neq (f_{1}, \dots, f_{n})$, then let $f_{n + 1} \in \mathfrak{i} \setminus (f_{1}, \dots, f_{n})$ be non-zero and of least degree. Note then that $f_{1}$ is an element of $\mathfrak{i}$ of least degree (if $\mathfrak{i} \neq 0$). If this terminates (when $\mathfrak{i} \setminus (f_{1}, \dots, f_{n})$ is empty), then $A[x]$ is Noetherian. If this doesn't terminate, we show a contradiction from $A$'s Noetherianness

Suppose (by way of contradiction) this procedure doesn't terminate. Let $a_{i} \in A$ be the leading coefficient (of the largest power) for each $f_{i}$. Since $A$ is Noetherian, $(a_{1}, a_{2}, \dots) = (a_{1}, \dots, a_{N})$ for some $N$. This allows us to write $a_{N + 1} = \sum_{i = 1}^N b_{i} a_{i}$. Then consider
$$
g = f_{N + 1} - \sum_{i = 1}^N b_{i} f_{i} x^{\deg f_{N + 1} - \deg f_{i}}.
$$
$g \not\in (f_{1}, \dots, f_{N})$ since $f_{N + 1} \not\in (f_{1}, \dots, f_{N})$. Also, $g - f_{N + 1}$ has the same leading term as $= f_{N + 1}$ — the leading term is $- \sum b_{i} a_{i} x^{\deg f_{N + 1}} = a_{N + 1} x^{\deg f_{N + 1}}$. Thus, $g$ has zero leading term.

---

##### _examples:_ Noetherian and non-Noetherian rings

This result, with all the others, implies that all finitely generated $\mathbb{F}$-algebras and $\mathbb{Z}$-algebras and algebras over any Noetherian ring (and localisation of it) are Noetherian. Note of course, that not all rings are Noetherian — $\mathbb{F}[x_{1}, x_{2}, \dots ]$ is not Noetherian since $(x_{1}) \subseteq (x_{1}, x_{2}) \subseteq \cdots$ is an infinite strictly ascending chain of ideals.

---

Part of the reason we care about Noetherian rings is that their spectra are Noetherian topological spaces, which have nice properties.

##### _proposition:_ Noetherian rings have Noetherian affine schemes

If $A$ is a Noetherian ring, then $\operatorname{Spec} A$ is a [[Algebraic geometry --- rising-sea/notes/Noetherian topological spaces#_definition _ Noetherian topological spaces|Noetherian topological space]].

###### _proof:_

Let $V(\mathfrak{i}_{1}) \supseteq V(\mathfrak{i}_{2}) \supseteq \cdots$ be a descending chain of closed subsets. Then $\mathfrak{i_{1}} \subseteq \mathfrak{i}_{2} \subseteq \cdots$ is an ascending chain of ideals. Since $A$ is Noetherian, this chain is eventually constant, and thus, so is the chain of closed subsets.

---

##### _example:_ non-Noetherian and Noetherian affine schemes

We can get non-Noetherian $\operatorname{Spec} A$ from our favourite non-Noetherian ring — $\mathbb{F}[x_{1}, x_{2}, \dots]$. The closed subsets $V(x_{1}) \supseteq V(x_{1}, x_{2}) \supseteq \cdots$ form an infinite strictly descending chain (the codimension $1$ plane $V(x_{1})$ contains the codimension $2$ plane $V(x_{1}, x_{2})$ and so on). That is, $\mathbb{A}^\infty_{\mathbb{F}}$ is non-Noetherian.

However, $A$ need not be Noetherian for $\operatorname{Spec} A$ to be Noetherian. For example, $\mathbb{F}[x_{1}, x_{2}, \dots] / (x_{1}, x_{2}^{2}, \dots)$ is just the (closed) point $(x_{1}, x_{2}, \dots)$ and thus, is Noetherian. However, $(x_{1}) \subseteq (x_{1}, x_{2}) \subseteq \cdots$ is still an infinite strictly ascending chain of ideals. The relevant point here is that an infinite strictly ascending chain of ideals only gives an infinite strictly descending chain of closed sets if the chain of radicals is still strictly ascending.

---

### Noetherian modules

Properly, Noetherianness is really a condition about $A$-modules.

##### _definition:_ Noetherian modules.

An $A$-module $M$ is a **Noetherian module** if every ascending chain of submodules is eventually constant.

---

We can prove many of the same properties

Note that $A$ is a Noetherian $A$-module if and only if it is a Noetherian ring. Thus, all the analogous proofs still hold.

##### _proposition:_ Noetherian modules have all submodules finitely generated

An $A$-module $M$ is Noetherian if and only if every submodule is [[Commutative algebra --- math-189AA/notes/Finite generation and finite presentation#_definition _ finitely generated|finitely generated]].

###### _proof:_

Suppose $M$ is Noetherian. Let $N \subseteq M$ be a submodule. Consider the following ascending chain of submodules. We define $N_{1}$ to be the image of some $f_{1} : A \to N$. We define $N_{i + 1}$ to be the image of some $f_{i + 1} : A^{\oplus i} \oplus A \to N$ that restricts to $f_{i}$ on $A^{\oplus i}$, and if $f_{i}$ is not surjective, choose $f_{i + 1}(0, \dots, 0, 1) \in N \setminus N_{i + 1}$. This ascending chain must eventually stabilise. This ascending chain only stabilises when we have $A^{\oplus r} \to N$ surjective, so we must have such an $r$, and thus, we have $N$ finitely generated.

Suppose every submodule of $M$ is finitely generated. Consider an ascending chain of submodules $N_{1} \subseteq N_{2} \subseteq \cdots$. Let $N$ denote the union of all of these submodules, which is also a submodule. It is finitely generated. But all of its generators must then be contained in some $N_{r}$ after which the ascending chain is eventually constant.

---

We can prove a lot of useful results using a more general result about Noetherianness behaving well in short exact sequences. This is the advantage of proving things for modules rather than rings.

##### _proposition:_ Noetherianness behaves well in exact sequences

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M' \ar[r, "\varphi"] & M \ar[r, "\psi"] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is [[Algebraic geometry --- rising-sea/notes/Complexes and exactness#_definition _ complexes, exactness, short exact sequence|a short exact sequence]]. Then $M'$ and $M''$ are Noetherian if and only if $M$ is Noetherian.

###### _proof:_

Suppose $M$ is Noetherian. Let $N_{1}' \subseteq N_{2}' \subseteq \cdots$ and $N_{1}'' \subseteq N_{2}'' \subseteq \cdots$ be ascending chains in $M'$ and $M''$ respectively. By inclusion in $M$, $N_{1}' \subseteq N_{2}' \subseteq \cdots$ is an ascending chain in $M$ and thus, is eventually constant. 

Recall that $\psi^\text{pre}(N'')$ is a submodule of $M''$ and $\psi^\text{pre}$ is inclusion preserving. Then $\psi^\text{pre}(N_{1}'') \subseteq \psi^\text{pre}(N_{2}'') \subseteq \cdots$ is an ascending chain in $M$, and thus, eventually constant. Since $\psi$ is surjective, $\psi^\text{img}(\psi^\text{pre}(N'')) = N''$. Thus, this implies that the chain $N_{1}'' \subseteq N_{2}'' \subseteq \cdots$ is eventually constant.

Suppose $M'$ and $M''$ are Noetherian. Let $N_{1} \subseteq N_{2} \subseteq \cdots$ be an ascending chain in $M$. Then notice that $N_{i}' = \varphi^\text{pre}(N_{i}) = N_{i} \cap M'$ and $N_{j}'' = \psi^\text{img}(N_{i})$ form ascending chains in $M'$ and $M''$ respectively. Both of these are eventually constant. We claim this implies that the chain in $M$ is constant. It suffices to show that equality in both of the induced chains implies equality in the chain in $M$.

Suppose $N_{i} \subseteq N_{j} \subseteq M$ are submodules with $N_{i}' = N_{j}'$ and $N_{i}'' = N_{j}''$. Suppose $x \in N_{j}$. Then $\psi(x) \in N_{j}'' = N_{i}''$. By exactness, there is then some $y \in N_{i}$ such that $\psi(y) = \psi(x)$. But then $\psi(x - y) = 0$ so $x - y = \varphi(z)$ for some $z \in M'$. That is, $x - y \in N_{i}$ and $x - y \in M'$ so $x - y \in N_{i}' = N_{i} \cap M'$. But then $x - y + y \in N_{i}' + N_{i} = N_{i}$ so $x \in N_{i}$. That is, $N_{j} \subseteq N_{i}$.

---

##### _corollary:_ Noetherianness is preserved by direct sums

$M$ and $N$ are Noetherian if and only if $M \oplus N$ is Noetherian.

###### _proof sketch:_

Consider the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M \ar[r] & M \oplus N \ar[r] & N \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

---

This implies that all free modules over a Noetherian ring are Noetherian.

##### _proposition:_ Noetherianness is preserved by submodules and quotients

If $M$ is Noetherian and $N \subseteq M$ is a submodule, $N$ is Noetherian then $M / N$ is Noetherian.

Also, if $N \subseteq M$ and $M / N$ are Noetherian, then $M$ is Noetherian.

###### _proof sketch:_

Consider the short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r] & M \ar[r] & M / N \ar[r] & 0.
	\end{tikzcd}
\end{document}
```

---

Note that this only directly implies $A / \mathfrak{i}$ is a Noetherian $A$-module which, a priori, we don't know implies $A / \mathfrak{i}$ is a Noetherian ring. However, all $A/\mathfrak{i}$-submodules of $A / \mathfrak{i}$ are also $A$-submodules, so this suffices.

Also note that in combination with direct sums, this implies that all finitely generated modules over a Noetherian ring are Noetherian. Thus a submodule of a finitely generated module over a Noetherian ring is finitely generated (even better, it is Noetherian).

##### _proposition:_ Noetherianness is preserved by localisation

If $M$ is Noetherian, then $S^{-1} M$ is Noetherian.

###### _proof:_

Consider the canonical $\varphi : M \to S^{-1} M$ and note that all submodules of $L \subseteq S^{-1} M$ are $S^{-1} N$ for the submodule $N = \varphi^\text{pre}(L)$. 

Let $L_{1} \subseteq L_{2} \subset  \cdots$ be an ascending chain of submodules of $S^{-1} M$. Then $N_{i} = \varphi^\text{pre}(L_{i})$ form an eventually constant ascending chain of submodules of $M$ — $N_{1} \subseteq N_{2} \subseteq \cdots$ . Thus $S^{-1} N_{1} \subseteq S^{-1} N_{2} \subseteq \cdots$ is eventually constant. But this is just $L_{1} \subseteq L_{2} \subseteq \cdots$.

---