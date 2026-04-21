---
tags:
- rising-sea/7/4
- alg-geo
---

Let $S_{\bullet}, R_{\bullet}$ be graded rings.

Just as ring homomorphisms $B \to A$ define [[Algebraic geometry --- rising-sea/notes/Morphisms of affine schemes#_definition _ morphism of affine schemes|morphisms of affine schemes]] $\operatorname{Spec} A \to \operatorname{Spec} B$, morphisms of graded rings $S_{\bullet} \to R_{\bullet}$ will define [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ morphism of schemes|morphisms]] of [[Algebraic geometry --- rising-sea/notes/Projective schemes#_definition _ projective $A$-schemes, quasiprojective $A$-schemes|projective schemes]] $\operatorname{Proj} R_{\bullet} \to \operatorname{Proj} S_{\bullet}$ except not quite. For one, this construction will actually give a morphism from an open subset of $\operatorname{Proj} R_{\bullet}$ that is not always the whole scheme. For another, this "functor" is neither full nor faithful — not all morphisms of projective schemes come from such maps and different morphisms of graded rings can give the same map of projective schemes.

##### _definition:_ morphism of graded rings

A **morphism of $\mathbb{Z}_{\geq 0}$-graded rings** $\varphi : S_{\bullet} \to R_{\bullet}$ is a ring homomorphism $\varphi : S_{\bullet} \to R_{\bullet}$ such that we always have $\varphi^\text{img}(S_{n}) \subseteq R_{dn}$ for some positive integer $d$.

---

##### _example:_ embedding $\mathbb{P}^1$ in $\mathbb{P}^2$

We know that the map $\pi : \mathbb{P}^1_{\mathbb{C}} \to \mathbb{P}^2_{\mathbb{C}}$ by $(x : y) \mapsto (x^{20} : x^{9} y^{11} : y^{20})$ on closed points should give a morphism of schemes — it is algebraic and homogeneous in each coordinate. 

Consider $\operatorname{Spec} \mathbb{C}[x] = D_{+}(y) \subseteq \mathbb{P}^1$. We have $\pi^\text{img}(D_{+}(y)) \subseteq D_{+}(w) \subseteq \operatorname{Proj} \mathbb{C}[u, v, w]$. On this set we can think of this as the morphism induced by $\mathbb{C}[u / w, v / w] \to \mathbb{C}[x / y]$ with $u / w \mapsto (x / y)^{20}$ and $v / w \mapsto (x / y)^9$. Similarly, we have $\pi_{\mid D_{+}(x)} : D_{+}(x) \to D_{+}(u)$ induced by $\mathbb{C}[v / u, w / u] \to \mathbb{C}[y / x]$ with $v / u \mapsto (y / x)^{11}$ and $w / u \mapsto (y / x)^{20}$. We can see that both of these ring homomorphisms are induced (not-uniquely) by the $\mathbb{Z}_{\geq 0}$-graded ring morphism $\mathbb{C}[u, v, w] \to \mathbb{C}[x, y]$ with $u, v, w \mapsto x^{20}, x^{9} y^{11}, y^{20}$ respectively. For example, any scaling of this morphism by $p(x, y) \in \mathbb{C}[x, y]$ would return the same morphism of schemes.

---

##### _proposition, definition:_ morphisms of graded rings induce morphisms of projective schemes

Suppose $\varphi : S_{\bullet} \to R_{\bullet}$ is a morphism of schemes. Then there is a [[Algebraic geometry --- rising-sea/notes/Morphisms of schemes#_definition _ morphism of schemes|morphism of schemes]]
$$
\operatorname{Proj} \varphi : \operatorname{Proj} R_{\bullet} \setminus V(\varphi^\text{img}(S_{+})) \to \operatorname{Proj} S_{\bullet}.
$$

If $\varphi^\text{img}(S_{+}) = \text{Ø}$, then $\operatorname{Proj} \varphi : \operatorname{Proj} R_{\bullet} \to \operatorname{Proj} S_{\bullet}$.

We call $\operatorname{Proj} \varphi$ the **scheme morphism induced by $\varphi$**.

###### _proof sketch:_

The set of all $D_{+}(\varphi(f)) \subseteq \operatorname{Proj} R_{\bullet}$ with homogeneous $f \in S_{+}$ [[Algebraic geometry --- rising-sea/notes/Projective schemes#_proposition _ the projective distinguished opens form a basis|cover]] $\operatorname{Proj} R_{\bullet} \setminus V(\varphi^\text{img}(S_{+}))$. Thus, it suffices to give morphisms of schemes $D_{+}(\varphi(f)) \to D(f)$ that agree on intersections. 

Clearly $\varphi : S_{\bullet} \to R_{\bullet}$ gives $\varphi_{f} : (S_{\bullet})_{f} \to (R_{\bullet})_{\varphi(f)}$. Since $\varphi$ preserves degree up to an integer multiplication, this map preserves the degree $0$ pieces. That is, we have $(\varphi_{f})_{0} : ((S_{\bullet})_{f})_{0} \to ((R_{\bullet})_{\varphi(f)})_{0}$ giving a morphism of schemes $D_{+}(\varphi(f)) \to D_{+}(f)$. 

Since $D_{+}(\varphi(f)) \cap D_{+}(\varphi(g)) = D_{+}(\varphi(f) \varphi(g)) = D_{+}(\varphi(fg))$, on intersections the two morphisms are $\operatorname{Spec} ((\varphi_{g})_{0})_{f_{g}} = \operatorname{Spec} (\varphi_{fg})_{0} = \operatorname{Spec} ((\varphi_{f})_{0})_{g_{f}}$. This equality follows from the [[Algebraic geometry --- rising-sea/notes/Projective schemes#_proposition _ gluing sheaves over the affine cover of a projective scheme|the corresponding isomorphism of rings]] that fits into the commutative diagram below.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
	    ((S_{\bullet})_{fg})_{0} \ar[r] \ar[d] & ((R_{\bullet})_{fg})_{0} \ar[d] \\
		(((S_{\bullet})_{f})_{0})_{g_{f}} \ar[r] & (((R_{\bullet})_{f})_{0})_{g_{f}}
	\end{tikzcd}
	
	\begin{tikzcd}
		\frac{s}{f^m g^n} \ar[r, mapsto] \ar[d, mapsto] & \frac{\varphi(s)}{\varphi(f)^m \varphi(g)^n} \ar[d, mapsto] \\
	    \frac{s g^{n (\deg f - 1)}}{f^m f^{n \deg g} g_{f}^n} \ar[r, mapsto] & \frac{\varphi(s) \varphi(g)^{n (\deg f - 1)}} {\varphi(f)^m \varphi(f)^{n \deg g} \varphi_{f}(g_{f})^n}
	\end{tikzcd}
\end{document}
```

---

The following obvious lemma is useful to check when $\varphi$ induces a fully defined morphism $\operatorname{Proj} R_{\bullet} \to \operatorname{Proj} S_{\bullet}$.

##### _lemma:_ $\varphi$ induces a full morphism if the image of irrelevant ideal is irrelevant

Suppose $\varphi : S_{\bullet} \to R_{\bullet}$ is a morphism of graded rings. Let $\mathfrak{i}_{\bullet} \subseteq R_{\bullet}$ be the ideal generated by $\varphi^\text{img}(S_{+})$. The vanishing set $V(\mathfrak{i}_{\bullet}) = \text{Ø}$ if and only if $\sqrt{ \mathfrak{i}_{\bullet} } = R_{+}$.

###### _proof:_

If $\sqrt{ \mathfrak{i}_{\bullet} } = R_{+}$ [[Algebraic geometry --- rising-sea/notes/Projective schemes#_proposition _ the irrelevant ideal really is irrelevant|then]] $V(\mathfrak{i}_{\bullet}) = \text{Ø}$.

If $V(\mathfrak{i}_{\bullet}) = \text{Ø}$, [[Algebraic geometry --- rising-sea/notes/Projective schemes#_proposition _ the irrelevant ideal really is irrelevant|then]] $R_{+} \subseteq \sqrt{ \mathfrak{i}_{\bullet} }$. Since $\varphi^\text{img}(S_{n}) \subseteq R_{dn} \subseteq R_{+}$ whenever $d, n > 0$, we have the reverse inclusion also.

---

##### _example:_ different ring homomorphisms that induce the same scheme morphism

Consider $S_{\bullet} = \mathbb{F}[x, y, z] / (xz, yz, z^{2})$ and $R_{\bullet} = \mathbb{F}[u, v, w] / (uw, vw, w^{2})$. Clearly there is an isomorphism $S_{\bullet} \to R_{\bullet}$ by $x, y, z \mapsto u, v, w$ respectively. This induces an isomorphism $\operatorname{Proj} R_{\bullet} \to \operatorname{Proj} S_{\bullet}$.

Also consider the map $x, y, z \mapsto u, v, 0$. [[Algebraic geometry --- rising-sea/notes/Projective schemes#_corollary _ containment of projective distinguished opens|Since]] $D_{+}(w) \subseteq D_{+}(w^{2}) = \text{Ø}$ in $\operatorname{Proj} R_{\bullet}$, $D_{+}(u)$ and $D(v)$ cover it. This ring homomorphism induces exactly the same morphism $D_{+}(u) \to D_{+}(x)$ as the ring isomorphism — $xz = 0$ implies $z = 0$ everywhere on $D_{+}(x)$ anyway. The same story is true for $D_{+}(v) \to D_{+}(y)$. Since the two morphisms are the same on the cover, they glue to the same morphism.

This also gives an isomorphism $\operatorname{Proj} S_{\bullet} \to \mathbb P^1_{\mathbb{F}} = \operatorname{Proj} \mathbb{F}[u, v]$.

---