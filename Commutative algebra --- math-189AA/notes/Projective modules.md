---
tags:
- comm-alg
- hom-alg
- math-189AA/7
- math-189AA/11
- math-189AA/13
- math-189AA/15
---

If $A$ is the best $A$-module, and free modules are second best, then the third best are their direct summands — projective modules.

##### _definition:_ direct summand

For an $A$-module $P$ we say an $A$-module $M$ is a direct summand of $P$ if $P \cong M \oplus N$. 

Note that we don't require $M, N$ to be submodules of $P$ and the direct sum to be internal.

---

##### _definition:_ projective module

An $A$-module $M$ is projective if it is a direct summand of a [[Commutative algebra --- math-189AA/notes/Modules#_example _ free modules|free module]]. That is, there is some $A$-module $N$ so that $M \oplus N \cong \bigoplus_{i \in \mathscr{I}} A$.

---

##### _example:_ projective modules

Since $\mathbb{Z} / (6) \cong \mathbb{Z} / (2) \oplus \mathbb{Z} / (3)$, the two modules $\mathbb{Z} / (2)$ and $\mathbb{Z} / (3)$ are projective $\mathbb{Z} / (6)$-modules.

---

### Splitting and retractions

It isn't immediately obvious how to determine direct summands. However, short exact sequences can once again, [[Commutative algebra --- math-189AA/notes/Complexes and exact sequences of modules#_example _ exact sequences tell you things|tell us things]]. 

##### _definition:_ split short exact sequence

A short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r, "f"] & M \ar[r, "g"] & P \ar[r] & 0
	\end{tikzcd}
\end{document}
```
**splits** if $M \cong N \oplus P$ with $f$ the natural inclusion $N \to N \oplus P$ and $g$ the surjection $0_{N} \oplus \operatorname{id}_{P} : N \oplus P \to P$.

---

##### _example:_ split short exact sequence

The simplest example of this is over vector spaces — the rank-nullity theorem is essentially saying that for a linear map $T : V \to W$, the following short exact sequence splits —
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker T \ar[r] & V \ar[r] & \mathrm{img} \, T \ar[r] & 0
	\end{tikzcd}
\end{document}
```

---

How do we know when a short exact sequence splits? Retractions! A retraction is opposite to an inclusion of modules, and characterise when the inclusion describes a direct summand.

##### _definition:_ retraction

For $N \subseteq M$ an $A$-submodule, a **retraction from $M$ to $N$** is a module homomorphism $\rho : M \to N$ such that $\rho_{\mid N} = \operatorname{id}_{\mid N}$.

---

##### _proposition:_ retractions characterise direct summands

A submodule $N \subseteq M$ is a direct summand of $M$ if and only if there exists a retraction $\rho : M \to N$.

###### _proof:_

It's clear that if $M = N \oplus P$, then $\operatorname{id}_{N} \oplus 0_{P} : M \to N$ is the desired retraction. 

If $\rho : M \to N$, we show that $M = N \oplus \ker \rho$. Suppose $m \in M$. Then $m = \rho(m) +  m - \rho(m)$. Since $\rho(m - \rho(m)) = \rho(m) - \rho(m) = 0$, we have $m - \rho(m) \in \ker \rho$. Thus, $M = N + \ker \rho$. Since $\rho_{\mid N} = \operatorname{id}_{N}$, the intersection $N \cap \ker \rho$ is $\ker \rho_{\mid N} = 0$. Thus the sum is a direct sum — $M = N \oplus \ker \rho$.

---

For example, this gives a characterisation of split exact sequences.

##### _corollary:_ retractions characterise split exact sequences

A short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r, "f"] & M \ar[r, "g"] & P \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is split if and only if there is some (injection) $i : P \to M$ such that $g$ is a retraction onto $P$.

###### _proof:_

