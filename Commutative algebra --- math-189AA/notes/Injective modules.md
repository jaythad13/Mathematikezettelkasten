---
tags:
- math-189AA/14
- comm-alg
- hom-alg
---

Injectives are defined dually to [[Commutative algebra --- math-189AA/notes/Projective modules#_theorem _ characterising projective modules|projective modules]]. We don't really have a dual to saying projective modules are direct summands of free modules. However, we can reverse all the arrows in the commutative diagram defining

##### _definition:_ injective modules

An $A$-module $E$ is **injective** if for each injection $\rho : N \to M$ and each homomorphism $h : N \to E$ there is a map $\overline{h} : M \to E$ such that $h = \overline{h} \circ \rho$. 

That is, the following diagram commutes
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		N \ar[r, hook, "\rho"] \ar[rd, "h"] & M \ar[d, dashed, "\overline{h}"] \\
		& E
	\end{tikzcd}
\end{document}
```

##### _example:_ injective modules

$\mathbb{Q}$ and $\mathbb{Q} / \mathbb{Z}$ are injective $\mathbb{Z}$-modules

---