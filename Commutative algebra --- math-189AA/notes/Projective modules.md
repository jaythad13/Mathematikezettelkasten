---
tags:
- comm-alg
- math-189AA/7
- math-189AA/11
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

It isn't immediately obvious how to determine direct summands.

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

How do we know when a module is projective? Retractions help! A retraction is opposite to an inclusion of modules, and characterise when the inclusion describes a direct summand.

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
is split if and only if there is some (injection) $i : P \to M$ such that $g \circ i = \operatorname{id}_{P}$.

###### _proof sketch:_

$g$ is then a retraction $M \to P$ with kernel isomorphic to $N$.

---