---
tags:
- antc
- matthew-gherman
---

### $G$-modules

> A $G$-module is a representation that loses some structure.

\- Matthew Gherman

The idea is that the invertibility of scalars makes vector spaces really rigid. Thus, we talk about $G$-modules —

##### _definition:_ $G$-module

A $G$-module is an abelian group $M$ with a group action $G \times M \to M$ such that $a \cdot(m_{1} + m_{2}) = a \cdot m_{1} + a \cdot m_{2}$.

##### _example:_ every representation is a $G$-module

Every representation is a $G$-module if we treat the vector space like an abelian group.



### Group cohomology

The $\mathbb{Z}/2\mathbb{Z}$ example of how you lose surjectivity when you look at $\mathbb{Z} /2\mathbb{Z}$ invariant parts of $\mathbb{Z}$, $2 \mathbb{Z}$, and $\mathbb{Z} / 2\mathbb{Z}$.

What is a group cohomology?

Think about all the functions $G^n \to M$ where $M$ is a $G$ module.

We define a thing $d^n$ that sends functions $f : G^n \to M$ to functions $g : G^{n + 1} \to M$. This gives us a chain complex (a weaker version of an exact sequence is). Then the $n$th cohomology group is $H^n(G, M) = \ker d^n/\operatorname{im} d^n$.

Basically the $n$th cohomology group is all maps that satisfy the exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		1 \ar[r] & M \ar[r] & E_1 \ar[r] & \cdots \ar[r] & E_{n - 1} \ar[r] & 1
	\end{tikzcd}
\end{document}
```
with some conditions (for $n = 2$, it's central extensions).

### Approximating Galois cohomology

Negligible classes go to zero in any approximation.

### Questions

What is the module that you usually care about for Galois cohomology?

By approximate really well, do you mean the quotient group is small?

Everything in the big Galois group appears in one of the small Galois groups.