Suppose the short exact sequence splits — $M \cong N \oplus P$ with $f^\text{img}(N) \cong N$ and $g$ the surjection $N \oplus P \to P$. Then consider the standard inclusion $i : P \to N \oplus P$. Clearly $g \circ i = \operatorname{id}_{P}$. That is, $g$ is a retraction $M \to P$.

Suppose $g$ is a retraction $M \to P$. It has $\ker g \cong N$ by exactness. But a retraction $g : M \to P$ gives $M = \ker g \oplus P$ and thus, $M \cong N \oplus P$.

---

One easy example of this in action (and a more general case of the rank-nullity theorem) is that free cokernels always split.

##### _example:_ free cokernels always split

If $P = A^{\oplus \mathscr{I}}$ is free then 
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker g \ar[r] & M \ar[r, "g"] & P \ar[r] & 0
	\end{tikzcd}
\end{document}
```
splits. Let $( e_{i} )_{i \in \mathscr{I}}$ be a basis for $P$. Since $g$ is surjective, we can choose $u_{i} \in M$ such that $g(u_{i}) = e_{i}$. We claim the map $j : P \to M$ by $e_{i} \mapsto u_{i}$ describes $\pi$ as a retraction. Specifically, we claim $M = \ker g \oplus \left< u_{i} \right>$, and since $\left< u_{i} \right> \cong P$ clearly, we are done.

Since each $m \in M$ is determined by its equivalence class $m + \ker g$ plus the information of which element in $\ker g$, clearly $M = \ker g + \left< u_{i} \right>$. If $\sum a_{i} u_{i} \mapsto 0$ under $g$, then all $\sum a_{i} e_{i} = 0$ and so all $a_{i} = 0$. Thus, $\ker g \cap \left< u_{i} \right> = 0$.

Note that this requires the axiom of choice to choose the basis of $P$.

---

The complete characterisation of all modules that behave like this is that they are projective. This allows us to give a complete characterisation of projective modules, including why they are called projective.

##### _theorem:_ characterising projective modules

The following are equivalent for any $A$-module 
1) $P$ is projective
2) Given any surjection $\rho : M \to N$ and homomorphism $h : P \to N$ there exists some $\overline{h} : P \to M$ (a lift of $h$) so that $\rho \circ \overline{h} = h$. That is, the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M \ar[r, "\rho", two heads] & N \\
		& P \ar[ul, dashed, "\exists \overline{h}"] \ar[u, "h"]
	\end{tikzcd}
\end{document}
```
3) Any short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r] & M \ar[r] & P \ar[r] & 0
	\end{tikzcd}
\end{document}
```
splits.

###### _proof:_

We show (1) implies (2) implies (3) implies (1).

Suppose $P$ is projective with $P \oplus Q$ free. Then consider the following diagram.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M \ar[r, "\rho"] & N \ar[r] & 0 \\
		& P \ar[u, "h"] \ar[d, "i", shift left] \\
		& P \oplus Q \ar[u, "\pi", shift left] \ar[uul, bend left, "\overline{g}"]
	\end{tikzcd}
\end{document}
```
Let $(e_{i})$ be a basis for $P \oplus Q$. Let $g = h \circ \pi : e_{i} \to n_{i}$. Also, by surjectivity of $\rho$, choose $m_{i} \in M$ such that $\rho : m_{i} \mapsto n_{i}$. Note that this defines a linear map $\overline{g} : P \oplus Q \to M$ with $e_{i} \mapsto m_{i}$ with $\rho \circ \overline{g} = g$. Define $\overline{h} = \overline{g} \circ i$. It follows that
$$
\begin{align}
\rho \circ \overline{h} & = \rho \circ \overline{g} \circ i \\
 & = g \circ i \\
 & = h \circ \pi \circ i \\
 & = h \circ \operatorname{id}_{P} \\
 & = h
\end{align}
$$
as desired.

Suppose the relevant diagram commutes for (2) to be true. Then the following diagram commutes for any $g : M \to P$ and corresponding short exact sequence.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r] & M \ar[r, "g"] & P \ar[r] & 0 \\
				& & & P \ar[u, "\mathrm{id}_{P}"] \ar[ul, "j"]
	\end{tikzcd}
