---
tags:
- cat-th
- basic-cat
- self-study
---

Category theory is about taking a bird's eye view of mathematics. Using categorical tools, you can spot and describe a phenomenon common to many different areas of mathematics.

The most important such phenomenon is the universal property. This is very tricky to nail down precisely in abstract terms, especially without categorical language to help, but eventually makes sense with enough examples. Thus, we're just going to give a bunch of them.

##### _example:_ the universal property on $\mathsf{Set}$

Let $\mathbf{1}$ denote a set with one element (we will see later that we consider all singleton sets to be the same in the category of sets). Then we have the following universal property.

For all sets $X$ there is exists a unique map (function) from $X$ to $\mathbf{1}$.

There are many categorical ways to say this — $\mathbf{1}$ satisfies a universal property on the category $\mathsf{Set}$, $\mathbf{1}$ is universal in $\mathsf{Set}$ (more specifically, it is initial, but we haven't got there yet).

While this seems like a trivial observation, this is worth noting because it allows us to know about the map from any set into $\mathbf{1}$. Of course, this is a trivial example, but seemingly trivial statements like this, can carry a lot more information when we're working in a category with more structure (whatever that means).

##### _informal definition:_ universal property

A phrase of the form "there exists a unique such and such satisfying some condition".

One example of a less trivial universal property is the following.

##### _example:_ $\mathbb{Z}$ is uniquely embedded in every ring

Note that from now on, by [[Rings|ring]], we always mean ring with a multiplicative identity $\mathcal{1}$. With this assumption, we can prove the following universal property.

For all rings $R$, there exists a unique [[Ring homomorphisms|homomorphism]] $\varphi : \mathbb{Z} \to R$.

To show existence, just consider
$$
\varphi(n) = \begin{cases}
\underbrace{ \mathcal{1} + \dots + \mathcal{1} }_{ n \text{ times} } & \text{if } n \in \mathbb{N} \\
\mathcal{0} & \text{if } n = 0 \\
- \varphi(-n) & \text{if } n < 0
\end{cases}
$$
This is clearly a homomorphism — identities and addition are clearly preserved, and we can show that multiplication is preserved because of distribution.
$$
\begin{split}
\varphi(mn) & = \underbrace{ \mathcal{1} + \dots + \mathcal{1} }_{ mn \text{ times} } \\
& = (\underbrace{ \mathcal{1} + \dots + \mathcal{1} }_{ m \text{ times} }) (\underbrace{ \mathcal{1} + \dots + \mathcal{1} }_{ n \text{ times} }) \\
& = \varphi(m) \varphi(n).
\end{split}
$$

To show uniqueness, consider any homomorphism $\psi : \mathbb{Z} \to R$. The definition of a homomorphism determines that we must have
$$
\begin{gathered}
\psi(0) = \mathcal{0} \\
\psi(1) = \mathcal{1} \\
\end{gathered}
$$
as well as the preservation of addition and multiplication. Thinking of $n$ as $\underbrace{ 1 + \dots + 1 }_{ n \text{ times} }$, and noting that $\psi(1) + \psi(-1) = 0$ and thus, $\psi(-1) = -\mathcal 1$, along with addition and multiplication preservation gives us $\psi = \varphi$.

We can see how this universal property is sort of the "opposite" property on the category of rings to what the previous one is on sets — all of the functions go out from $\mathbb{Z}$ instead of into $\mathbf{1}$. It was easy to believe that any singleton was the same since basically all sets have alone is their cardinality, and thus, it's easy to see that there is "essentially" only one $\mathbf{1}$ satisfying the universal property where "essentially" means upto bijections of sets. It turns out this is true for rings, only "essentially" means upto isomorphisms of rings.

##### _proposition:_ $\mathbb{Z}$ is the only ring uniquely embedded in every ring

If $A$ is a ring with a unique homomorphism to every ring $R$, then $A \cong \mathbb{Z}$.

###### _proof:_

If $A$ has a unique homomorphism to every ring $R$, then it has a unique homomorphism, $\varphi : A \to \mathbb{Z}$. Similarly, $\mathbb{Z}$ has a unique homomorphism to $\varphi' : \mathbb{Z} \to A$.

Since compositions of homomorphisms are homomorphisms, we have homomorphisms $\varphi \circ \varphi' : \mathbb{Z} \to \mathbb{Z}$ and $\varphi' \circ \varphi : A \to A$. However, we already have the unique homomorphisms $\operatorname{id}_{\mathbb{Z}}$ and $\operatorname{id}_A$ on $\mathbb{Z}$ and $A$ respectively. Thus, $\varphi \circ \varphi' = \operatorname{id}_{\mathbb{Z}}$ and $\varphi' \circ \varphi = \operatorname{id}_{A}$ making them inverses of each and the isomorphisms we wanted.

Note that this proof has basically nothing to do with ring theory — it basically only uses the fact that homomorphisms that are inverses of each other are isomorphisms which is just generally true for any "notion of isomorphism" one might define. We will see basically the exact same trick pop up again in proving that a universal property is uniquely satisfied for other universal properties.

##### _example:_ the basis determines a linear map

Suppose we have a [[Vector spaces|vector space]] $V$, and a choice of [[Bases|basis]] $(v_{s})_{s \in S}$. Choose a target vector space $W$. For every function $f : S \to W$, there is a unique linear map $T_{f} \in \mathcal{L}(V, W)$ such that $T_{f} \circ i = f$. Here $i(s) = v_{s}$ for all $s \in S$.

This basically amounts to the fact that a [[Linear maps|linear map from a vector space is uniquely determined by its values on the basis]]. We can rephrase this as $\Phi : \mathcal{L}(V, W) \to \{ f : S \to W \}$ given by $\Phi(T_{f}) = T_{f} \circ i$ is a bijection.

Here $T_{f}$ is satisfying the universal property.

We can often draw a commutative diagram to represent statements in category theory. In a commutative diagram, any paths from one object to another along arrows are the same. In the diagram below this means that $T_{f} \circ i = f$.

```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
		S \arrow[r, "i"] \arrow[dr, "\forall f"] & V \arrow[d, dashrightarrow, "\exists! \, T_f \in \mathcal L({V, W})"] \\
		& W
	\end{tikzcd}
\end{document}
```

##### _example:_ bilinear maps uniquely factor through the tensor product

Given vector spaces $U, V, W$ a bilinear map $f : U \times V \to W$ is a function that is linear in each variable — each function (for each $v \in V$) given by $u \mapsto f(u, v)$ is linear, and so is each function given by $v \mapsto f(u, v)$. The space of all such bilinear maps is $\mathcal{B}(U \times V, W)$.

It is a fact that there exists a vector space (called the tensor product) $U \otimes V$ and a bilinear map $b : U \times V \to U \otimes V$ with the following universal property (refer to [[Linear Algebra Done Right.pdf#page=393|tensor products]]):

```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
	U \times V \ar[r, "b"] \ar[dr, "\forall f \in \mathcal B({U \times V, W})"'] & U \otimes V \ar[d, dashrightarrow, "\exists ! \, T_f \in \mathcal L({U \otimes V, W})"] \\
	& W
	\end{tikzcd}
\end{document}
```

We can pull the same trick that we did with the rings to show that there is in fact only one vector space $U \otimes V$ through which every bilinear map $U \times V \to W$.

##### _proposition:_ bilinear maps uniquely factor only through the tensor product

Suppose we have another vector space $P$, satisfying the same commutative diagram. That is, we have both of the following diagrams commute.
```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
	U \times V \ar[r, "b"] \ar[dr, "\forall f \in \mathcal B({U \times V, W})"'] & U \otimes V \ar[d, dashrightarrow, "\exists ! \, T_f \in \mathcal L({U \otimes V, W})"] \\
	& W
	\end{tikzcd}
	\begin{tikzcd}
	U \times V \ar[r, "b'"] \ar[dr, "\forall f \in \mathcal B({U \times V, W})"'] & P \ar[d, dashrightarrow, "\exists ! \, T_f' \in \mathcal L({P, W})"] \\
	& W
	\end{tikzcd}
\end{document}
```

Then, $U \otimes V \cong P$ by an isomorphism $i$, such that $i \circ b = b'$.

###### _proof:_

We will try to prove this just using diagrams. 

The following diagrams must commute, since the diagrams in the hypothesis commute.
```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
	U \times V \ar[r, "b"] \ar[dr, "b'"'] & U \otimes V \ar[d, dashrightarrow, "\exists ! \, T_{b'} \in \mathcal L({U \otimes V, P})"] \\
	& P
	\end{tikzcd}
	\begin{tikzcd}
	U \times V \ar[r, "b'"] \ar[dr, "b"'] & P \ar[d, dashrightarrow, "\exists ! \, T_b' \in \mathcal L({P, U \otimes V})"] \\
	& U \otimes V
	\end{tikzcd}
\end{document}
```

Since $b' = T_{b'} \circ b$ and $b = T_{b}' \circ b'$ we have $b = T_{b}' \circ T_{b'} \circ b$ and $b' = T_{b'} \circ T_{b}' \circ b'$. That is, $T = T_{b}' \circ T_{b'} \in \mathcal{L}(U \otimes V)$ is the unique linear map that satisfies $T \circ b = b$ for the bilinear map $b : U \times V \to U \otimes V$ and $T' = T_{b'} \circ T_{b}' \in \mathcal{L}(U \otimes V)$ is the unique linear map that satisfies $T' \circ b' = b'$ for the bilinear map $b : U \times V \to P$.

