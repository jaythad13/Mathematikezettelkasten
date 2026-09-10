---
tags:
- math-172/4
- alg
- rep-th
---

Let $G$ be a finite group.

Maschke's theorem tells us that our program of classifying irreducible representations makes sense! In particular, we will see that we can always break down an $\mathbb{F}[G]$ module into irreducible pieces.

##### _theorem:_ Maschke's theorem

Suppose $\mathbb{F}$ is a field of characteristic not dividing the order of $G$. Then $\mathbb{F}[G]$ is semisimple.

###### _proof:_

We first give the proof for $\mathbb{F}$ with a positive definite inner product.

Suppose $M$ is an $\mathbb{C}[G]$-module. Let $m_{1}, \dots, m_{n}$ be an $\mathbb{C}$-basis of $M$. We know what the Hermitian inner product is with respect to this basis. Denote the Hermitian inner product by $\left< m, n \right>$. We will use it to create a new inner product. The $G$-invariant inner product is
$$
\left< m, n \right>_{G} = \sum_{g \in G} \left< g\cdot m, g \cdot n \right>.
$$
It satisfies $\left< g \cdot m, g \cdot n \right>_{G} = \left< m, n \right>_{G}$. That is, we have created an inner product so that $G \to \mathrm{GL}(M)$ factors as $G \to \mathrm{O}(M, \left< -, - \right>_{G}) \to \mathrm{GL}(M)$. Thus, for any submodule $N_{1} \subseteq M$, we can choose $N_{2}$ to be the orthogonal complement of $N_{1}$ and we get $M = N_{1} \oplus N_{2}$.

More generally, the idea is to turn the $\mathbb{F}$-linear projection map $M \to N$ into an $\mathbb{F}[G]$-linear map. This projection gives a splitting of the exact sequence coming from $N \subseteq M$. Thus, we get $N$ as a direct summand of $M$.

One way to do this is to take $\mathbb{F}$-linear $\pi : M \to N$ and turn it into $\mathbb{F}[G]$-linear $\pi_{G} : M \to N$ by
$$
\pi_{G}(m) = \frac{1}{\# G} \sum_{g \in G} g \cdot \pi(g^{-1} \cdot m).
$$
$\pi_{G}$ has image in $N$ since $\pi$ has image in $N$ and $N$ is $G$-invariant. It is surjective and restricts to the identity on $N$ —
$$
\begin{split}
\pi_{G}(n) & = \frac{1}{\# G} \sum_{g \in G} g \cdot \pi(g^{-1} \cdot n) \\
 & = \frac{1}{\# G} \sum_{g \in G} g \cdot g^{-1} \cdot n \\
 & = n.
\end{split}
$$
Further, it is $G$-linear. It suffices to check that it commutes with the action of elements $h \in G$.
$$
\begin{split}
\pi_{G}(h \cdot m) & = \frac{1}{\# G} \sum_{g \in G} g \cdot \pi(g^{-1}h \cdot n) \\
 & = h \cdot \left( \frac{1}{\# G} \sum_{g \in G} h^{-1} g \cdot \pi(g^{-1} h \cdot n) \right) \\
 & = h \cdot \pi_{G}(m).
\end{split}
$$
Here the second inequality is just acting on the left by $h h^{-1}$.

---

##### _corollary:_ every representation is unitary

Every representation $G \to \mathrm{GL}_{n}(\mathbb{C})$ factors through $\mathrm{U}_{n}(\mathbb{C})$ (the group of unitary matrices).

###### _proof:_

Modify the Hermitian inner product to be the $G$-invariant inner product as before. Choose an orthonormal basis with respect to the $G$-invariant inner product. The resulting matrix is unitary.

---

Note, both proofs of Maschke's theorem used this idea of summing over all $g$ to make something $G$-invariant. This is a common argument — the **averaging argument**.