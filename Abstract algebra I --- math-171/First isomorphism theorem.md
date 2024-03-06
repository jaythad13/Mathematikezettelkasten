---
tags:
- math-171
- alg
lecture:
- math-171-12
---

Last time we stated the first isomorphism theorem. We restate it here. 

##### _theorem:_ the first isomorphism theorem

If $\varphi : G \to H$ is a group homomorphism, then
1) $\ker \varphi \le G$
2) $G / \ker \varphi \cong \varphi(G)$

To understand it better, lets recall the idea of [[Exact sequences|exact sequences]] and in particular, [[Exact sequences#_example _ short exact sequence|the short exact sequence]]. We will look at some interesting things that the first isomorphism theorem tells us about short exact sequences.

##### _example:_ short exact sequences for the first isomorphism theorem

For $Z_{n} = \left< x \right>$, is the following sequence exact?
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & n \mathbb Z \ar[r, hook] & \mathbb Z \ar[r, "\varphi"] &  Z_n \ar[r] & 0
	\end{tikzcd}
\end{document}
```
Here $\varphi : z \mapsto x^z$.

Yes! The first map is fine because it has to be, the second map is an inclusion and thus, only sends $0$ to $0$, the third map sends exactly the multiples of $n$ to $x^n = 0$, and the last map sends everything to $0$, while the third map is surjective, so we're good.

More generally, for a surjective homomorphism $\varphi$, is
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & \ker \varphi \ar[r, hook] & B \ar[r, "\varphi", two heads] & C \ar[r] & 0
	\end{tikzcd}
\end{document}
```
exact?

Yes! The first map is obviously fine, the second map is an inclusion, and therefore injective, the image of the inclusion of $\ker \varphi$ is obviously just $\ker \varphi$, and then $\varphi$ is surjective by definition.

Even more generally, for an exact sequence,
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
			0 \ar[r] & A \ar[r, "\varphi"] & B \ar[r, "\psi"] & C \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is $A \cong \ker \psi$?

Yes! $\operatorname{im} \varphi = \ker \psi$ but since $\varphi : A \to \operatorname{im} \varphi$ is obviously surjective, and is defined to be injective (by the short exact sequence), we have $A \cong \operatorname{im} \varphi =  \ker \psi$.

##### _examples:_ quotient isomorphisms using the first isomorphism theorem

Is there a homomorphism $\varphi : D_{8} \to \mathbb{Z}/2\mathbb{Z}$ with $\ker \left< r \right>$.

Yes! Define $\varphi$ by $s \mapsto \bar{1}$ and $r \mapsto \bar{0}$.

Thus, $D_{8} /\left< r \right> \cong \mathbb{Z} / 2 \mathbb{Z}$. This is basically saying that if we ignore rotations, flipping a square around an axis of symmetry is just the same as flipping between odd and even numbers.

More generally, given an exact sequence
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		0 \ar[r] & A \ar[r, "\varphi"] & B \ar[r, "\psi"] & C \ar[r] & 0
	\end{tikzcd}
\end{document}
```
is $B / \operatorname{im} \varphi \cong C$?

Yes! Since $\operatorname{im} \varphi = \ker \psi$, by quotienting it out, we're just getting rid of the null space. Since $\psi$ has to be surjective (by the exact sequence), we have that $\psi$ takes equivalence classes to all of $G$.

##### _examples:_ some interesting isomorphisms

1) $\pi : \mathbb{R}^2 \to \mathbb{R}$ by $(x, y) \mapsto x + y$ gives us that the $\mathbb{R}/L \cong \mathbb{R}$ where $L$ is the line by $y = -x$. This is just the same as the standard vector space quotient where it corresponds to all of the ways that you could move the line around parallel to itself.
2) $\varphi : \mathbb{R}^\times \to \mathbb{R}^\times$ by $x \mapsto \lvert x \rvert$ gives us that $\mathbb{R} / \{ 1, -1 \} = \mathbb{R}_{> 0}^\times$. Basically, identifying $1$ with $-1$ with the group structure forces us to fold over the real line until we only have the positive reals.
3) $\psi : \mathbb{C}^\times \to \mathbb{R}^\times$ by $z \to \lvert z \rvert^2$ gives us that $\mathbb{C}^\times /\{ z \in \mathbb{C} : \lvert z \rvert = 1 \} \cong \mathbb{R}^\times_{> 0}$. This corresponds to how getting rid of all of the angles is just reducing the complex numbers to their distance from the 
4) $\theta : \mathbb{Z} / 8 \mathbb{Z} \to \mathbb{Z} / 4 \mathbb{Z}$ tells us that $\mathbb{Z} / 8 \mathbb{Z} \big / \left< \bar{4} \right> \cong \mathbb{Z} / 4 \mathbb{Z}$.