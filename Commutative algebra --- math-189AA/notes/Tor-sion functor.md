---
tags:
- math-189AA/22
- math-189AA/23
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

$\operatorname{Tor}$ is well-defined for the same reason that $\operatorname{Ext}$ is well-defined. We have not proved this yet, but $\operatorname{Tor}_{i}^A(M, N) = \operatorname{Tor}_{i}^A(N, M)$, and thus we can calculate $\operatorname{Tor}_{i}^A(M, N) = H_{i}(M \otimes P_{\bullet})$ from a projective resolution of $N$ instead. This is essentially because $M \otimes N = N \otimes M$.

One good reason to care about $\operatorname{Tor}$ is that [[Commutative algebra --- math-189AA/notes/Betti numbers#_proposition _ computing Betti numbers from $ operatorname{Tor}$|it makes computing Betti numbers]] easy.

##### _example:_ $\operatorname{Tor}$ against a cyclic module

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

The homology in the $0$th spot is $N / p N$ and the homology before it is $\{ n \in N \mid pn = 0 \}$ which is the set of $p$-torsion elements ($\operatorname{Tor}$ is short for torsion). All other $\operatorname{Tor}$ are $0$.

---

### Properties of $\operatorname{Tor}$

Many of the following properties of $\operatorname{Tor}$ follow from almost exactly the same proofs as for $\operatorname{Ext}$.

##### _proposition:_ $\operatorname{Tor}_{0}$ is the tensor product

For any two $A$-modules $M, N$, we have $\operatorname{Tor}_{0}^A(M, N) = M \otimes N$

---

##### _proposition:_ the long exact sequence of $\operatorname{Tor}$s

For any short exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & M' \ar[r] & M \ar[r] & M'' \ar[r] & 0
	\end{tikzcd}
\end{document}
```
there is a long exact sequence of $\operatorname{Tor}$s
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\cdots \ar[r] & \mathrm{Tor}_{1}^A(M'', N) \ar[r] & \mathrm{Tor}_{1}^A(M, N) \ar[r] & \mathrm{Tor}_{1}^A(M'', N) \\
		\ar[r] & M' \otimes N \ar[r] & M \otimes N \ar[r] & M'' \otimes N.
	\end{tikzcd}
\end{document}
```

---