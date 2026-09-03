---
tags:
- alg
- math-174/2
---

Let $A$ be a (commutative, unital) ring.

##### _definition:_ (associative) $A$-algebras

The **category of (unital, associative) $A$-algebras** is $\mathsf{Alg}_{A}$ the category of objects under central homomorphisms $A$ in $\mathsf{nCRing}$ (non-commutative rings).

Then, each **$A$-algebra** is then a structure homomorphism $f_{R} : A \to R$ with $\operatorname{img} f_{R} \subseteq Z(R)$. Each homomorphism of $A$-algebras is a rng homomorphism $R \to S$ so that the triangle below
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& A \ar[rd] \ar[ld] \\
		R \ar[rr] & & S
	\end{tikzcd}
\end{document}
```

---

We say $A$ acts on $R$ by scaling. Let $r, s \in R$ and $a \in A$. Then $a \cdot r = f_{R}(a) r$. Further, $(a \cdot r) s = r (a \cdot s) = a \cdot (rs)$. For these identities, we need $A$ to lie in the centre of $R$. Although it will already commute with itself, it will not necessarily commute with everything else if it doesn't lie in the centre.
