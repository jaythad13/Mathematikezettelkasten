---
tags:
- math-189AA/23
- math-189AA/24
- comm-alg
---

Depth provides one such example.

##### _example:_ depth of a polynomial ring

Let $A = \mathbb{F}[x, y, z]$. Not only are $x, y, z$ non-unit, non-zero-divisors, they are also non-zero-divisors in sequence. That is, $x$ is not a zero divisor in $A$, $y$ is not a zero divisor in $A / (x)$, and $z$ is not a zero divisor in $A / (x, y)$. Finally, $A / (x, y, z) = \mathbb{F}$, which has no more non-unit non-zero-divisors left to mod out by. We say $A$ has depth $3$. This is exactly what we might expect by looking at the ring.

---

By Noetherianness, adding finitely many non-units will eventually get us to a maximal ideal, and then we will have nothing no more non-zero non-units to mod out by. Thus, depth is a sensible notion of Noetherian rings.

##### _example:_ depth of $\mathbb{Z}$-modules

Consider $M = \mathbb{Q} / \mathbb{Z}$ as a $\mathbb{Z}$-module. Evert $n \in \mathbb{Z}$ kills the non-zero $1 / n \in M$. Thus, every $n \in \mathbb{Z}$ is a zero-divisor on $M$. Since there are no non-zero-divisors on $M$, it has depth $0$.

$N = \mathbb{Q}$ as a $\mathbb{Z}$-module has depth $1$. Any $a \in \mathbb{Z}$ is a non-zero divisor, but then $\mathbb{Q} / a \mathbb{Q} = 0$ and we are done.

---

We define some language to capture this notion of non-zero-divisors on a module.

##### _definition:_ regular elements on a module, regular sequence, maximal regular sequence

Let $M$ be an $A$-module. $x \in A$ is $M$-regular or regular on $M$ if $xm = 0$ implies $m = 0$ and $M / (x) M \neq 0$.

A sequence of elements $x_{1}, \dots, x_{n} \in A$ is $M$-regular if $x_{i}$ is regular on $M / (x_{1}, \dots, x_{i - 1}) M$ and $M / (x_{1}, \dots, x_{n}) M \neq 0$.

An $M$-regular sequence is maximal if it cannot be extended to a longer $M$-regular sequence.

---

##### _example:_ a surprising example

For $\mathbb{F}[x, y, z, w] / (x, y) \cap (z, w)$ we surprisingly have a regular sequence of length $1$. Specifically, $x + z$ is a maximal regular sequence.

---

It's only natural that we should define depth as the maximal length of a regular sequence. However, it's not obvious that this is well-defined. This is only true when $A$ is local as well. We will use homological algebra to prove this.

##### _definition:_ depth

Let $A$ be a Noetherian local ring, and $M$ a finitely generated $A$-module. The **depth** of $M$ is the length of a maximal sequence of $M$-regular elements in $A$.

---

##### _proposition:_ depth is well-defined

Let $A, \mathfrak{m}, \kappa$ be a Noetherian local ring. Let $M$ be a finitely generated $A$-module. Then $\operatorname{depth}_{A} M = \min \{ i \mid \operatorname{Ext}^i_{A}(\kappa, M) \neq 0 \}$. Thus, depth is well-defined.

###### _proof sketch:_

We claim that if $\operatorname{Hom}(\kappa, M) = 0$, then $\operatorname{Ann}_{A} \kappa = \mathfrak{m}$ contains an $M$-regular element. This is because if $\mathfrak{m}$ consists only of zero-divisors, then $\mathfrak{m}$ is an associated prime, and there is an injection $\kappa = A / \mathfrak{m} \to M$.

We claim that if $x_{1}, \dots, x_{n}$ is an $M$-regular sequence generating the ideal $\mathfrak{i}$ in $\operatorname{Ann}_{A} N$, then $\operatorname{Hom}(N, M / \mathfrak{i} M) \cong \operatorname{Ext}^n(N, M)$. We prove this by induction. We show only the base case.

Since $x_{1}$ is regular on $M$, we get a short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M \ar[r, "\times x_{1}"] & M \ar[r] & M / x_{1} M \ar[r] & 0
	\end{tikzcd}
\end{document}
```
and thus, a long exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	0 \ar[r] & \mathrm{Hom}(N, M) \ar[r, "\times x_{1}"] & \mathrm{Hom}(N, M) \ar[r] & \mathrm{Hom}(N, M / x_{1} M) \ar[r] & \, \\
	\, \ar[r] & \mathrm{Ext}_{A}^1(N, M) \ar[r, "\times x_{1}"] & \mathrm{Ext}_{A}^1(N, M) \ar[r] & \cdots
	\end{tikzcd}
\end{document}
```

Since $x_{1} \in \operatorname{Ann}_{A} N$, we have $\operatorname{Hom}(N, M) = 0$. In fact, the "$\times x_{1}$" map is the zero map. Since we have $\operatorname{Hom}_{A}(N, M / x_{1} M) \to \operatorname{Ext}_{A}^1(N, M)$ sandwiched between two zero maps, they are isomorphic. 

Choose $N = \kappa$ and induct on $n$, the length of the regular sequence.

---

##### _example:_ 

Consider $A = \kappa[x, y] / (x^{2}, y^{2})$. Note that this is local with maximal ideal $\mathfrak{m} = (x, y)$. Then every non-unit annihilates $\mathfrak{m}$, so $\operatorname{depth}_{A} \mathfrak{m} = 0$.

---
