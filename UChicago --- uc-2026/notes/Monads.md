---
tags:
- alg-top
- uc-2026/alg-top/14
- uc-2026/alg-top/15
- peter-may
---

A monad is just a monoid in the category of endofunctors. They show up all the time, mostly when there are [[Algebraic geometry --- rising-sea/notes/Adjoint functors#_definition _ adjoint functors, left adjoint, right adjoint, adjoint pair|adjoint functors]].

##### _definition:_ monad

A **monad** on a category $\mathscr{C}$ is a functor $M : \mathscr{C} \to \mathscr{C}$ and with a multiplication [[Algebraic geometry --- rising-sea/notes/Natural transformations#_definition _ natural transformations, natural isomorphism, equivalence of categories|natural transformation]] $\mu : MM \to M$ and identity natural transformation $\eta : \operatorname{id}_{\mathscr{C}} \to M$ such that the monoid diagrams commute.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M M M  \ar[r, "\mu"] \ar[d, "M \mu"] & MM \ar[d, "\mu"] \\
		MM \ar[r, "\mu"] & M
	\end{tikzcd}
	\begin{tikzcd}
	    M \ar[r, "\eta"] \ar[rd, "\mathrm{id}_{M}"'] & MM \ar[d, "\mu"] & M \ar[l, "M \eta"'] \ar[ld, "\mathrm{id}_{M}"] \\
	    & M
	\end{tikzcd}
\end{document}
```

---

##### _definition:_ algebra over a monad

A functor $A : \mathscr{C} \to \mathscr{C}$ is an **algebra over a monad** $M$ on $\mathscr{C}$ if there is a structure natural transformation $\theta : M A \to A$ such that the algebra diagrams commute.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		M M A \ar[r, "\mu"] \ar[d, "M \theta"] & M A \ar[d, "\theta"] \\
		M A \ar[r, "\theta"] & A
	\end{tikzcd}
	\begin{tikzcd}
	    A \ar[r, "\eta"] \ar[rd, "\mathrm{id}_{A}"'] & M A \ar[d, "\theta"] \\
	    & A 
	\end{tikzcd}
\end{document}
```

---

### Beck monadicity

Let $\Gamma = \Omega \Sigma$ be the endofunctor $\mathscr{T} \to \mathscr{T}$. 

##### _definition:_ monadic pair

A pair of adjoint functors $\Sigma, \Omega$ between $\mathscr{S}$ and $\mathscr{T}$ is **monadic** if $\Sigma_{\Gamma}, \Omega_{\Gamma}$ is an adjoint equivalence 

---

##### _theorem:_ Beck monadicity

A pair of adjoint functors $\Sigma, \Omega$ is monadic if and only if $\Omega$ creates coequalisers of **$\Omega$-split pairs**. That is, for any $\Omega$-split pair.

fork $h \circ f = h \circ g : A \to B \to C$ such that there are retracts

---