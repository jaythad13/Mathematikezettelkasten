---
tags:
- math-189AA/22
- comm-alg
- hom-alg
---

Let $A$ be a ring.

Much like $\operatorname{Ext}$ for $\operatorname{Hom}$, $\operatorname{Tor}$ allows us to continue the [[Algebraic geometry --- rising-sea/notes/Tensor products, categorically#_proposition _ tensoring is functorial and right-exact|right-exactness of tensoring]] to a long exact sequence in homology. Unlike $\operatorname{Ext}$, here we use homology instead of cohomology. (Basically we number the maps a little differently)

##### _definition:_ $\operatorname{Tor}$, Tor-sion functor

Let $M, N$ be $A$-modules. For $P_{\bullet}$, a [[Commutative algebra --- math-189AA/notes/Projective resolutions#_definition _ projective resolution, syzygies|projective resolution]] of $M$,
$$
\operatorname{Tor}_{i}^A(M, N) = H_{i}(P_{\bullet} \otimes N).
$$

---

$\operatorname{Tor}$ is well-defined for the same reason that $\operatorname{Ext}$ is well-defined.

One good reason to care about $\operatorname{Tor}$ is that [[Commutative algebra --- math-189AA/notes/Betti numbers#_proposition _ computing Betti numbers from $ operatorname{Tor}$|it makes computing Betti numbers]] easy.

##### _example:_

Consider some $\mathbb{Z}$-module $N$ against $\mathbb{Z} / (p)$. We can think of this as computing $\operatorname{Tor}_{i}^\mathbb{Z}(\mathbb{Z} / (p), N)$. The following is a projective resolution of $\mathbb{Z} / (p)$.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \mathbb{Z} \ar[r, "\times p"] & \mathbb{Z} \ar[rd, two heads] & & 0. \\
		& & & \mathbb{Z} / (p) \ar[ru]
	\end{tikzcd}
\end{document}
```
Tensoring with $N$, we get
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & N \ar[r, "\times p"] & N \ar[r] & 0
	\end{tikzcd}
\end{document}
```

---