\end{document}
```
The commutativity of this diagram clearly implies that $g$ is a retraction with $j \circ g = \operatorname{id}_{P}$.


Suppose any short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r] & M \ar[r] & P \ar[r] & 0
	\end{tikzcd}
\end{document}
```
splits. Then, since every module is the cokernel of a free module, write $g : A^{\oplus \mathscr{I}} \to A^{\oplus \mathscr{I}} / \ker g \cong P$ and consider the exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker g \ar[r] & A^{\oplus \mathcal{I}} \ar[r, "g"] & P \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
For this to split is exactly for $P$ to be a direct summand of $A^{\oplus \mathscr{I}}$ and thus, projective.


---

### Projectives are useful

Projective modules can be very useful. One example is Schanuel's lemma which allows us to compare exact sequences when the middle term is projective and the right term is the same.

##### _lemma:_ Schanuel's lemma

Suppose
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & K \ar[r] & P \ar[r] & M \ar[r] & 0
	\end{tikzcd}
\end{document}
```
and
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & K' \ar[r] & P' \ar[r] & M \ar[r] & 0
	\end{tikzcd}
\end{document}
```
are exact with $P$ and $P'$ projective. Then $P \oplus K' \cong P \oplus K$.

###### _proof:_

We construct $\alpha$ and $\beta$ so that the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & K \ar[r, "i"] \ar[d, dashed, "\alpha"] & P \ar[r, "\pi"] \ar[d, dashed, "\beta"] & M \ar[r] \ar[d, "\mathrm{id}_{M}"] & 0 \\
		0 \ar[r] & K' \ar[r, "i'"] & P' \ar[r, "\pi'"] & M \ar[r] & 0 \\
	\end{tikzcd}
\end{document}
```
$\beta$ exists by the universal property of $P$ projective — we are given $\pi' : P' \to M$ surjective and $\pi : P \to M$, so there is a lift $\beta : P \to P'$ such that $\pi' \circ \beta = \pi$, and thus, $\pi' \circ \beta = \operatorname{id}_{M} \circ \pi$. That is, the right square commutes.

To construct $\alpha$, note that exactness means it suffices to show $\operatorname{img} \beta \circ i \subseteq \ker \pi'$. But by commutativity of the right square, we have $\pi' \circ \beta \circ i = \operatorname{id}_{M} \circ \pi \circ i = 0$ (by exactness, $\pi \circ i = 0$). Thus, for each $k \in K$ choose $k \mapsto k'$ uniquely (by injectivity of $i'$) such that $i'(k') = \beta \circ i(k)$. By construction $\alpha$ makes the left square commute.

Consider $\psi : K' \oplus P \to P'$ by $(k', p) \mapsto \beta(p) - i'(k')$. Clearly, if $(k', p) = (\alpha(k), i(k))$, then $\psi(k', p) = 0$ by commutativity of the left square. Conversely, $\ker \psi$ contains all all $(k', p)$ such that $\beta(p) = i'(k')$. But then $\pi'(\beta(p)) = \pi'(i'(k')) = 0$. By commutativity, this means $\operatorname{id}_{M}(\pi(p)) = \pi(p) = 0$. Now, since $p = i(k)$, we have $i'(k') = \beta(p) = \beta(i(k))$. By commutativity of the square, $i'(k') = i'(\alpha(k))$. Since $i'$ is injective, $k' = \alpha(k)$. We have shown $K \cong \ker \psi$ by $k \mapsto (\alpha(k), i(k))$.

This means that we have a short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & K \ar[r] & K' \oplus P \ar[r, "\psi"] & P' \ar[r] & 0.
	\end{tikzcd}
\end{document}
```
Since $P'$ is projective, it splits and we get $K' \oplus P \cong K \oplus P'$.

---