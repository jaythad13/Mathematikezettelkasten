---
tags:
- math-171
- alg
lecture:
- math-171-12
- math-171-14
- math-171-15
---

### The first isomorphism theorem

[[Fibres and quotients|Last time]] we stated the first isomorphism theorem. We restate it here. 

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

### The second isomorphism theorem

The second isomorphism theorem tells us how [[Centralisers, centre, normalisers, and stabilisers#_definition _ normaliser, $N_{G}(A)$|normality type conditions]] allow us to take the product of groups. For this, we need to define the product of subgroups, and prove that it really is a group.

##### _definition, theorem:_ product of subgroups, the product of subgroups is a group

Let $H, K$ be subgroups of $G$. We say the product of $H$ and $K$ is
$$
HK = \{ hk | h \in H, k \in K \}.
$$

1) If $\lvert H \rvert, \lvert K \rvert < \infty$, then $\lvert HK \rvert = \frac{\lvert H \rvert \lvert K \rvert}{\lvert H \cap K \rvert}$.
2) $HK \le G$ if and only if $HK = KH$.
3) If $H \le N_{G}(K)$ then $HK \le G$.
4) If $K \trianglelefteq G$, then $HK \le G$.

###### _proof (sketch?):_

1) Basically, $h_{1}K = h_{2}K$ are the same if and only if $h_{1}(K \cap H) = h_{2}(K \cap H)$. Thus, there are $\frac{\lvert H \rvert}{\lvert H \cap K \rvert}$ cosets of $H \cap K$, and thus, that many cosets of $K$ in $H$. There are $\lvert K \rvert$ elements in each of those cosets. The disjoint union of all of these cosets is just $HK$ and thus, has cardinality $\lvert HK \rvert = \frac{\lvert H \rvert \lvert K \rvert}{\lvert H \cap K \rvert}$.
2) Suppose $HK \le G$. Then for all $k \in K$ and all $h \in H$ we have $k, h \in HK$. Since $HK$ is a group, we must have $kh \in HK$. Thus, $KH \subset HK$. For any $hk \in HK$ we must also have $(hk)^{-1} = h' k'$, (where $h' \in H, k' \in K$) and thus, $hk = (h'k')^{-1}$. But we know that then $hk = k'^{-1} h'^{-1} \in KH$. Thus, $HK \subset KH$.
	Suppose $HK = KH$. Note that $HK$ is nonempty since $1_{G}$ must be in $HK$. Suppose we have $hk, h'k' \in HK$ with $h, h' \in H$ and $k, k' \in K$. Then we can write
	$$
\begin{split}
hk (h'k')^{-1} & = hkk'^{-1} h'^{-1} \\
& = h h'' k'' \\
 & \in HK
\end{split}
$$
	where the second step (that $kk'^{-1}h'^{-1} = h'' k''$) follows from $HK = KH$.
3) If $H \le N_{G}(K)$, then for any $h \in H$, $hK = Kh$. Since this is true for all $h$, $HK = KH$. By 2), $HK \le G$.
4) If $K$ is a normal subgroup of $G$, then $H \le G = N_{G}(K)$ and thus, by 3) $HK \le G$.

##### _theorem:_ the second isomorphism theorem

Let $H, K$ be subgroups of $G$ where $H \le N_{G}(K)$. Then
1) $H \cap K \trianglelefteq H$
2) $HK / K \cong H/H \cap K$.

###### _proof:_

1) For any $h \in H$, $x \in H \cap K$, we want to show that $hxh^{-1} \in H \cap K$. Note that $hxh^{-1}$ is obviously in $H$. Note that since $x \in K$, $x \in hKh^{-1} = K$ (since $H \le N_{G}(K)$). Thus $H \cap K$ is a normal subgroup of $H$.
2) Suppose $hk = h' k'$, (for $h, h' \in H$, $k, k' \in K$). We want $h'^{-1} h \in H \cap K$. We have $h'^{-1}h = k' k^{-1}$ and thus it is in both $H$ and $K$ and thus is in $H \cap K$. Thus the map $$
\begin{split}
\varphi & : HK \to H/H \cap K \\
 & : hk \mapsto h(H \cap K)
\end{split}
$$
	is well defined (any two different representations of $hk$ have $h, h'$ that differ only by an element in $H \cap K$). Note that in $hkh'k'$, $kh' = h'k''$ for some $k'' \in K$ since $h \in N_{G}(K)$. Thus, $hkh'k' = hh'k''k'$. Thus,
	$$
\begin{split}
\varphi(hkh' k') & = \varphi(hh'k''k') \\
 & = hh'(H \cap K) \\
 & = h(H \cap K) h'(H \cap K) \\
 & =  \varphi(hk) \varphi(h' k')
\end{split}
$$
	where the second to last equality follows from the fact that $H/H \cap K$ [[Normal subgroups#_theorem _ quotients are only those of normal subgroups|is a group]]. Thus $\varphi$ is a homomorphism. Note that it is surjective since for any $h(H \cap K)$, we have $\varphi(h) = h(H \cap K)$. Also note that it has kernel $K$ — any $k \in K$ is clearly mapped to $H \cap K$. If $hk \in \ker \varphi$, then $h(H \cap K) = H \cap K$ giving us $h \in H \cap K$ and thus $h \in K$.
	Then by the [[#_theorem _ the first isomorphism theorem|the first isomorphism theorem]],
	$$
HK / K \cong H / H \cap K
$$
	since $K = \ker \varphi$.

Notice that this gives us the following lattice
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& G \\
		& HK \ar[u] \\
		H \ar[ru] & & K \ar[lu, "\trianglelefteq"] \\
		& H \cap K \ar[lu, "\trianglelefteq"] \ar[ru]
	\end{tikzcd}
\end{document}
```

### The third isomorphism theorem

The third isomorphism tells us when quotients behave like fractions — how we can quotient out quotient groups by quotient groups.

##### _theorem:_ the third isomorphism theorem

Let $H, K$ be normal subgroups of $G$ with $H$ a subgroup of $K$. Then
1) $K / H \trianglelefteq G / H$.
2) $(G/H)/(K / H) \cong G / K$.

### The fourth isomorphism theorem

The fourth isomorphism theorem tells us that

##### _theorem:_ the fourth isomorphism theorem

Suppose $G$ is a group with normal subgroup $H$. Then there is a bijection between the set of subgroups of $G$ that contain $H$ and the subgroups of $G/H$ by $K \mapsto K/H$ for $H \le K$.