However, we already have $\operatorname{id}_{U \otimes V}$ and $\operatorname{id}_{P}$ as those respective unique maps. Thus, we must have $T = \operatorname{id}_{U \otimes V}$ and $T' = \operatorname{id}_{P}$, giving us that $T_{b'}$ and $T_{b}'$ are inverses of each other, and thus isomorphisms. Specifically, $T_{b'}$ is the desired isomorphism $i$. The diagrams hint at this isomorphism since you pretty much can't tell $U \otimes V$ and $P$ apart.

Although, we've stayed mainly algebraic, we can also have topological universal properties — they are just as common

##### _example:_ every map from the discrete space is continuous

Let $S$ be a set, and let $\mathcal{D}(S)$ be $S$ endowed with the [[Metric spaces#_examples _ metric spaces|discrete topology]]. Since every subset is open, any function $F$, from $S$ to a topological space $X$ is defines a unique continuous function $f$ from $\mathcal{D}(S)$ to $X$ that agrees with $F$ everywhere — just set $f(s) = F(s)$. That is, for $i : S \to \mathcal{D}(S)$ by $s \mapsto s$, the following diagram commutes.

```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
		S \ar[r, "i"] \ar[rd, "\forall F"'] & \mathcal D(S) \ar[d, dashrightarrow, "\exists ! \, f \in \mathcal C({\mathcal D(S), X})"] \\
		& X
	\end{tikzcd}
\end{document}
```

This works because the pre-image of any subset of $X$ under $f$, is just a subset of $S$, which is open in $\mathcal{D}(S)$.

##### _example:_ the gluing lemma is a universal property

The gluing lemma tells us that if a space $X$ is covered by its open subsets $U$ and $V$, then any functions from $U$ and $V$ to a space $Y$ that agree on $U \cap V$ define a unique continuous function from all of $X$ to $Y$. That is, the following diagram commutes (where all arrows are continuous functions).

```tikz
\usepackage{tikz-cd}
\begin{document}
	\begin{tikzcd}
			U \cap V \arrow[r, hook, "i"] \arrow[d, hook, "j"] & U \arrow[d, hook, "j'"] \arrow[ddr, bend left, "\forall f"] \\
			V \arrow[r, hook, "i'"] \arrow[drr, bend right, "\forall g"] & X \arrow[dr, dashrightarrow, "\exists ! \, h"] \\
						&&\forall Y
	\end{tikzcd}
\end{document}
```