---
tags:
- uc-2026/de-rham/6
- alg-geo
- michael-barz
---

Here we want to study the elliptic curve $y^{2} = x^{3} + 1$. We can think of this as a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Affine and projective algebraic curves#_definition _ projective plane curve|projective curve]] in $\mathbb{C} \mathbb{P}^{2}$ with homogeneous coordinates. We can also think of this as a compact Riemann surface by taking two $\mathbb{C} \mathbb{P}^1$s and on each of them, making two branch cuts from $-1$ to $\infty$ and $-\omega$ to $-\omega^{2}$ (so that $\sqrt{ x^{3} + 1 }$ is well defined). Then gluing, we can see that it is a torus! Gauss knew this.

Gauss also wanted to count the solutions to this modulo $p$. Remember, by Hensel's lemma and Chinese remainder theorem this gives all solutions modulo any $n \in \mathbb{N}$.

### The easiest case

Suppose $p \equiv 0 \pmod 3$, that is $p = 3$. There are $3$ solutions — $(0, 1), (0, 2), (2, 0)$. Thus, $N_{3} = 3$.

### The next easiest case

Suppose $p \equiv 2 \pmod 3$. Then $x \mapsto x^{3} + 1$ is a bijection $\mathbb{Z} / (p) \to \mathbb{Z} / (p)$. It suffices to show $x \mapsto x^{3}$ is a bijection. Powers of $3$ on $\mathbb{Z} / (p)^\times$ are the same as scaling by $3$ on $\mathbb{Z} / (p - 1)$. Since $p - 1 \equiv 1 \pmod 3$, multiplying by $3$ is a bijection on $\mathbb{Z} / (p - 1)$.

Thus, counting the solutions to $y^{2} = x^{3} + 1$ is the same as counting solutions to $y^{2} = z$. But there are exactly $p$ of these for each of the $p$ values of $y$. Thus, $N_{p} = p$.

Another way to say this is that there are unique cube roots of each number in $\mathbb{Z} / (p)$ (when $p \equiv 2$). Thus, the number of solutions is just indexed by choosing $y$ and then we are forced to choose $x = \sqrt[3]{ y^{2} - 1 }$.

### The hard case

Finally, suppose $p \equiv 1 \pmod 3$. Note that we don't have the same argument we did before. However, we can generalise its rephrasing —
$$
N_{p} = \sum_{y = 0}^{p - 1} \#\{ \sqrt[3]{ y^{2} + 1 } \in \mathbb{Z} / (p) \}.
$$
We already know how to get the number of square roots modulo $p$ in terms of the Legendre symbol.
$$
\# \{ \sqrt{ a } \in \mathbb{Z} / (p) \} = 1 + \left( \frac{a}{p} \right).
$$

Think of $\mathbb{Z} / (3)$ as the subgroup of $\mathbb{C}^\times$ given by cube roots of unity. Then there are three group homomorphisms $\mathbb{Z} / (p)^\times \to \mathbb{Z} / (3)$ given by $1 \mapsto 1, \omega, \omega^{2}$ respectively. Call these $1, \chi, \overline{\chi}$ respectively.  We claim 
$$
\# \{ \sqrt[3]{ a } \in \mathbb{Z} / (p) \} = 1 + \chi(a) + \overline{\chi}(a).
$$

Thus,
$$
\begin{align}
N_{p} & = p + \sum_{y = 0}^{p - 1} \chi(y^{2} - 1) + \sum_{y = 0}^{p - 1} \overline{\chi}(y^{2} - 1) \\
 & = p + \varpi + \overline{\varpi} \\
 & = p + O(\sqrt{ p }) \\
 & = O(p)
\end{align}
$$
The last step is as follows. Gauss and Jacobi knew, by factoring $p$ in $\mathbb{Z}[\omega]$, that
$$
\left( \sum_{y = 0}^{p - 1} \chi(y^{2} - 1) \right) \left( \sum_{y = 0}^{p - 1} \overline{\chi}(y^{2} - 1) \right) = \varpi + \overline{\varpi} = p
$$
always. But then this tells us that $\varpi$ and its conjugate both have norm $\sqrt{ p }$.