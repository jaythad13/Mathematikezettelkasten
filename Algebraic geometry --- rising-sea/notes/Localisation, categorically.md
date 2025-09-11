---
tags:
- rising-sea/1/2
- cat-th
- alg
- comm-alg
---

### Localisation of rings

One very important example of a definition by [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal property]] is that of localisation (of [[Abstract algebra --- math-171/notes/Rings#What's a ring?|(commutative, unital) rings]] and modules). Recall the constructive definition of localisation as follows:

![[Commutative algebra --- math-189AA/notes/Localisation of a ring#What is localisation?|Localisation]]

##### _proposition:_ the universal property of localisation

$S^{-1} A$ is initial among $A$-algebras $B$ where every element of $S$ is sent to an invertible element in $B$. That is, there is a unique map $S^{-1} A \to B$ such that the composition with $A \to S^{-1} A$ is the structure map $A \to B$.

###### _proof:_

Suppose $B$ is an $A$-algebra with $\varphi : A \to B$ the structure homomorphism and $\varphi^\text{img}(S) \in B^\times$. Then consider $\psi : S^{-1} A \to B$ with $a / s \mapsto \varphi(a) / \varphi(s)$ for all $a \in A$ and $s \in S$. Then consider the composition $A \to S^{-1}A \to B$. For each $a \in A$ we have $a \mapsto a / 1 \mapsto \varphi(a) / 1$ so the composition is just $\varphi$.

If $\psi' : S^{-1} A \to B$ also satisfies the composition $A \to S^{-1} A \to B$ being $\varphi$, then $\psi'(a / 1) = \varphi(a)$ for all $a$, and in particular $\psi'(s) = \varphi(s)$ for each $s \in S$. Since $s (a / s) = a$, we have $\psi'(s) \psi(a / s) = \varphi(s) \varphi(a) / \varphi(s)$ and finally, cancelling $\psi'(s) = \varphi(s)$ on both sides, we have $\psi'(a / s) = \varphi(a) / \varphi(s)$. Thus, $\psi' = \psi$.

From this definition it's obvious that if $A$ is a field, then its localisation by any multiplicative set is just itself. 

### Localisation of modules

We use the universal property to extend to a definition of localisation of modules. This yields a cleaner characterisation up to unique isomorphism which we verify actually exists.

##### _construction:_ localisation of a module

Suppose $M$ is an $A$-module and $S \subseteq A$ is multiplicative. $S^{-1} M$ (with a distinguished $\alpha : M \to S^{-1} M$) is the initial $A$-module in the category of modules $N$ with a distinguished $A$-module map $M \to N$ such that the action of $S$ is invertible (as a module map) on $N$.

That is, for any $\varphi : M \to N$ there is a unique $\psi : S^{-1} M \to N$ such that $\psi \circ \alpha = \varphi$ —
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M \ar[r, "\alpha"] \ar[rd, "\varphi"] & S^{-1} M \ar[d, dotted, "\exists ! \psi"] \\
		& N
	\end{tikzcd}
\end{document}
```

###### _proof:_

The uniqueness follows from a standard universal property argument.

A concrete construction is as follows. Let
$$
S^{-1} M = \{ m / s \mid m \in M, s \in S \} / \sim
$$
with $m_{1} / s_{1} \sim m_{2} /s_{2}$ if and only if $s(m_{1} s_{2} - m_{2} s_{1}) = 0$ for some $s \in S$, addition defined by
$$
\frac{m_{1}}{s_{1}} + \frac{m_{2}}{s_{2}} = \frac{m_{1} s_{2} + m_{2} s_{1}}{s_{1} s_{2}}
$$
and scaling defined by
$$
a \frac{m}{s} = \frac{a m}{s}.
$$
Notice that this also defines an $S^{-1} A$-module structure by $(a / s) m = am / s$.

Let the localisation map be $\alpha : m \mapsto m / 1$. Then for any $\varphi : M \to N$ such that the action of $S$ is invertible on $N$, we have $\psi : m / s \mapsto \varphi(m) / s$ giving $\psi \circ \alpha = \varphi$. If any other $\psi'$ has $\psi' \circ \alpha = \varphi$, then we must have $\psi'(m / 1) = \varphi(m)$ for all $m$. Since $\psi'(s m / s) = \psi'(m) = \varphi(m)$, by linearity $s \psi'(m / s) = \varphi(m)$ finally giving the $\psi'(m / s) = \varphi(m) / s$. Here $\varphi(m) / s$ is used to denote the inverse of the "multiplication by $s$" map evaluated at $\varphi(m)$.


##### _proposition:_ localisation commutes with finite products and all coproducts

If $M_{1}, \dots, M_{n}$ are $A$-modules, then there is an isomorphism (of $A$-modules and $S^{-1} A$-modules) $S^{-1} (M_{1} \times \dots \times M_{n}) \to S^{-1} M_{1} \times \dots \times S^{-1} M_{n}$.

If $\{ M_{i} \}_{i \in \mathscr{I}}$ is a collection of modules, then there is an isomorphism (of $A$-modules and $S^{-1} A$-modules)
$$
S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i} \to \bigoplus_{i \in \mathscr{I}} S^{-1}M_{i}.
$$


###### _proof:_

Let the morphisms $pr_{i} : \prod_{i = 1}^n M_{i} \to M$ define the product structure and let $S^{-1} pr_{i} : S^{-1} \prod_{i = 1}^n M_{i} \to S^{-1} M_{i}$ be given by $m / s \mapsto pr_{i}(m) / s$. Suppose $P'$ has morphisms $\sigma_{i}': P' \to M_{i}$. Then we can define $\Pi : P' \to S^{-1} \prod_{i = 1}^n M_{i}$ by
$$
\Pi(p) = (S^{-1}\mu_{1}'(p), \dots, S^{-1}\mu_{n}'(p)) = \frac{(m_{1} \hat{s}_{1}, \dots, m_{n} \hat{s}_{n})}{s}
$$
where $\sigma_{i}'(p) = m_{i} / s_{i}$, and we set $s = s_{1} \cdots s_{n}$ and $\hat{s}_{i} = s / s_{i}$. Clearly $S^{-1}pr_{i} \circ \pi = \sigma_{i}'$ for each $i$. 

Suppose $\Pi' : P' \to S^{-1} \prod_{i = 1} M_{i}$ has $S^{-1} pr_{i} \circ \pi' = \sigma_{i}'$ for each $i$. Then for $m' / s' = \Pi'(p)$, we must have $S^{-1}pr_{i}(m' / s') = m_{i} / s_{i}$. Thus, $pr_{i}(m') / s = m_{i} / s_{i}$ and finally $pr_{i}(m') = s m_{i} / s_{i}$ for each $i$. This determines $m' = (s m_{1} / s_1, \dots, s m_{n} / s_{n})$ which finally gives
$$
\Pi'(p) = \frac{m'}{s} = (s m_{1} / s_{1}, \dots, s m_{n} / s_{n}) / s = (m_{1} / s_{1}, \dots, m_{n} / s_{n})  = \Pi(p).
$$
That is, $\Pi' = \Pi$, or $\Pi$ is unique. Thus, $S^{-1} \prod_{i = 1}^n M_{i}$ satisfies the universal property of the product $\prod_{i = 1}^n S^{-1} M_{i}$, and is uniquely isomorphic to it. Note that we could have also made an argument by the universal property of localisation.

Note that direct sums of modules are just coproducts. Thus, we can use the [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?|universal property of coproducts]]. In particular, let $pr_{i} : M_{i} \to \bigoplus_{i \in \mathscr{I}} M_{i}$ define the coproduct and let $S^{-1} pr_{i} : S^{-1} M_{i} \to S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i}$ be given by $m_{i} / s \mapsto pr_{i}(m) / s$. Suppose $P'$ has morphisms $\sigma_{i}' : S^{-1}M_{i} \to P'$. We claim there is a unique $\amalg : S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i} \to P'$ such that $\amalg \circ S^{-1} pr_{i} = \sigma_{i}'$. We define
$$
\amalg(m_{i} / s) = \sigma_{i}'(m_{i}/s)
$$
for each $i$ and extend linearly. Clearly this is the desired map.

Suppose $\amalg' : S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i} \to P'$ has $\amalg \circ S^{-1} pr_{i} = \sigma_{i}'$. Then, for each $i$, we must have exactly the defining property of $\amalg$ —
$$
\amalg(m_{i} / s) = \sigma'_{i}(m_{i} / s).
$$
Thus, $\amalg' = \amalg$, $\amalg$ is unique, and $S^{-1} \bigoplus_{i \in \mathscr{I}} M_{i}$ satisfies the universal property of the direct sum $\bigoplus_{i \in \mathscr{I}} S^{-1} M_{i}$ and is isomorphic to it.

Note that localisation does not necessarily commute with infinite products — in particular the unique map
$$
S^{-1} \prod_{i \in \mathscr{I}} M_{i} \to \prod_{i \in \mathscr{I}} S^{-1} M_{i}
$$
given by the universal property of localisation is not necessarily an isomorphism. For a specific example, the unique map $(\mathbb{Z}^\times)^{-1} \prod_{i \in \mathbb{N}} \mathbb{Z} \to \prod_{i \in \mathbb{N}} \mathbb{Q}$ has no pre-image for the point $(1, 1 / 2, 1 / 3, 1 / 4, \dots) = (1 / n)_{n \in \mathbb{N}}$, and thus, is not an isomorphism.