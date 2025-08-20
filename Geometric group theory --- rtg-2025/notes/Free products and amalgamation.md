---
tags:
- alg
- rtg-2025
---

The free product of groups $G, H$ allows mixing the symmetries of $G$ and $H$ freely in exactly the way that the regular product strictly prohibits.

In the regular product $G \times H$ you only allow elements of $G$ to multiply with elements of $G$ and only allow elements of $H$ to multiply with elements of $H$. For example, $(g_{1}, h_{1}) (g_{2}, h_{2}) = (g_{1} g_{2}, h_{1} h_{2})$. In the free product, we want to be able to get $g_{1} g_{2} h_{1} h_{2}$, but we also want $g_{1} h_{1} g_{2} h_{2}$ as a separate, meaningful element, and similarly for $g_{1} h_{1} h_{2} g_{2}$, and so on. 

In other words, if $G$ and $H$ have [[Geometric group theory --- rtg-2025/notes/Free groups and presentations#_examples _ group presentations|presentations]] $G = \left< S_{G} \mid R_{G} \right>$ and $H = \left< S_{G} \mid R_{G} \right>$, we want their free product to have presentation $\left< S_{G} \sqcup S_{H} \mid R_{G} \sqcup R_{H} \right>$. This is a valid definition of the free product, but a better one is categorical.

##### _definition:_ free product, coproduct of groups

For groups $G$ and $H$, their free product, denoted $G * H$, is their [[Algebraic geometry --- rising-sea/notes/Universal properties and why categories?#Definitions by universal property|categorical coproduct]]. 

Since this is the categorical coproduct, we may also write $G * H = G \coprod H$ and $\coprod_{i \in \mathcal{I}} G_{i}$ for the coproduct of groups indexed by $\mathcal{I}$.

Thus, $G * H$ has morphisms $\gamma : G \to G * H$ and $\eta : H \to G * H$ satisfying the following universal property. For any group $P$ with homomorphisms $G \to P$ and $H \to P$, there is a unique homomorphism $G * H \to P$ so that the morphisms from $G$ and $H$ factor through it. That is, the following diagram commutes.
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		& G \ar[d, "\gamma"] \ar[rdd, bend left] \\
		H \ar[r, "\eta"] \ar[rrd, bend right] & G * H \ar[rd, dashed, "\exists !"] \\
		& & P
	\end{tikzcd}
\end{document}
```

We can verify that the $\left< S_{G} \sqcup S_{H} \mid R_{G} \sqcup R_{H} \right>$ really does satisfy this universal property. First choose $\gamma$ to be the identity on $S_{G}$ and $\eta$ to be the identity on $S_{H}$. Then for any $\gamma' : G \to P$ and $\eta' : H \to P$ we can choose $\amalg : G * H \to P$ such that $\amalg(g) = \gamma'(g)$ for any $g \in S_{G}$ and similarly for $h \in S_{H}$ and extending by requiring $\amalg$ be a homomorphism.

It suffices to show it is well-defined in the case $\amalg(gh) = \amalg(g) \amalg(h)$ since for every other product $\amalg$ is already equal to a well-defined homomorphism. Suppose a distinct (reduced) word $w$ in $\left< S_{G} \sqcup S_{H} \right>$ is sent to $g h$ under the universal map $\varphi : F_{S} \to G * H$ determined by $g \mapsto g$ on $S_{G}$ and $h \mapsto h$ on $S_{H}$. Then since the only relations are those in $R_{G}$ and $R_{H}$, it follows that $w = w_{1} g w_{2} h w_{3}$ where $w_{i}$ are composed of trivial words in $G$ or $H$. Now, it follows easily that $\amalg(\varphi(w)) = \amalg(gh)$. 

It's clear that $\amalg$ is unique since any map satisfying the requirements must agree with $\amalg$ on $G$ and $H$, thus on generators, and finally on all of the free product.

##### _example:_ the free product of $\mathbb{Z}$

$\mathbb{Z} * \mathbb{Z}$ is the [[Geometric group theory --- rtg-2025/notes/Free groups and presentations#_definition _ free group|free group]] on two generators, and in general $\coprod_{i = 1}^n \mathbb{Z} \cong F_{n}$. From the generator/relator definition, this just follows immediately — 
$$
\coprod_{i = 1}^n \mathbb{Z} = \left< \bigsqcup_{i = 1}^n \{ x \} \right> \cong \left< \{ g_{1}, \dots, g_{n} \} \right> = F_{n}.
$$

### Amalgamations

Sometimes we don't quite want the free product of two groups — we want certain relations to hold. In particular, it's common (for instance, in the Seifert–van Kampen theorem) to have (injective) maps $K \to G$ and $K \to H$ and want only one copy of $K$ in $G * H$. The group we desire is an amalgamation.

If $i_{G} : K \to G$ and $i_{H} : K \to H$ are injections and $G, H$ have presentations as before, then the resulting amalgamation is $\left< S_{G} \sqcup S_{H} \mid R_{G} \sqcup R_{H} \sqcup \{ i_{G}(k) i_{H}(k)^{-1} \mid k \in K \} \right>$. Again, this is a perfectly good definition, but a better one comes from category theory.

##### _definition:_ free product with amalgamation, co-fibred product of groups

Given groups $G, H$ and a group $K$ with inclusions $i_{G} : K \to G$ and $i_{H} : K \to H$, the free product amalgamated along the inclusions, the corresponding [[Algebraic geometry --- rising-sea/notes/Fibred products#_definition _ co-fibred product|co-fibred product]] or co-(rresponding fibred product) is the unique object $G *_{K} H$ with maps $\gamma : G \to G *_{K} H$ and $\eta : H \to G *_{K} H$ such that the following diagram commutes for any $P$ with maps $G \to P$ and $H \to P$. Note that the diagram commuting requires the maps from $G, H$ to the amalgamation and to $P$ to agree on $K$
```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		K \ar[r, hook] \ar[d, hook] & G \ar[d, "\gamma"] \ar[rdd, bend left] \\
		H \ar[r, "\eta"] \ar[rrd, bend right] & G *_{K} H \ar[rd, dashed, "\exists !"] \\
		& & P
	\end{tikzcd}
\end{document}
```


Note that though the inclusions are obscured in the notation $G *_{K} H$, the construction does depend on them.

##### _example:_ the free product is trivially amalgamated

The free product of any two groups $G, H$ is the amalgamation under $1$, the trivial group with its unique injections into $G$ and $H$.